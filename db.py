import MySQLdb

db = MySQLdb.connect(host="sql7.freesqldatabase.com",    	# your host, usually localhost
                     user="sql7142368",         			# your username
                     passwd="y65TanAMCg",  					# your password
                     db="sql7142368")      				  	# name of the data base
					 
cur = db.cursor()

def getDoorPublicKey(door_id):
	query = 'SELECT * FROM Door WHERE id=' + str(door_id) + ';'
	cur.execute(query)
	print "Id: %s -- Public Key: %s" % cur.fetchone()
	
def addNewDoor(door_id, public_key):
	query = 'INSERT INTO Door VALUES (' + str(door_id) + ',\'' + public_key + '\');'
	cur.execute(query)
	db.commit()	
	
def getRole(role_id):
	query = 'SELECT * FROM Role WHERE id=' + str(role_id) + ';'
	cur.execute(query)
	print "Id: %s -- Name: %s" % cur.fetchone()
	
def addNewRole(role_id, role_name):
	query = 'INSERT INTO Role VALUES (' + str(role_id) + ',\'' + role_name + '\');'
	cur.execute(query)
	db.commit()	
	
def getPerson(user_id):
	query = 'SELECT Person.id, Person.key_uid, Person.name, Role.name FROM Person, Role WHERE Person.id=' + str(user_id) + ' AND Person.role_id = Role.id;'
	cur.execute(query)
	print "Id: %s -- Key UID: %s -- Name: %s -- Role: %s" % cur.fetchone()
	
def addNewPerson(person_id, key_uid, name, role_id):
	query = 'INSERT INTO Person VALUES (' + str(person_id) + ',\'' + key_uid + '\',\'' + name + '\',' + str(role_id) + ');'
	cur.execute(query)
	db.commit()	
	
def getPersonDoor(user_id):
	query = 'SELECT Person_Door.person_id, Person.name, Person_Door.door_id FROM Person, Person_Door WHERE Person_Door.person_id=' + str(user_id) + ';'
	cur.execute(query)
	print "User [ID]Name: [%s]%s -- Door ID: %s" % cur.fetchone()
	
def addNewPersonDoor(user_id, door_id):
	query = 'INSERT INTO Person_Door VALUES (' + str(user_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
def getRoleDoor(role_id):
	query = 'SELECT Role_Door.role_id, Role.name, Role_Door.door_id FROM Role, Role_Door WHERE Role_Door.role_id=' + str(role_id) + ';'
	cur.execute(query)
	print "Role [ID]Name: [%s]%s -- Door ID: %s" % cur.fetchone()
	
def addNewRoleDoor(role_id, door_id):
	query = 'INSERT INTO Role_Door VALUES (' + str(role_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
#addNewDoor(0, 'asjfde942e9fdsffsdfsdfsdfsdfsdfsddsf')
#addNewRole(1, 'Tester')
#addNewPerson(0, 'DC 7C 98 1E', 'Chris Witteveen', 1)
#addNewPersonDoor(0, 0)
#addNewRoleDoor(1, 0)

getDoorPublicKey(0)
getRole(1)
getPerson(0)
getPersonDoor(0)
getRoleDoor(1)