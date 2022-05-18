from email import message
from multiprocessing import context
import smtplib
import ssl
import datetime as dt
import time

from django.dispatch import receiver.

sender_email = "downbread2911@gmail.com"
receiver_email = "tanphamminh2002@gmail.com"
password = "Homework2911"
port = 587
smtp_server = "smtp.gmail.com"
message = """/
Subject: Trail mail via Python
Hello! Welcome to my channel UrGOD."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as email:

    email.starttls(context=context)

    email.login(sender_email, password)
    send_time = dt.datetime(2022, 5, 17, 12, 35, 0)
    print(send_time.timestamp())
    print(time.time())
    x = time.sleep(send_time.timestamp()-time.time())
    print(x)
    email.sendmail(sender_email, receiver_email, message)

    print('email sent')
