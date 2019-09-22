# Before use this utility you MUST allow less secure apps
# In your gmail account https://myaccount.google.com/u/4/lesssecureapps

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import settings

# send email
def send_email(email, token):
    """Send email function(SMTP)
    :param email: email recipient
    :param token: token for verify user
    :return: True or False
    """
    sender = settings.get('email_sender')
    recipient = email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Subject'
    body = '''Click to below link to verify your email
           <br />http://localhost:8888/register/checkmail
           ?email={0}&token={1}'''.format(recipient, token)

    msg.attach(MIMEText(body, 'html'))

    # establish smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # start tls
    server.starttls()
    # login
    server.login(sender, settings.get('email_password'))
    # message
    text = msg.as_string()
    # send mail
    response = server.sendmail(sender, recipient, text)

    if not response:
        return True
    return False
