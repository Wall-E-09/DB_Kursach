import mysql.connector

# Підключення до бази даних
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",  # Ваш логін
    password="yourpassword"  # Ваш пароль
)

cursor = conn.cursor()

# Створення бази даних
cursor.execute("CREATE DATABASE IF NOT EXISTS pharma_db")
cursor.execute("USE pharma_db")
