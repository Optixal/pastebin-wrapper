#!/usr/bin/python3

# Light Pastebin Wrapper
# By Optixal

# Pastebin Documentation: https://pastebin.com/api

import requests, os

# Precedence of Confidential Information:
# Environment Variable > Function Argument > Constant Defined Here
# Recommended: Set confidential information as environment variables with "export PASTEBIN_DEV_KEY=abc123". You can store the "export" commands within a file named "keys" as well and run "source keys".
PASTEBIN_DEV_KEY = ''
PASTEBIN_USER_NAME = ''
PASTEBIN_USER_PASSWORD = ''

# Pastes code/text anonymously to Pastebin
# Returns: paste_url, the URL containing the paste
def paste(paste_code, dev_key=PASTEBIN_DEV_KEY, user_key='', option='paste', paste_private=0, paste_name='', paste_expire_date='N', paste_format='text'):

    data = {
            'api_dev_key'           : os.getenv('PASTEBIN_DEV_KEY', dev_key),
            'api_user_key'          : user_key,
            'api_option'            : option,
            'api_paste_private'     : str(paste_private),
            'api_paste_name'        : paste_name,
            'api_paste_expire_date' : paste_expire_date,
            'api_paste_format'      : paste_format,
            'api_paste_code'        : paste_code,
            }

    url = 'https://pastebin.com/api/api_post.php'
    r = requests.post(url, data=data)
    if r.status_code == 200 and 'Bad' not in r.text: return r.text
    else: raise PasteError(r.text)

class PasteError(Exception):
    def __init__(self, response):
        self.response = response
    def __str__(self):
        return repr(self.response)

# Authenticate with Pastebin with username and password
# Returns: user_key, a session key used when pasting a non-guest paste
def login(dev_key=PASTEBIN_DEV_KEY, user_name=PASTEBIN_USER_NAME, user_password=PASTEBIN_USER_PASSWORD):

    data = {
        'api_dev_key'       : os.getenv('PASTEBIN_DEV_KEY', dev_key),
        'api_user_name'     : os.getenv('PASTEBIN_USER_NAME', user_name),
        'api_user_password' : os.getenv('PASTEBIN_USER_PASSWORD', user_password),
    }

    url = 'https://pastebin.com/api/api_login.php'
    r = requests.post(url, data=data)
    if r.status_code == 200 and 'Bad' not in r.text: return r.text
    else: raise LoginError(r.text)

class LoginError(Exception):
    def __init__(self, response):
        self.response = response
    def __str__(self):
        return repr(self.response)
