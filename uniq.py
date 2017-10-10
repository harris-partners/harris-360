import random
import string
import schedule
import time

def job():
	key = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
	print key

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)