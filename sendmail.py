import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

fromaddr = 'emmanuel@nelaapp.com'
frompass = 'PASSWORD'

toaddr = 'emanfazio@gmail.com'

msg = 'Hello, this is an email sent from Python!'


server.login(fromaddr, frompass)
server.sendmail(fromaddr, toaddr, msg)

print('Email has been successfully sent')

server.quit()