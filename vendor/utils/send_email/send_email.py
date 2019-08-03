import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# send email
def send_email(email, token):
    """Send email function(SMTP)"""
    sender = 'Sender'
    recipient = email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Subject'
        
    body = 'Click to below link to verify your email' + \
           '<br />http://localhost:8888/register/checkmail?email={0}&token={1}'.format(recipient, token)

    msg.attach(MIMEText(body, 'html'))

    # establish smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # start tls
    server.starttls()
    # login
    server.login(sender, 'password')
    # message
    text = msg.as_string()
    # send mail
    response = server.sendmail(sender, recipient, text)

    if not response:
        return True
    else:
        return False
