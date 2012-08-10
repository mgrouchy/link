#Link - Your Master Sword for dealing with the LinkedIn API

![link](https://github.com/mgrouchy/link/raw/master/link.png)
#Install

You can install with setup.py

```shell
git clone git://github.com/mgrouchy/link.git
cd link
python setup.py install
```

or you can install with pip
```shell
pip install link-py
```

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
l.profile()

#or maybe you want to get specific fields from your profile
l.profile(field_selectors=('id', 'first-name', 'last-name', 'company'))

```

#Bugs?
See a bug and want me to fix it? Create an issue and your wish, is my command(sort of).


#Want to Contribute?
Fork this repo, submit a pull request with your changes and an updated Authors.md with your name.

Thats it!

Author: Mike Grouchy ([@mgrouchy](http://twitter.com/mgrouchy))
