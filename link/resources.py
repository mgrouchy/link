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
        'companies': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/companies/%(resource_id)s%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/company-lookup-api-and-fields'
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
        'company_products': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/companies/%(resource_id)s/products/%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/company-products-and-recommendations'
        },
        'jobs': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/jobs/%(resource_id)s%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/job-lookup-api-and-fields'
        },
        'jobs_search': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/jobs-search%(field_selectors)s',
            '__doc__': 'see https://developer.linkedin.com/documents/job-search-api'
        },
        'job_bookmarks': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/~/job-bookmarks',
            '__doc__': 'see https://developer.linkedin.com/documents/job-bookmarks-and-suggestions'
        },
        'add_job_bookmark': {
            'method': 'POST',
            'url': 'https://api.linkedin.com/v1/people/~/job-bookmarks',
            '__doc__': 'see https://developer.linkedin.com/documents/job-bookmarks-and-suggestions'
        },
        'delete_job_bookmark': {
            'method': 'DELETE',
            'url': 'https://api.linkedin.com/v1/people/~/job-bookmarks/%(resource_id)s',
            '__doc__': 'see https://developer.linkedin.com/documents/job-bookmarks-and-suggestions'
        },
        'job_bookmark_suggestions': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/~/job-suggestions:(jobs)',
            '__doc__': 'see https://developer.linkedin.com/documents/job-bookmarks-and-suggestions'
        },
        'message': {
            'method': 'POST',
            'url': 'https://api.linkedin.com/v1/people/~/mailbox',
            '__doc__': 'see https://developer.linkedin.com/documents/messaging-between-connections-api and\
                    https://developer.linkedin.com/documents/invitation-api'
        },
        'network_updates': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/%(named_params)s/network/updates',
            '__doc__': 'see https://developer.linkedin.com/documents/get-network-updates-and-statistics-api'
        },
        'network_stats': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/~/network/network-stats',
            '__doc__': 'see https://developer.linkedin.com/documents/get-network-updates-and-statistics-api'
        },
        'post_network_update': {
            'method': 'POST',
            'url': 'https://api.linkedin.com/v1/people/~/person-activities',
            '__doc__': 'see https://developer.linkedin.com/documents/get-network-updates-and-statistics-api'
        },
        'share': {
            'method': 'POST',
            'url': 'https://api.linkedin.com/v1/people/~/shares',
            '__doc__': 'see https://developer.linkedin.com/documents/share-api'
        },
        'current_share': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/~:(current-share)',
            '__doc__': 'see https://developer.linkedin.com/documents/share-api'
        },
        'network_shares': {
            'method': 'GET',
            'url': 'https://api.linkedin.com/v1/people/~/network',
            '__doc__': 'see https://developer.linkedin.com/documents/share-api'
        },
        'get_update_comments': {
            'method': 'GET',
            'url': 'http://api.linkedin.com/v1/people/~/network/updates/%(named_params)s/update-comments',
            '__doc__': 'see https://developer.linkedin.com/documents/commenting-reading-comments-and-likes-network-updates'
        },
        'get_update_likes': {
            'method': 'GET',
            'url': 'http://api.linkedin.com/v1/people/~/network/updates/%(named_params)s/likes',
            '__doc__': 'see https://developer.linkedin.com/documents/commenting-reading-comments-and-likes-network-updates'
        },
        'add_comment': {
            'method': 'POST',
            'url': 'http://api.linkedin.com/v1/people/~/network/updates/%(named_params)s/update-comments',
            '__doc__': 'see https://developer.linkedin.com/documents/commenting-reading-comments-and-likes-network-updates'
        },
        'add_like': {
            'method': 'PUT',
            'url': 'http://api.linkedin.com/v1/people/~/network/updates/%(named_params)s/is-liked',
            '__doc__': 'see https://developer.linkedin.com/documents/commenting-reading-comments-and-likes-network-updates'
        },

}
