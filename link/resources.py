BASE_API = 'api.linkedin.com'


ENDPOINTS = {
        'profile': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/%(named_params)s%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/profile-api'
        },
         'connections': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/%(named_params)s/connections%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/connections-api ',
        },
        'people_search': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people-search',
            '__doc__': 'see https://developer.linkedin.com/documents/people-search-api',
        },
        'company_search': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/company-search%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/company-search'
        },
        'company_follow_list': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/%(named_params)s/following/companies',
            '__doc__': 'see https://developer.linkedin.com/documents/company-follow-and-suggestions',
        },
        'company_follow': {
            'method': 'POST',
            'url': 'https://api.linkedin.com/v1/people/~/following/companies',
            '__doc__': 'see https://developer.linkedin.com/documents/company-follow-and-suggestions',
        },
        'company_unfollow': {
            'method': 'DELETE',
            'url': 'http://api.linkedin.com/v1/people/~/following/companies/%(named_params)s',
            '__doc__': 'see https://developer.linkedin.com/documents/company-follow-and-suggestions',
        },
        'company_follow_suggestions': {
            'method': 'GET',
            'url': 'http://api.linkedin.com/v1/people/~/suggestions/to-follow/companies',
            '__doc__': 'see https://developer.linkedin.com/documents/company-follow-and-suggestions',
        },


}
