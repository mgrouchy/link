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
        params:
            linkedin_key:
            linkedin_secret:
            oauth_token:
            oauth_token_secret:
    """
    def __init__(self, linkedin_key=None, linkedin_secret=None,
                     oauth_token=None, oauth_token_secret=None):

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

        self.oauth_token = oauth_token or None
        self.oauth_token_secret = oauth_token_secret or None

        if self.oauth_token and self.oauth_token_secret:
            oauth_hook = OAuthHook(oauth_token=self.oauth_token,
                                   oauth_token_secret=self.oauth_token_secret)
        else:
            oauth_hook = OAuthHook()

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
        params:
            endpoint:
            method:
            data:
            field_selectors:
        """
        method = method.lower()
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

        response = _client(endpoint, data=data)

        content_dict = simplejson.loads(response.content)
        return content_dict

    def get_auth_url(self, token, callback=None):
        """
        Get an Authorization url developers can put in their app to get user to
        authorize a linkedin connection
        """
        params = {'oauth_token': token}
        if callback:
            params['oauth_callback'] = callback

        return '%s?%s' % (self.authorize_url, urllib.urlencode(params)

    def get_request_token(self, callback=None):
        """
        Get a linkedin request token. Return the tokens as a dict, also append
        the authorization url, cause you likely want it.
        """
        response = self.client.get(self.request_token_url)

        self.request_token = parse_qs(response.content)
        self.request_token['url'] = self.get_auth_url(request_token['oauth_token'], callback=callback)
        return self.request_token

    def get_access_token(self, verifier):
        """
        Given a Verifier, get the linkedin access tokens
        """
        response = self.client.post(self.access_token_url,
                data={'oauth_verifier': verifier, 'oauth_token': self.oauth_token})

        access_token = parse_qs(response.content)
        self.oauth_token = access_token['oauth_token']
        self.oauth_token_secret = access_token['oauth_token_secret']
        return access_token


