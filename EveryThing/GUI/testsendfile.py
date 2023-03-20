import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Create a multipart message
    message = MIMEMultipart()
    message['63011212069@msu.ac.th'] = sender_email
    message['63011212098@msu.ac.th'] = receiver_email
    message['Subject'] = subject
 

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Open the file in bynary
    with open(attachment_path, 'rb') as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEApplication(attachment.read(), Name='name.pdf')
        part['Content-Disposition'] = 'attachment; filename="name.pdf"'
        message.attach(part)

    # Log in to server using secure context and send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

# Example usage
sender_email = '63011212069@msu.ac.th'
sender_password = 'Tk!130613'
receiver_email = '63011212069@msu.ac.th'
subject = 'PDF Report'
body = 'สวัสดีจ้า'
attachment_path = 'name.pdf'

send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
