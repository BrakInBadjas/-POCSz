import MySQLdb
import time

#Open connection to the database
db = MySQLdb.connect(host="sql7.freesqldatabase.com",    	# your host, usually localhost
                     user="sql7142368",         			# your username
                     passwd="y65TanAMCg",  					# your password
                     db="sql7142368")      				  	# name of the data base					 
cur = db.cursor()

#Get a public_key from the Door Table selected on id
#returns a public_key belonging to the door_id
def getDoorPublicKey(door_id):
	query = 'SELECT public_key FROM Door WHERE id=' + str(door_id) + ';'
	cur.execute(query)
	return cur.fetchone()[0]
	
#Add a new Door to the Door Table
def addNewDoor(door_id, public_key):
	query = 'INSERT INTO Door VALUES (' + str(door_id) + ',\'' + public_key + '\');'
	cur.execute(query)
	db.commit()	
	
#Get a Role from the Role Table selected on id
#returns the role_name belonging to the role_id
def getRole(role_id):
	query = 'SELECT name FROM Role WHERE id=' + str(role_id) + ';'
	cur.execute(query)
	return cur.fetchone()[0]
	
#Add a new Role to the Role Table
def addNewRole(role_id, role_name):
	query = 'INSERT INTO Role VALUES (' + str(role_id) + ',\'' + role_name + '\');'
	cur.execute(query)
	db.commit()	
	
#Get a Person from the Person Table selected on id
#returns a 4-tuple containing (person_id, key_uid, person_name, role_id) belonging to the id
def getPerson(user_id):
	query = 'SELECT * FROM Person WHERE key_uid=' + str(user_id) + ';'
	cur.execute(query)
	return cur.fetchone()
	
#Get a Person from the Person Table selected on key_uid
#returns a 4-tuple containing (person_id, key_uid, person_name, role_id) belonging to the key_uid
def getPersonByUID(key_uid):
	query = 'SELECT * FROM Person WHERE key_uid=\'' + str(key_uid) + '\';'
	cur.execute(query)
	return cur.fetchone()
	
#Add a new Person to the Person Table
def addNewPerson(person_id, key_uid, name, role_id):
	query = 'INSERT INTO Person VALUES (' + str(person_id) + ',\'' + key_uid + '\',\'' + name + '\',' + str(role_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Get a all door_id's to which a person has access
#returns a list of door_id's
def getPersonDoor(user_id):
	query = 'SELECT door_id FROM Person_Door WHERE person_id=' + str(user_id) + ';'
	cur.execute(query)
	return [list(a) for a in cur.fetchall()]
	
#Add a new Combination of person_id, door_id to the Person_Door Table
def addNewPersonDoor(user_id, door_id):
	query = 'INSERT INTO Person_Door VALUES (' + str(user_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Get a all door_id's to which a role has access
#returns a list of door_id's
def getRoleDoor(role_id):
	query = 'SELECT door_id FROM Role_Door WHERE role_id=' + str(role_id) + ';'
	cur.execute(query)
	return [list(a) for a in cur.fetchall()]
	
#Add a new Combination of role_id, door_id to the Role_Door Table
def addNewRoleDoor(role_id, door_id):
	query = 'INSERT INTO Role_Door VALUES (' + str(role_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Some test commands	

#To use the add function, first be sure there is no entry with that id in the table you want to add something to
#	addNewDoor(5, 'asasdfpoirewmsnd')
#	addNewRole(1, 'Tester')
#	addNewPerson(0, 'DC 7C 98 1E', 'Chris Witteveen', 1)
#	addNewPersonDoor(0, 0)
#	addNewRoleDoor(1, 1)

#Specify for which user we are going to check to which doors he has acces
person_id = 0
person = getPerson(person_id)

#Check acces, first by person_id then by role_id
print person[2] + " has access to the following doors:"
for row in getPersonDoor(person_id):
	print " - Door " + str(row[0]) + " with public key: " + getDoorPublicKey(row[0])
print "His role: " + getRole(person[3]) + ", grants him access to the following doors:"
for row in getRoleDoor(person[3]):
	print " - Door " + str(row[0]) + " with public key: " + getDoorPublicKey(row[0])
print "His Key UID is: " + person[1]

#For readability
print ""
print ""

startt = time.time()

#Specify which door to open
doorToOpen = 1L

#Check who tried to enter the door
person = getPersonByUID("DC 7C 98 1E")
print "A card with UID: DC 7C 98 1E, has tried to open door " + str(doorToOpen)
print "This card belongs to " + person[2] + " with ID: " + str(person[0]) + " and Role ID: " + str(person[3])

#Check if the user has access to the door
if ([doorToOpen]) in getPersonDoor(person[0]):
	print "He has acces to this door!"
elif ([doorToOpen]) in getRoleDoor(person[3]):
	print "His role has granted him access!"
else:
	print person[2] + " has no access to this door!"
	
#Check how long it took to check who tried to gain access and if he has access
endt = time.time()
print "it took " + str(endt - startt) + " seconds to check if the card had access!"	

#Example output:
#  	Chris Witteveen has access to the following doors:
#  	 - Door 0 with public key: asjfde942e9fdsffsdfsdfsdfsdfsdfsddsf
#  	His role: Tester, grants him access to the following doors:
#  	 - Door 0 with public key: asjfde942e9fdsffsdfsdfsdfsdfsdfsddsf
#  	 - Door 1 with public key: asjfde942e9fasdfsddsf
#  	His Key UID is: DC 7C 98 1E
#  	
#  	
#  	A card with UID: DC 7C 98 1E, has tried to open door 5
#  	This card belongs to Chris Witteveen with ID: 0 and Role ID: 1
#  	Chris Witteveen has no access to this door!
#  	it took 0.0780000686646 seconds to check if the card had access!
