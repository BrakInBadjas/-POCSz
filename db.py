import MySQLdb

#Open connection to the database
db = MySQLdb.connect(host="sql7.freesqldatabase.com",    	# your host, usually localhost
                     user="sql7142368",         			# your username
                     passwd="y65TanAMCg",  					# your password
                     db="sql7142368")      				  	# name of the data base
					 
cur = db.cursor()

#Get a Door from the Door Table selected on id
def getDoorPublicKey(door_id):
	query = 'SELECT * FROM Door WHERE id=' + str(door_id) + ';'
	cur.execute(query)
	print "Id: %s -- Public Key: %s" % cur.fetchone()
	
#Add a new Door to the Door Table
def addNewDoor(door_id, public_key):
	query = 'INSERT INTO Door VALUES (' + str(door_id) + ',\'' + public_key + '\');'
	cur.execute(query)
	db.commit()	
	
#Get a Role from the Role Table selected on id
def getRole(role_id):
	query = 'SELECT * FROM Role WHERE id=' + str(role_id) + ';'
	cur.execute(query)
	print "Id: %s -- Name: %s" % cur.fetchone()
	
#Add a new Role to the Role Table
def addNewRole(role_id, role_name):
	query = 'INSERT INTO Role VALUES (' + str(role_id) + ',\'' + role_name + '\');'
	cur.execute(query)
	db.commit()	
	
#Get a Person from the Person Table selected on id
def getPerson(user_id):
	query = 'SELECT Person.id, Person.key_uid, Person.name, Role.name FROM Person, Role WHERE Person.id=' + str(user_id) + ' AND Person.role_id = Role.id;'
	cur.execute(query)
	print "Id: %s -- Key UID: %s -- Name: %s -- Role: %s" % cur.fetchone()
	
#Add a new Person to the Person Table
def addNewPerson(person_id, key_uid, name, role_id):
	query = 'INSERT INTO Person VALUES (' + str(person_id) + ',\'' + key_uid + '\',\'' + name + '\',' + str(role_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Get a Combination of person_id, person_name and door_if from the Person_Door Table selected on Person_Door.person_id
def getPersonDoor(user_id):
	query = 'SELECT Person_Door.person_id, Person.name, Person_Door.door_id FROM Person, Person_Door WHERE Person_Door.person_id=' + str(user_id) + ';'
	cur.execute(query)
	print "User [ID]Name: [%s]%s -- Door ID: %s" % cur.fetchone()
	
#Add a new Combination of person_id, door_id to the Person_Door Table
def addNewPersonDoor(user_id, door_id):
	query = 'INSERT INTO Person_Door VALUES (' + str(user_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Get a Combination of role_id, role_name, door_id from the Role_Door Table selected on Role_Door.role_id
def getRoleDoor(role_id):
	query = 'SELECT Role_Door.role_id, Role.name, Role_Door.door_id FROM Role, Role_Door WHERE Role_Door.role_id=' + str(role_id) + ';'
	cur.execute(query)
	print "Role [ID]Name: [%s]%s -- Door ID: %s" % cur.fetchone()
	
#Add a new Combination of role_id, door_id to the Role_Door Table
def addNewRoleDoor(role_id, door_id):
	query = 'INSERT INTO Role_Door VALUES (' + str(role_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Some test commands	

#To use the add function, first be sure there is no entry with that id in the table you want to add something to
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