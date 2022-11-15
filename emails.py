#!/usr/bin/env python3

import email.message
import mimetypes
from os import listdir
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    # creates an email with an attachment
    
    # email format
    msg = email.message.EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)
    
    # add the attachment to the email
    attached_filename = os.listdir(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    
    with open(attachment_path, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype = mime_type,
                           subtype = mime_subtype,
                           filename = attached_filename)
    
    return msg

def send_email(msg):
    """sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(msg)
    mail_server.quit()