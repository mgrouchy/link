import urllib
import requests
from urlparse import parse_qs
from oauth_hook import OAuthHook
from resources import ENDPOINTS
from functools import partial, update_wrapper


import simplejson


class LinkError(Exception):
    pass


class Link(object):
    """
    Link is the main interface for the linkedin Api
    """
    def __init__(self, linkedin_key, linkedin_secret,
                oauth_token=None, oauth_token_secret=None):
        """
        :param linkedin_key:
        :param linkedin_secret:
        :param oauth_token:
        :param oauth_token_secret:
        """

        # api urls
        self.base_api_url = 'https://api.linkedin.com'
        self.request_token_url = '%s/uas/oauth/requestToken' % self.base_api_url
        self.access_token_url = '%s/uas/oauth/accessToken' % self.base_api_url
        self.authorize_url = '%s/uas/oauth/authorize' % self.base_api_url

        # initialize vars and get our client
        self.linkedin_key = linkedin_key
        self.linkedin_secret = linkedin_secret
        if not (self.linkedin_key and self.linkedin_secret):
            raise LinkError

        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret

        self.client = self._get_authorized_client(self.linkedin_key, self.linkedin_secret,
                        oauth_token=self.oauth_token, oauth_token_secret=self.oauth_token_secret)
        self.request_token = None

    def _get_authorized_client(self, linkedin_key, linkedin_secret, oauth_token=None,
                                                        oauth_token_secret=None):
        """
        get Authorized Oauth Client using requests and an OAuthHook
        """
        OAuthHook.consumer_key = linkedin_key
        OAuthHook.consumer_secret = linkedin_secret

        oauth_hook = OAuthHook(access_token=oauth_token,
                    access_token_secret=oauth_token_secret, header_auth=True)

        client = requests.session(hooks={'pre_request': oauth_hook})
        return client

    def __getattr__(self, name):
        """
        Implement getattr to map Linkedin Endpoints from the endpoints dict
        to a partial of request.
        """
        try:
            endpoint = ENDPOINTS[name]
            func = partial(self.request, endpoint['url'], method=endpoint['method'])
            # update our partial with self.requests attributes
            update_wrapper(func, self.request)
            return func
        except KeyError:
            raise AttributeError

    def _get_field_selector_str(self, field_selectors=None):
        """
        Given a set of field_selectors in the format
            ('selector1, 'selector2', 'selector3')
            or
            ['selector1, 'selector2', 'selector3', ['s4', 's5']]

            return a field selector string in the format
                ":(selector1,selector2,selector3)
        """
        if not field_selectors:
            return ''

        def unpack_selectors(selector):
            if not isinstance(selector, (tuple, list)):
                return ',%s' % selector
            else:
                l = ':(%s)' % ''.join([unpack_selectors(s) for s in selector])
                return l.replace('(,', '(')

        return unpack_selectors(field_selectors)

    def _build_endpoint_url(self, endpoint, method, data=None, named_params=None, field_selectors=None):
        """
            Given an endpoint and params, construct a proper linkedin url
        """
        if named_params:
            named_param_str = '%s=%s'.join((k, v) for k, v in named_params.iteritems())
        else:
            named_param_str = '~'

        if field_selectors:
            field_selector_str = self._get_field_selector_str(field_selectors)

        endpoint = endpoint % ({
                                'named_params': named_param_str,
                                'field_selectors': field_selector_str,
                              })

        # get our querystring
        if method == 'get':
            if data:
                endpoint = '%s?%s' % (endpoint, urllib.urlencode(data))

        return endpoint

    def request(self, endpoint, method='GET', data=None, named_params=None, field_selectors=None):
        """
        Execute a Linkedin API request
        :param endpoint:
        :param method:
        :param data:
        :param field_selectors:
        """
        method = method.lower()

        headers = {'x-li-format': 'json'}

        if method not in ['get', 'post', 'delete', 'put']:
            raise LinkError

        _client = getattr(self.client, method)
        if not _client:
            raise LinkError

        endpoint = self._build_endpoint_url(endpoint, method, data=data,
                    named_params=named_params, field_selectors=field_selectors)

        response = _client(endpoint, data=data, headers=headers)

        content_dict = simplejson.loads(response.content)
        return content_dict

    def get_authorization_url(self, token, callback=None):
        """
        Get an Authorization url developers can put in their app to get user to
        authorize a linkedin connection
        :param token
        :param callback
        """
        qs = 'oauth_token=%s' % token
        if callback:
            qs = '%s&oauth_callback=%s' % (qs, urllib.urlencode(callback))
        return '%s?%s' % (self.authorize_url, qs)

    def get_request_token(self, callback=None):
        """
        Get a linkedin request token. Return the tokens as a dict, also append
        the authorization url, cause you likely want it.
        :param callback
        """
        response = self.client.get(self.request_token_url)

        self.request_token = parse_qs(response.content)
        # update variables
        self.oauth_token = self.request_token['oauth_token'][0]
        self.oauth_token_secret = self.request_token['oauth_token_secret'][0]
        # inject authorization url into request token dict
        self.request_token['url'] = self.get_authorization_url(
                    self.request_token['oauth_token'][0], callback=callback)
        # update authenticated client
        self.client = self._get_authorized_client(self.linkedin_key, self.linkedin_secret,
                    oauth_token=self.oauth_token, oauth_token_secret=self.oauth_token_secret)

        return self.request_token

    def get_access_token(self, verifier):
        """
        Given a Verifier, get the linkedin access tokens
        """
        response = self.client.post(self.access_token_url,
                data={'oauth_verifier': verifier})

        access_token = parse_qs(response.content)
        # update token variables
        self.oauth_token = access_token['oauth_token'][0]
        self.oauth_token_secret = access_token['oauth_token_secret'][0]
        # update authenticated client
        self.client = self._get_authorized_client(self.linkedin_key, self.linkedin_secret,
                oauth_token=self.oauth_token, oauth_token_secret=self.oauth_token_secret)

        return access_token
