#https://sourceforge.net/projects/mysql-python/files/latest/download?source=files

#Host: sql7.freesqldatabase.com
#Database name: sql7142368
#Database user: sql7142368
#Database password: y65TanAMCg
#Port number: 3306

#DROP TABLE IF EXISTS Person_Door;
#DROP TABLE IF EXISTS Role_Door;
#DROP TABLE IF EXISTS Person;
#DROP TABLE IF EXISTS Door;
#DROP TABLE IF EXISTS Role;
#
#CREATE TABLE Role (
#	id INT NOT NULL,
#	name TEXT NOT NULL,
#	PRIMARY KEY (id)
#);
#
#CREATE TABLE Person (
#	id INT NOT NULL,
#	key_uid INT NOT NULL,
#	name TEXT NOT NULL,
#	role_id NOT NULL,
#	PRIMARY KEY (id),
#	FOREIGN KEY (role_id) REFERENCES Role(id)
#);
#
#CREATE TABLE Door (
#	id INT NOT NULL,
#	public_key TEXT NOT NULL,
#	PRIMARY KEY (id)
#);
#
#CREATE TABLE Role_Door (
#	role_id INT NOT NULL,
#	door_id INT NOT NULL,
#	PRIMARY KEY (role_id, door_id),
#	FOREIGN KEY (role_id) REFERENCES Role(id),
#	FOREIGN KEY (door_id) REFERENCES Door(id)
#);
#
#CREATE TABLE Person_Door (
#	person_id INT NOT NULL,
#	door_id INT NOT NULL,
#	PRIMARY KEY (person_id, door_id),
#	FOREIGN KEY (person_id) REFERENCES Person(id),
#	FOREIGN KEY (door_id) REFERENCES Door(id)
#);
import MySQLdb

db = MySQLdb.connect(host="sql7.freesqldatabase.com",    	# host server
                     user="sql7142368",         			# username
                     passwd="y65TanAMCg",  					# password
                     db="sql7142368")      				  	# db name

#Create cursor. We use this to execute queries
cur = db.cursor()

#Execute all queries
cur.execute('DROP TABLE IF EXISTS Person_Door;')
cur.execute('DROP TABLE IF EXISTS Role_Door;')
cur.execute('DROP TABLE IF EXISTS Person;')
cur.execute('DROP TABLE IF EXISTS Door;')
cur.execute('DROP TABLE IF EXISTS Role;') 
cur.execute('CREATE TABLE Role (id INT NOT NULL, name TEXT NOT NULL, PRIMARY KEY (id));')
cur.execute('CREATE TABLE Person (id INT NOT NULL, key_uid INT NOT NULL, name TEXT NOT NULL, role_id INT NOT NULL, PRIMARY KEY (id), FOREIGN KEY (role_id) REFERENCES Role(id));')
cur.execute('CREATE TABLE Door (id INT NOT NULL, public_key TEXT NOT NULL, PRIMARY KEY (id) );') 
cur.execute('CREATE TABLE Role_Door (role_id INT NOT NULL, door_id INT NOT NULL, PRIMARY KEY (role_id, door_id), FOREIGN KEY (role_id) REFERENCES Role(id), FOREIGN KEY (door_id) REFERENCES Door(id) );') 
cur.execute('CREATE TABLE Person_Door (person_id INT NOT NULL, door_id INT NOT NULL, PRIMARY KEY (person_id, door_id), FOREIGN KEY (person_id) REFERENCES Person(id), FOREIGN KEY (door_id) REFERENCES Door(id) );') 

#Close cursor and database
cur.close() 
db.close()