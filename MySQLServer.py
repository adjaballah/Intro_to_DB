import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL server address if different
            user='your_user',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except for MySQL. connector.Error as e:
        # Raising the exception after catching it
        raise Exception(f"An error occurred while interacting with MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    try:
        create_database()
    except Exception as e:
        print(f"Error: {e}")
