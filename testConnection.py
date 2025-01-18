import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',       # e.g., 'localhost' or the IP address of your MySQL server
            database='database',  # The name of your database
            user='root',    # Your MySQL username
            password='password' # Your MySQL user password
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            # Get the server info
            db_info = connection.get_server_info()
            print("MySQL Server version:", db_info)

            # Create a cursor object
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connected to the database:", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function to connect
connect_to_database()
