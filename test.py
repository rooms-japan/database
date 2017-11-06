# test.py
# Short code to test database connection and a single query
import psycopg2
import sys


try:
	conn = psycopg2.connect(dbname='rooms-japan', user='tiphaine', host='localhost', password='tiphsolange')
except:
	print("Unable to connect to database.")
	sys.exit()

cur = conn.cursor()
cur.execute("SELECT * FROM dwellings LIMIT 1;")
print(cur.fetchall())

conn.close()