#import boto3	#Used for AWS... Not sure if required.
import MySQLdb 	#Need for connection to SQL db
import random	#Need for random id generation
import string	#Need for random id generation
import datetime
import time
import smtplib

conn = MySQLdb.connect(host="harrisfaceapi.ckuvqwkjly5s.ap-southeast-2.rds.amazonaws.com", port=3306, user="harris", passwd="988$_iADO_k9484ASDJFSDJ_afdsj", db="harris_face_dev")
cur = conn.cursor() #Create a cursor for the select
print("You have just connected to the database! You are a true legend!")

cur.execute("SELECT * FROM api_customer")
results = cur.fetchall()

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

cur.execute("CREATE UNIQUE INDEX face_id ON api_customer (face_id ASC)")
conn.commit()

for row in api_customer:
	print "%s, %s, %s" % (row["face_id"])

try:
	cur.execute("INSERT INTO api_customer (id, created, face_id, customer_ref, face_sharpness, face_brightness, first_name, last_name, surname, company_id, loyal)")
	conn.commit()
except:
	conn.rollback()

############################ WORK IN PROGRESS #############################
# SENDING AN EMAIL
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

cur.close()
conn.close()