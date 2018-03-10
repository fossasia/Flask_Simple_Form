import MySQLdb

def connect():
	c=MySQLdb.connect(host="localhost",user="root",passwd="#your_own_password",db="#your_own_database_name")
	d=c.cursor()
	return c,d
