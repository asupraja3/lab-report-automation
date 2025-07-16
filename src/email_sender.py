import smtplib
from email.message import EmailMessage

def send_email_report(subject, body, to_email, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "youremail@example.com"
    msg['To'] = to_email
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='lab_report.pdf')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("youremail@example.com", "your_app_password")  # Use app password
        smtp.send_message(msg)
