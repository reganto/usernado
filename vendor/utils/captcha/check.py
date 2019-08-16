import requests
from vendor.keys.secret import CAPTCHA_SECRET_KEY

# check captcha
def check_captcha(g_recaptcha_response, remote_ip):
    """ check recaptcha function
    :parama g_recaptcha_response: response from recaptcha
    (self.get_argument('g_recaptcha_response'))
    :param remote_ip: remote ip(request.remote_ip)
    :return: True or Flase
    """

    query_string = '''?secret={0}&response={1}&remoteip={2}
    '''.format(CAPTCHA_SECRET_KEY, g_recaptcha_response, remote_ip)
    api_call = "https://www.google.com/recaptcha/api/siteverify" + query_string
    api_response = requests.post(api_call)
    api_response = api_response.json()
    if api_response["success"]:
        return True
    return False
