#import boto3	#Used for AWS... Not sure if required.
import MySQLdb 	#Need for connection to SQL db
import random	#Need for random id generation
import string	#Need for random id generation
import datetime
import time
import csv #Required to import table data int CSV

#Required to send email with an attachment
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


conn = MySQLdb.connect(host="harrisfaceapi.ckuvqwkjly5s.ap-southeast-2.rds.amazonaws.com", port=3306, user="harris", passwd="988$_iADO_k9484ASDJFSDJ_afdsj", db="harris_face_dev")
cur = conn.cursor() #Create a cursor for the select
print("You have just connected to the database! You are a true legend!")

cur.execute("SELECT * FROM api_customer")
results = cur.fetchall()
with open("api_customer_query.csv", "wb") as csv_file: #Python 2 version
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cur.description]) #Write headers
    csv_writer.writerows(cur)

    print('Query has been exported')

# Create a table for print function
widths = []
columns = []
tavnit = '|'
separator = '+'

for cd in cur.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

# Print the results of the SQL Table in a table format
print(separator)
print(tavnit % tuple(columns))
print(separator)

for row in results:
	print(tavnit % row)
print(separator)

# Display all the names of people we know and exclude face_ids missing both first name or last name.
print("Here is a list of people whose face we have stored in Harris 360.")

cursor = conn.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT face_id, first_name, last_name FROM api_customer WHERE first_name IS NOT NULL AND first_name !='' AND last_name IS NOT NULL AND last_name !='' ")
result_set = cursor.fetchall()
for row in result_set:
    print "%s, %s, %s" % (row["face_id"], row["first_name"], row["last_name"])

############################ WORK IN PROGRESS #############################

# Add new entry to database

'''def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	value = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
	cur.execute("INSERT INTO api_customer (id, created, first_name, last_name) VALUES (%s, %s, %s)", (id, date, value))
	conn.commit()'''

#dynamic_data_entry()

#new_entry = {'id': id, 'created': date, 'first_name': %s, 'last_name': %s}

'''cur.execute("CREATE UNIQUE INDEX face_id ON api_customer (face_id ASC)")
conn.commit()

for row in api_customer:
	print "%s, %s, %s" % (row["face_id"])

try:
	cur.execute("INSERT INTO api_customer (id, created, face_id, customer_ref, face_sharpness, face_brightness, first_name, last_name, surname, company_id, loyal)")
	conn.commit()
except:
	conn.rollback()'''

############################ WORK IN PROGRESS #############################

# SENDING AN EMAIL WITH ATTACHED QUERY CSV FILE
email_user = 'emmanuel@nelaapp.com' # Gmail Login
email_password = 'emanfaz1'			# Gmail Password
email_send = 'emanfazio@gmail.com'	# Email of recipient

subject = 'Daily query results'		# Email Subject

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'This email has been sent from Python!' # Messgae with the email
msg.attach(MIMEText(body,'plain'))

filename ='api_customer_query.csv'	# Attaching file in same folder as script
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.quit()

print('Email has been sent')

cur.close()
conn.close()