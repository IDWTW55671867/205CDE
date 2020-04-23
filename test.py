import csv
import sqlite3

with open('./admin.csv', newline='') as user:
    user_reader = csv.DictReader(user)
    user = [
    	(row['email'], row['password'], row['groups'])
    	for row in user_reader
    ]

with open('create_db.sql') as f:
	create_db_sql = f.read()

db = sqlite3.connect('user.db')
c = db.cursor()
c.executescript(create_db_sql)

with db:
	c.executemany('insert into user (email,password,groups) values (?,?,?)',user)

c = db.execute('SELECT * FROM user')
for row in c:
	print(row)