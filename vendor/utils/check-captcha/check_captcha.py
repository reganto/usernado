# Python

import requests


# check captcha
def check_captcha(g_recaptcha_response, remote_ip):
    secret_key = 'YOUR SECRET KEY'
    query_string = '?secret={0}&response={1}&remoteip={2}'.format(secret_key, g_recaptcha_response, remote_ip)
    api_call = "https://www.google.com/recaptcha/api/siteverify" + query_string
    api_response = requests.post(api_call)
    api_response = api_response.json()
    if api_response["success"]:
        return True
    else:
        return False

