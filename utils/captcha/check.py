# Get a secret code and data-sitekey from https://www.google.com/recaptcha/intro/v3.html
# Add secret code to settings.py
# Add below lines to your html:
# <script src='https://www.google.com/recaptcha/api.js'></script>
# <div class="g-recaptcha" data-sitekey="YOUR DATA-SITEKEY"></div>

import requests
from settings import settings


def check_captcha(g_recaptcha_response, remote_ip):
    """ check google recaptcha 
    :parama g_recaptcha_response: response from recaptcha
    (self.get_argument('g-recaptcha-response'))
    :param remote_ip: remote ip(request.remote_ip)
    :return: True or Flase
    """

    query_string = '?secret={0}&response={1}&remoteip={2}'.format(
        settings.get('captcha_secret_key'),
        g_recaptcha_response,
        remote_ip
    )
    api_call = "https://www.google.com/recaptcha/api/siteverify" + query_string
    api_response = requests.post(api_call)
    api_response = api_response.json()
    if api_response["success"]:
        return True
    return False
