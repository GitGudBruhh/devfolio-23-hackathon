# -*- coding: utf-8 -*-
"""30_days.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CoDsVfKP9jLun9E5wLcgq_dZGP4NnlvA
"""

import numpy as np
import pandas as pd
from getpass import getpass
import imaplib
import email
from email.header import decode_header
import time
from datetime import date, timedelta
import re

class Emails:
    def __init__(self, email_address, password):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.email_address = email_address
        response_code, response_message = self.imap.login(email_address, password)

        if response_code == "OK":
            print("Login successful")
        else:
            print("Login failed:", response_message)

    def mail_box(self, mailbox_name):
        self.mailbox = mailbox_name
        status, message_data = self.imap.select(mailbox_name)

        if status == "OK":
            print(f"Mailbox {mailbox_name} selected successfully")
            # print(f"Total message in {mailbox_name}: {message_data[0].decode()}")
        else:
            print(f"Mailbox selection failed. Status: {status}")

    def fetch(self):
        ref_date = date.today() - timedelta(days=30)
        months = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
                  'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        data = {"date":[], "sender": [], "subject": []}

        status, email_ids = self.imap.search(None, "ALL")
        email_ids = email_ids[0].split()
        count = 0

        for i in range(len(email_ids)):
            status, email_data = self.imap.fetch(email_ids[-i], "(RFC822)")

            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            subject = email_message["subject"]
            sender = email_message["from"]
            date_data = email_message["date"]

            date_lst = date_data[5:16].split()
            if date_lst[0][0] == '0':
                date_lst[0] = date_lst[0][1]


            if date(int(date_lst[2]), months[date_lst[1]], int(date_lst[0])) < ref_date:
                count += 1
                # print(count)
                if count > 10:
                    break
                continue
            if sender.find('<') != -1:
                sender = sender[:sender.find('<')]
            # print(date_lst)

            data["date"].append(date(int(date_lst[2]), months[date_lst[1]], int(date_lst[0])))
            data["sender"].append(sender)
            data["subject"].append(subject)

        return pd.DataFrame(data)

email_id = getpass("Enter your email_id: ")
password = getpass("Enter your emai_id password: ")
server_conn = Emails(email_id, password)

server_conn.mail_box("INBOX")
df = server_conn.fetch()

word = "Seminar"
df[df.subject.str.contains(fr'\b{re.escape(word)}\b', case=False)]

df.to_csv("final_dataset.csv", index=False)