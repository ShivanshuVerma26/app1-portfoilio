import smtplib, ssl


host = "smtp.gmail.com"
port = 465


def send_email(message):
    username = "er.shivanshu26@gmail.com"
    password = "fbav vlsi tayg yphm"

    context = ssl.create_default_context()

    receiver = "er.shivanshu26@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server(username, receiver, message)

