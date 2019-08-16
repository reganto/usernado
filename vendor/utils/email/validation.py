import requests
from vendor.keys.secret import NEVERBOUNCE_KEY

# email validation
def email_validation(email):
    """ validation received email
    :param email: received email
    :return: True or Flase
    """
    
    email_validation_url = '''https://api.neverbounce.com/v4/
    single/check?key={0}&email={1}'''.format(NEVERBOUNCE_KEY, email)
    email_response = requests.post(email_validation_url)
    email_response = email_response.json()
    if email_response['result'] == 'valid':
        return True
    return False
