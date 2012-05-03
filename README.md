#Link - A Linkedin API Wrapper that doesn't suck

![link](https://a248.e.akamai.net/camo.github.com/d3e948a500a39390a2f47415016ef06a9fb6aca4/687474703a2f2f6d696b6567726f756368792e636f6d2f6c696e6b2f696d616765732f6c696e6b2e706e67)

#Magnets, how do they work?!

Testing this from your interpreter is pretty easy

```python
from link import Link
l = Link(linkedin_key='yourkeygoeshere', linkedin_secret='yoursecretgoeshere')
# get your request token and authorization url
request_token = l.get_request_token()

# now open up request_token['url'] in your browser and authorize your app
# you will be given a verifier with which you can get your access token
access_token = l.get_access_token(yourverfiergoeshere)

#now you can make a request for your profile info
l.get_profile()

#or maybe you want to get specific fields from your profile
l.get_profile(field_selectors=('id', 'first-name', 'last-name', 'company'))

```

#Want to Contribute?
Fork this repo, submit a pull request with your changes and an updated Authors.md with your name.

Thats it!

Author: Mike Grouchy ([@mgrouchy](http://twitter.com/mgrouchy))
