import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("username of gmail", "password of gmail")

server.sendmail("from","to", "message")

print("Sent mail")