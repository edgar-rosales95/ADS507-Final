import mysql.connector as mysql
from mysql.connector import Error
import os
from dotenv import load_dotenv


# Database credentials (replace with your details)
load_dotenv()

hostname=os.getenv('wildfire-watch1.mysql.database.azure.com')
port=3306
username='tkirk'
password=os.getenv('Wildfire507')
ssl_ca = os.getenv('ssl_cert')  # Required for Azure MySQL SSL connection
database = 'wildfire_housing'

try:
    # Establish connection
    conn = mysql.connect(
        host="wildfire-watch1.mysql.database.azure.com",
        user="tkirk",
        password="Wildfire507",
        ssl_ca=ssl_ca,  # Secure connection
        database = "wildfire_housing"
    )

    if conn.is_connected():
        print("✅ Successfully connected to MySQL database")

except Error as e:
    print(f"❌ Error: {e}")