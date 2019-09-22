import requests
from settings import settings


def email_validation(this_email):
    """ validation received email
    :param email: received email
    :return: True or Flase
    """

    key = settings.get('neverbounce_key')
    payload = 'https://api.neverbounce.com/v4/single/check?key={0}&email={1}' \
        .format(key, this_email)
    response = requests.post(payload)
    response = response.json()
    result = response.get('result')
    if result == 'valid':
        return True
    return False
