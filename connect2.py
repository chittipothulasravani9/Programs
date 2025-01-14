import mysql.connector

# Establish the connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='21mg1a0573',
    database='students'
)

# Create a cursor
mycursor = mydb.cursor()

# Clear the table
mycursor.execute("DELETE FROM data")

# Create table (if not exists)
mycursor.execute("CREATE TABLE IF NOT EXISTS data (rollno INT, sname VARCHAR(255), branch VARCHAR(255))")

# Example: Insert multiple records
sql = "INSERT INTO data (rollno, sname, branch) VALUES (%s, %s, %s)"
values = [
    (1, 'Sravani', 'CSE'),
    (2, 'Chinnu', 'MEC'),
    (3, 'Leela', 'CSE'),
    (4, 'Chitti', 'ECE')
]

# Insert all records
mycursor.executemany(sql, values)
mydb.commit()

# Fetch and print data from the table
mycursor.execute("SELECT * FROM data")
result = mycursor.fetchall()
for x in result:
    print(x)
