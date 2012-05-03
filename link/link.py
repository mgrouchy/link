import urllib
import requests
from urlparse import parse_qs
from oauth_hook import OAuthHook
from resources import ENDPOINTS
from functools import partial

import simplejson


class LinkError(Exception):
    pass


class Link(object):
    """
    Link is the main interface for the linkedin Api
    """
    def __init__(self, linkedin_key=None, linkedin_secret=None,
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

        OAuthHook.consumer_key = self.linkedin_key
        OAuthHook.consumer_secret = self.linkedin_secret

        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret

        oauth_hook = OAuthHook(access_token=self.oauth_token,
                               access_token_secret=self.oauth_token_secret)

        self.client = requests.session(hooks={'pre_request': oauth_hook})
        self.request_token = None

    def __getattr__(self, name):
        """
        Implement getattr to map Linkedin Endpoints from the endpoints dict
        to a partial of request.
        """
        try:
            endpoint = ENDPOINTS[name]
            return partial(self.request, endpoint['url'], method=endpoint['method'])
        except KeyError:
            raise AttributeError

    def request(self, endpoint, method='GET', data=None, field_selectors=None):
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

        # compose our arguments
        if method == 'get':
            if not data:
                query_str = '~'
            else:
                query_str = urllib.urlencode(data)

            endpoint = endpoint % query_str

        # get a client
        _client = getattr(self.client, method)
        if not _client:
            raise LinkError

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

        self.request_token['url'] = self.get_authorization_url(
                    self.request_token['oauth_token'][0], callback=callback)
        return self.request_token

    def get_access_token(self, verifier):
        """
        Given a Verifier, get the linkedin access tokens
        """
        response = self.client.post(self.access_token_url,
                data={'oauth_verifier': verifier})

        access_token = parse_qs(response.content)
        print access_token

        self.oauth_token = access_token['oauth_token']
        self.oauth_token_secret = access_token['oauth_token_secret']
        return access_token
