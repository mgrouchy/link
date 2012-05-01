import requests
from urlparse import parse_qs
from oauth_hook import OAuthHook


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

        self.oauth_token = oauth_token or None
        self.oauth_token_secret = oauth_token_secret or None

        hook_kwargs = {
                        'consumer_key': self.linkedin_key,
                        'consumer_secret': self.linkedin_secret,
                        'oauth_token': self.oauth_token,
                        'oauth_token_secret': self.oauth_token_secret
                      }

        self.client = requests.session(hooks={'pre_request': OAuthHook(**hook_kwargs)})
        self.request_token = None

    def __getattr__(self, *args, **kwargs):
        """docstring for __getattr__"""
        pass

    def request(self, method, *args, **kwargs):
        pass

    def get_auth_url(self):
        """
        Get an Authorization url developers can put in their app to get user to
        authorize a linkedin connection
        """
        pass

    def get_request_token(self):
        """
        Get a linkedin request token. Return the tokens as a dict
        """
        response = self.client.get(self.request_token_url)
        self.request_token = parse_qs(response.content)
        self.request_token['url'] = self.get_auth_url()
        return self.request_token

    def get_access_token(self, verifier):
        """
        Given a Verifier, get the linkedin access tokens
        """
        response = self.client.post(self.access_token_url,
                {'oauth_verifier': verifier, 'oauth_token': self.oauth_token})

        access_token = parse_qs(response.content)
        self.oauth_token = access_token['oauth_token']
        self.oauth_token_secret = access_token['oauth_token_secret']
        return access_token


