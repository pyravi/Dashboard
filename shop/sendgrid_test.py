import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='testing@mail.com',
    to_emails='to@testing.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)