from creds import email
import smtplib, ssl

email_username = email.username
email_password = email.password

smpt_address = "smtp.gmail.com"
smpt_port = 465

message = "This is a test message being sent"
subject = "Test message send from PY"

to_send = ssl.create_default_context()

message_to_send = "Subject: {subject} \n\n {message}".format(
    subject = subject,
    message = message,
)

with smtplib.SMTP_SSL(smpt_address, smpt_port, context=to_send) as e:
    e.login(email_username, email_password)
    e.sendmail("Test",email_username,message_to_send)