import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465


def sendemail(message):
    username = "er.shivanshu26@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "er.shivanshu26@gmail.com"
    context = ssl.create_default_context()

    message = message

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
