import boto3	#Used for AWS... Not sure if required.
import MySQLdb 	#Need for connection to SQL db
import random	#Need for random id generation
import string	#Need for random id generation

conn = MySQLdb.connect(host="harrisfaceapi.ckuvqwkjly5s.ap-southeast-2.rds.amazonaws.com", port=3306, user="harris", passwd="988$_iADO_k9484ASDJFSDJ_afdsj", db="harris_face_dev")
cur = conn.cursor() #Create a cursor for the select
print("You have just connected to the database! You are a true legend!")

#Step 1: Does the face exist?
cur.execute("SELECT face_id FROM api_customer") #Execute an sql query
conn.commit()

#Line below creates a unique ID - Need to work out where to put this.
key = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)]) 

#Step 2A: If face doesn't exist, create new face_id
if not fid:
	self.cur.execute("SELECT face_id FROM api_customer") #Check if this is how to add new entry to SQL
	cur.execute('INSERT INTO api_customer values (id, created, face_id, customer_ref, face_sharpness, face_business, first_name, last_name, surname, company_id, loyal')
	conn.commit()

	cur.execute('INSERT INTO ENTRIES (face_id) VALUES (key)')
	conn.commit()

	print("Unknown face, new entry added")

#Step 3A: Match face with with customer details - Need to determine where these details are stored.
#Time/date stamp from another db can be used to relate the two tables!


#Step 2B: If face does exist, do we know the person's details?
else:
	print("Known face")
	det = conn.cursor()
	det.execute("SELECT first_name, last_name FROM api_customer")
	names = det.fetchall()
	det.commit()

	if not names:
		print("No face and id match ") #If either first or last name is missing - match the names from transactions

	else:
		for row in cursor: #If both names are saved, pull that person's data.
			print row[1] #Print the row if there is a result/match

cur.close() #Close the cursor

cur.close() #Close the connection

'''def face():
	for item in event['face_id']:
		return first_name, last_name

	for obj in event['face_id']:
		face_id = 'var' in globals()
		try:
			var
		except NameError:
			face_id = False
		else:
			face_id = True'''

'''Rows
	for row in cursor:
	first_name = str(row[0])
	last_name = str(row[1])'''