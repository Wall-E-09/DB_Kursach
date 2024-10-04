import mysql.connector

# Example of connecting to a MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            # Perform database operations here
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    connect_to_database()