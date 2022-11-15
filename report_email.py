#!/usr/bin/env python3

import reports
import emails
import os
from datetime import date

# set text dir and file location
txt_dir = "supplier-data/descriptions/"
attachment = "/tmp/processed.pdf"

# define varaible report as a list
summary = ""

# define date format for today as report title
dt = datetime.today().strftime("%B %d, %Y")
title = "Processed Update on " + dt

# loop for a summary string
for txt_file in os.listdir(txt_dir):
    with open(txt_file, "r") as f:
        lines = f.read().strip().splitlines()
        name = "name: {}".format(lines[0])
        weight = "weight: {}".format(lines[1])
    summary +="{}<br/>{}<br/><br/>".format(name, weight)
    
if __name == "__main__":
    """send email"""
    subject = "Upload Complete - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "<student>@example.com"
    body = "All fruits are uploaded to our website successfully. \
        A detial list is attached to thsi emial."
    msg = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(msg)

