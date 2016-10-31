import pymysql.cursors

#Database Settings
host = "sql7.freesqldatabase.com"
user = "sql7142368"
password = "y65TanAMCg"
db = "sql7142368"

#Open connection to Database and start cursor. We use the cursor to execute queries.
db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)				 
cur = db.cursor()



#Function to add new entries to the Database
#Add new Role to the Database
def addNewRole(role_id, role_name):
	query = 'INSERT INTO Role VALUES (' + str(role_id) + ',\'' + role_name + '\');'
	cur.execute(query)
	db.commit()	
	
#Add a new Person to the Database
def addNewPerson(person_id, key_uid, name, role_id):
	query = 'INSERT INTO Person VALUES (' + str(person_id) + ',\'' + key_uid + '\',\'' + name + '\',' + str(role_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Add a new Door to the Database
def addNewDoor(door_id, public_key):
	query = 'INSERT INTO Door VALUES (' + str(door_id) + ',\'' + public_key + '\');'
	cur.execute(query)
	db.commit()	
	
#Add a new Permission, to open a Door, for a Person to the Database
def addNewPersonDoor(user_id, door_id):
	query = 'INSERT INTO Person_Door VALUES (' + str(user_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Add a new Permission, to open a Door, for a Role to the Database
def addNewRoleDoor(role_id, door_id):
	query = 'INSERT INTO Role_Door VALUES (' + str(role_id) + ',' + str(door_id) + ');'
	cur.execute(query)
	db.commit()	

#Functions to get data from the Database	
#Returns the role belonging to the role_id
def getRole(role_id):
	query = 'SELECT name FROM Role WHERE id=' + str(role_id) + ';'
	cur.execute(query)
	return cur.fetchone()[0]
	
#Returns the public_key belonging to the door_id
def getDoorPublicKey(door_id):
	query = 'SELECT public_key FROM Door WHERE id=' + str(door_id) + ';'
	cur.execute(query)
	return cur.fetchone()[0]

#Return a 4-tuple of (ID, Key UID, Name, Role ID) belonging to the user_id
def getPerson(user_id):
	query = 'SELECT * FROM Person WHERE key_uid=' + str(user_id) + ';'
	cur.execute(query)
	return cur.fetchone()

#Return a 4-tuple of (ID, Key UID, Name, Role ID) belonging to the key_uid	
def getPersonByUID(key_uid):
	query = 'SELECT * FROM Person WHERE key_uid=\'' + str(key_uid) + '\';'
	cur.execute(query)
	return cur.fetchone()
	
#Returns a list of all doors a person has access to (Access by group not included)
def getPersonDoor(user_id):
	query = 'SELECT door_id FROM Person_Door WHERE person_id=' + str(user_id) + ';'
	cur.execute(query)
	return [list(a) for a in cur.fetchall()]

#Returns a list of all doors a role has access to
def getRoleDoor(role_id):
	query = 'SELECT door_id FROM Role_Door WHERE role_id=' + str(role_id) + ';'
	cur.execute(query)
	return [list(a) for a in cur.fetchall()]
	