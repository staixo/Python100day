import smtplib
import glob
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

folder_path = "./output/"  # Replace with the path to your folder containing CSS files

css_files = glob.glob(f"{folder_path}/*.css")  # Get a list of all CSS files in the folder
email= []
for file_path in css_files:
    with open(file_path,"r") as f:
        email.append(f.read())

connection = smtplib.SMTP("smtp.gmail.com", port=587)


# Email configuration
sender_email = "@gmail.com"  # Replace with your email address
receiver_email = "@example.com"  # Replace with recipient's email address
subject = ""
message = ""

# SMTP server configuration
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server address
smtp_port = 587  # Replace with the appropriate port number
username = "your_username"  # Replace with your SMTP server username
password = "your_password"  # Replace with your SMTP server password

# Create a multipart message object
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the message body to the email
msg.attach(MIMEText(message, "plain"))

# Create an SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Enable TLS encryption
    server.login(username, password)  # Login to the SMTP server
    server.send_message(msg)  # Send the email

print("Email sent successfully!")
