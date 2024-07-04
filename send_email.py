import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "er.shivanshu26@gmail.com"
password = "fbav vlsi tayg yphm"

receiver = "er.shivanshu26@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: My new email from app
Hi How are you!
Hope you are doing fine.
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
