import csv
import sqlite3
from flask import Flask, g


app = Flask(__name__)
SQLITE_DB_PATH = 'user.db'
SQLITE_DB_SCHEMA = 'create_db.sql'
USER_CSV_PATH = 'admin.csv'


def get_db():
	db = g._database = sqlite3.connect(SQLITE_DB_PATH)
	db.execute("PRAGMA foreign_keys = ON")
	return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)


@app.before_first_request
def create_db():
	db = sqlite3.connect('user.db')
	c = db.cursor()
	c.execute('''DROP TABLE IF EXISTS user''')
	c.execute('''CREATE TABLE user (email text,password text,groups text);''')
	purchases = [('admin1@admin1','admin1','admin')
				,('admin2@admin2','admin2','admin')
				,('admin3@admin3','admin3','admin')
				,('guest1@guest1','guest1','guest')
				,('guest2@guest2','guest2','guest')
				,('guest3@guest3','guest3','guest')]
	c.executemany('insert into user (email,password,groups) values (?,?,?)',user)
	c.commit()
	c.close()