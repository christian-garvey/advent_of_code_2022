import requests
#from requests.auth import HTTPBasicAuth

def get_input(day):
    cookie = '53616c7465645f5f3b717be0084c6cfb3725bd526f7d725e6be68923380bde5e9ec73b083883e380629c6ee60b0bb18f84a5122817cd0ba970c223ff8e08952b'
    url_str = "https://adventofcode.com/2022/day/%s/input" % (day)
    cookies = dict(session=cookie)
    f= requests.get(url_str, cookies=cookies)
    fo = f.text.splitlines()
    return fo

# print(get_input(4))

### SSL CERTIFCATE ERROR ###
## RUN THIS LINE: pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip_system_certs
## [https://arup.sharepoint.com/sites/network-software-development/SitePages/SSL-Certificates.aspx]