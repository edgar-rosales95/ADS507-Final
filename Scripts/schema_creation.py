import mysql.connector as mysql
from mysql.connector import Error
import os
from dotenv import load_dotenv


# Database credentials (replace with your details)
load_dotenv()

hostname=os.getenv('hostname')
port=3306
username='tkirk'
password=os.getenv('password')
ssl_ca = os.getenv('ssl_cert')  # Required for Azure MySQL SSL connection
database = 'wildfire_housing'

try:
    # Establish connection
    conn = mysql.connect(
        host=hostname,
        user=username,
        password=password,
        ssl_ca=ssl_ca,  # Secure connection
        database = database
    )

    if conn.is_connected():
        print("✅ Successfully connected to MySQL database")

except Error as e:
    print(f"❌ Error: {e}")

cursor = conn.cursor()

try:
    cursor.execute('CREATE DATABASE IF NOT EXISTS wildfire_housing')
    print('Database create or already exists')

except mysql.Error as err:
    print(f"Error creating database")

conn.database = database
    
with open('schema.sql', 'r') as schema:
    sql_script = schema.read()

try:

    for statement in sql_script.split(";\n"):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)
except mysql.Error as err:
    print(f"Error executing statement: {statement}")
    print(f"MySQL Error: {err}")

conn.commit()
cursor.close()
conn.close()

print('Database schema created successfully')