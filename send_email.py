import tkinter as tk
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import hashlib

# Function to send email
def send_email(from_user, to_user, subject, body, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

# The following code cause git conflict
#     # Attach the email body to the message
#     message.attach(email_body)

#     # Connect to the SMTP server using SMTP_SSL
#     with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
#         server.set_debuglevel(1)  # Enable debug output
#         # Login to the SMTP server if authentication is required
#         server.login(smtp_username, smtp_password)
        
#         # Send the email
#         server.sendmail(sender_email, receiver_email, message.as_string())
#         print("Email sent successfully!")

# # Set up email parameters
# sender_email = 'a70904597@gmail.com'
# receiver_email = 'p36494089@gmail.com'
# subject = 'Test Email'
# body = 'This is a test email sent from Python.'
# smtp_server = 'smtp.gmail.com'
# smtp_port = 465  # Use 465 for SSL/TLS
# smtp_username = 'a70904597@gmail.com'
# smtp_password = '@you-91YA'

# # Send the email
# send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        text = msg.as_string()
        server.sendmail(from_user, to_user, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
