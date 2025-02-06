import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (modify host, user, password as needed)
        connection = mysql.connector.connect(
            host='localhost',  # Change if MySQL is hosted elsewhere
            user='root',        # Change to your MySQL username
            password='yourpassword'  # Change to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()