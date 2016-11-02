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

with open('createDB.sql', 'r') as content_file:
	query = content_file.read()

cur.execute(query)
db.commit()
 
db.close()