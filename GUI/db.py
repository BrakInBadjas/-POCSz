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
def addNewRole(role_name):
	query = 'INSERT INTO Role VALUES (NULL,\'' + role_name + '\');'
	cur.execute(query)
	db.commit()	
	
#Add a new Person to the Database
def addNewPerson(key_uid, name, role_id):
	query = 'INSERT INTO Person VALUES (NULL,\'' + key_uid + '\',\'' + name + '\',' + str(role_id) + ');'
	cur.execute(query)
	db.commit()	
	
#Add a new Door to the Database
def addNewDoor(public_key):
	query = 'INSERT INTO Door VALUES (NULL,\'' + public_key + '\');'
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
	query = 'SELECT * FROM Role WHERE id=' + str(role_id) + ';'
	cur.execute(query)
	return cur.fetchone()
    
def getRoleByName(role_name):
	query = 'SELECT * FROM Role WHERE name=\'' + str(role_name) + '\';'
	cur.execute(query)
	return cur.fetchone()
	
#Returns the public_key belonging to the door_id
def getDoorPublicKey(door_id):
	query = 'SELECT public_key FROM Door WHERE id=' + str(door_id) + ';'
	cur.execute(query)
	return cur.fetchone()[0]

#Return a 4-tuple of (ID, Key UID, Name, Role ID) belonging to the user_id
def getPerson(user_id):
	query = 'SELECT * FROM Person WHERE id=' + str(user_id) + ';'
	cur.execute(query)
	return cur.fetchone()

#Return a 4-tuple of (ID, Key UID, Name, Role ID) belonging to the key_uid	
def getPersonByUID(key_uid):
	query = 'SELECT * FROM Person WHERE key_uid=\'' + str(key_uid) + '\';'
	cur.execute(query)
	return cur.fetchone()
	
def getPersonByName(name):
	query = 'SELECT * FROM Person WHERE name=\"' + str(name) + '\";'
	cur.execute(query)
	return cur.fetchone() 
    
def getPersonByRole(role_id):
	query = 'SELECT * FROM Person WHERE role_id=\"' + str(role_id) + '\";'
	cur.execute(query)
	return cur.fetchall()
    
#Returns a list of all doors a person has access to (Access by group not included)
def getPersonDoor(user_id):
	query = 'SELECT door_id FROM Person_Door WHERE person_id=' + str(user_id) + ';'
	cur.execute(query)
	ids = []
	for a in cur.fetchall():
		ids.append(a['door_id'])
	return ids
    
def getDoorPerson(door_id):
	query = 'SELECT person_id FROM Person_Door WHERE door_id=' + str(door_id) + ';'
	cur.execute(query)
	ids = []
	for a in cur.fetchall():
		ids.append(a['person_id'])
	return ids

#Returns a list of all doors a role has access to
def getRoleDoor(role_id):
	query = 'SELECT door_id FROM Role_Door WHERE role_id=' + str(role_id) + ';'
	cur.execute(query)
	ids = []
	for a in cur.fetchall():
		ids.append(a['door_id'])
	return ids
    
def getDoorRole(door_id):
	query = 'SELECT role_id FROM Role_Door WHERE door_id=' + str(door_id) + ';'
	cur.execute(query)
	ids = []
	for a in cur.fetchall():
		ids.append(a['role_id'])
	return ids

def getDoorCount(door_id):
	query = 'SELECT count(*) FROM Door WHERE id=' + str(door_id) + ';'
	cur.execute(query)
	return cur.fetchone()
	
def removePermPers(person_id, door_id):
    query = 'Delete FROM Person_Door WHERE person_id=' + str(person_id) + ' AND door_id=' + str(door_id) +';'
    cur.execute(query)
    db.commit()
    
def removeAllPermPers(person_id):
    query = 'Delete FROM Person_Door WHERE person_id=' + str(person_id) + ';'
    cur.execute(query)
    db.commit()
    
def removePerson(person_id,):
    query = 'Delete FROM Person WHERE id=' + str(person_id) + ';'
    cur.execute(query)
    db.commit()
    
def removePermRole(role_id, door_id):
    query = 'Delete FROM Role_Door WHERE role_id=' + str(role_id) + ' AND door_id=' + str(door_id) +';'
    cur.execute(query)
    db.commit()
    
def removeAllPermRole(role_id):
    query = 'Delete FROM Role_Door WHERE role_id=' + str(role_id) + ';'
    cur.execute(query)
    db.commit()
    
def removeRolePers(role_id):
    query = 'UPDATE Person SET role_id=NULL WHERE role_id=' + str(role_id) + ';'
    cur.execute(query)
    db.commit()
    
def removeRole(role_id,):
    query = 'Delete FROM Role WHERE id=' + str(role_id) + ';'
    cur.execute(query)
    db.commit()