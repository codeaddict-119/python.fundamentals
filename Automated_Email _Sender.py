import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail credentials
sender_email = "your_email@gmail.com"
app_password = "your_app_password"

# List of recipients
recipients = [
    "recipient1@example.com",
    "recipient2@example.com",
    "recipient3@example.com"
]

# Email subject and body
subject = "Automated Email from Python"
body = """
Hello,

This is a test email sent automatically using a Python script.

Best regards,
Python Email Bot
"""

# Create email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)

    # Send email to each recipient
    for recipient in recipients:
        msg["To"] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    # Close server connection
    server.quit()
    print("All emails sent successfully!")

except Exception as e:
    print("Error sending email:", e)
