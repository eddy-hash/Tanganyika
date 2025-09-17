import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Eddy@123",
    db="university_db"
)

print("Connected successfully!")
db.close()
