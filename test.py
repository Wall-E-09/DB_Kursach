import mysql.connector

conn = mysql.connector.connect(
    host="localhost",       # Або IP-адреса сервера MySQL
    user="root",            # Ваш логін до MySQL
    password="1233",        # Ваш пароль до MySQL
    database="sql_kursova"  # Ім'я бази даних
)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS components (
        id INT AUTO_INCREMENT PRIMARY KEY,
        components VARCHAR(255) NOT NULL UNIQUE,

        type_of_component INT,
        FOREIGN KEY (type_of_component) REFERENCES type_of_component(id),
        
        total_amount INT NOT NULL,
        price DECIMAL(10,2) NOT NULL
    );
''')