#Link - A Linkedin API Wrapper that doesn't suck

![link](http://mikegrouchy.com/link/images/link.png)

#Magnets, how do they work?!

Testing this from your interpreter is pretty easy

```python
    from link import Link
    l = Link(linkedin_key='yourkeygoeshere', linkedin_secret='yoursecretgoeshere')
    # get your request token and authorization url
    request_token = l.get_request_token()

    # now open up request_token['url'] in your browser and authorize your app
    # you will be given a verifier with which you can get your access token
    access_token = l.get_access_token(yourverfiergoeshere')

    #now you can make a request for your profile info
    l.get_profile()

    #or maybe you want to get specific fields from your profile
    l.get_profile(field_selectors=('id', 'first-name', 'last-name', 'company'))

```

Author: Mike Grouchy ([@mgrouchy](http://twitter.com/mgrouchy))
