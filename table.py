import boto3	#Used for AWS... Not sure if required.
import MySQLdb 	#Need for connection to SQL db
import random	#Need for random id generation
import string	#Need for random id generation

conn = MySQLdb.connect(host="harrisfaceapi.ckuvqwkjly5s.ap-southeast-2.rds.amazonaws.com", port=3306, user="harris", passwd="988$_iADO_k9484ASDJFSDJ_afdsj", db="harris_face_dev")
cur = conn.cursor() #Create a cursor for the select
print("You have just connected to the database! You are a true legend!")

cur.execute("SELECT * FROM api_customer")
results = cur.fetchall()

#Create a table for print function
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

#Print the results of the SQL Table in a table format
print(separator)
print(tavnit % tuple(columns))
print(separator)

for row in results:
	print(tavnit % row)
print(separator)

cur.close()
conn.close()