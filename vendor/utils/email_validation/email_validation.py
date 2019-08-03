#Python

import requests


# email validation
def email_validation(this_email):
    secret_key = 'YOUR SECRET KEY'
    email_validation_url = 'https://api.neverbounce.com/v4/single/check?key={0}&email={1}'.format(secret_key, this_email)
    email_response = requests.post(email_validation_url)
    email_response = email_response.json()
    if email_response['result'] == 'valid':
        return True
    else:
        return False

