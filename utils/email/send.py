# Before use this utility you MUST allow less secure apps
# In your gmail account https://myaccount.google.com/u/4/lesssecureapps
# Change email_sender and email_password in settings.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import settings


def send_email(email, text):
    """Send email to users
    :param email: email recipient
    :param text: email text
    :return: True or False
    """

    sender = settings.get('email_sender')
    recipient = email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Subject'

    msg.attach(MIMEText(text, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, settings.get('email_password'))
    text = msg.as_string()
    response = server.sendmail(sender, recipient, text)

    if not response:
        return True
    return False
