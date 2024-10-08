import mysql.connector

conn = mysql.connector.connect(
    host="localhost",       # Або IP-адреса сервера MySQL
    user="root",    # Ваш логін до MySQL
    password="1233",# Ваш пароль до MySQL
    database="sql_kursova" # Ім'я бази даних
)

cursor = conn.cursor()

cursor.execute ('''
    CREATE TABLE products IF NOT EXISTS (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                

                


''')