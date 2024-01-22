import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email(receiver_email, html_content, subject):
    # Email configuration
    sender_email = 'pblock.help@gmail.com'
    sender_password = 'tytytwhzzomhkrdp'

    # Create a message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach HTML content to the email
    msg.attach(MIMEText(html_content, 'html'))

    # Establish a connection with the SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server and port
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login credentials

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print("HTML Email sent successfully!")
    except Exception as e:
        print(f"Error sending HTML email: {str(e)}")
    finally:
        # Close the SMTP server connection
        server.quit() if 'server' in locals() else None