BASE_API = 'api.linkedin.com'


ENDPOINTS = {
        'profile': {
            'method': 'GET',
            'url': '%s/v1/people/' % BASE_API,
        },
        'connections': {
            'method': 'GET',
            'url': '%s/v1/people/%s/connections' % BASE_API,
        }

}
