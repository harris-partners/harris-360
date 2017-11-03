import smtplib
import MINEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

fromaddr = 'emmanuel@nelaapp.com'
frompass = 'PASSWORD'
toaddr = 'emanfazio@gmail.com'

msg = 'Subject: {}\n\n{}'.format('Daily query results', 'Hello, this is an email sent from Python!') #'Hello, this is an email sent from Python!'
msg.attach(MINEText(b))

server.login(fromaddr, frompass)
server.sendmail(fromaddr, toaddr, msg)

print('Email has been successfully sent')

server.quit()