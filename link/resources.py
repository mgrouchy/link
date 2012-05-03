BASE_API = 'api.linkedin.com'


ENDPOINTS = {
        'profile': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/%(named_params)s%(field_selectors)s',
        },
        # 'connections': {
        #    'method': 'GET',
        #    'url': '%s/v1/people/%s/connections' % BASE_API,
        #}

}
