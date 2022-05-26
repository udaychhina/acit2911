import smtplib
from email.message import EmailMessage
import datetime as dt
import time
from apscheduler.schedulers.background import BackgroundScheduler


def email_send(*args):

    subject = args[0]
    body = args[1]
    to = args[2]
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "downbread2911@gmail.com"
    msg['from'] = user
    password = "Homework2911"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    server.send_message(msg)

    server.quit()


def schedule(course, desc, email_address, y, m, d):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=email_send,
                      trigger='cron',
                      year=y, month=m, day=d, hour=10, minute=10,  second=10, args=(course, desc, email_address))
    scheduler.start()
