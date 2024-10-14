import mysql.connector


def create_database(cursor):
    """Function to create tables in the database."""
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS fabric (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fabric_name VARCHAR(255) NOT NULL,
            fabric_address VARCHAR(255) NOT NULL,
            fabric_type TEXT
        );
    ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                description_instruktsiya TEXT,
                
                components_id INT,
                FOREIGN KEY (components_id) REFERENCES components(id),

                drug_types_id INT,
                FOREIGN KEY (drug_types_id) REFERENCES drug_types(id),

                method_of_application_id INT,
                FOREIGN KEY (method_of_application_id) REFERENCES method_of_application(id),

                drug_characteristics_id INT,
                FOREIGN KEY (drug_characteristics_id) REFERENCES drug_characteristics(id),

                type_of_packaging_id INT,
                FOREIGN KEY (type_of_packaging_id) REFERENCES type_of_packaging(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS availability (
                product_id INT,  
                FOREIGN KEY (product_id) REFERENCES products(id),
                availability_status BOOLEAN,
                total_amount INT,
                availability_in_stock BOOLEAN,
                availability_in_order BOOLEAN
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                
                product_id INT,
                FOREIGN KEY (product_id) REFERENCES products(id),

                customers_id INT,
                FOREIGN KEY (customers_id) REFERENCES customers(id),

                carriers_id INT,
                FOREIGN KEY (carriers_id) REFERENCES carriers(id),

                total_price DECIMAL(10,2),
                total_amount INT,
                order_date DATE,
                order_status BOOLEAN,
                date_of_sending DATE,
                approx_date_of_arrival DATE,
                date_of_arrival DATE,

                order_description TEXT
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS supply (
                id INT AUTO_INCREMENT PRIMARY KEY,
                
                components_id INT,
                FOREIGN KEY (components_id) REFERENCES components(id),

                supplier_id INT,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),

                total_price DECIMAL(10,2),
                total_amount INT,
                supply_date DATE,
                supply_status BOOLEAN,
                date_of_sending DATE,
                approx_date_of_arrival DATE,
                date_of_arrival DATE,

                other_description TEXT
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS supplier (
                id INT AUTO_INCREMENT PRIMARY KEY,
                supplier_first_name VARCHAR(255) NOT NULL,
                supplier_last_name VARCHAR(255) NOT NULL,
                name_of_company_or_organization VARCHAR(255) NOT NULL,
                supplier_address_office_or_storage VARCHAR(255) NOT NULL,
                supplier_phone_number VARCHAR(255) NOT NULL,
                supplier_email VARCHAR(255) NOT NULL,
                supplier_license_number VARCHAR(255) NOT NULL,
                supplier_bank_account_number VARCHAR(255) NOT NULL,

                supplier_license_type INT,
                FOREIGN KEY (supplier_license_type) REFERENCES license_types(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_first_name VARCHAR(255) NOT NULL,
                customer_last_name VARCHAR(255) NOT NULL,
                name_of_company_or_organization VARCHAR(255) NOT NULL,
                customer_address_office_or_storage VARCHAR(255) NOT NULL,
                customer_phone_number VARCHAR(255) NOT NULL,
                customer_email VARCHAR(255) NOT NULL,
                customer_license_number VARCHAR(255) NOT NULL,
                customer_bank_account_number VARCHAR(255) NOT NULL,

                customer_license_type INT,
                FOREIGN KEY (customer_license_type) REFERENCES license_types(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS carriers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                carrier_first_name VARCHAR(255) NOT NULL,
                carrier_last_name VARCHAR(255) NOT NULL,
                name_of_company_or_organization VARCHAR(255) NOT NULL,
                carrier_phone_number VARCHAR(255) NOT NULL,
                carrier_license_number VARCHAR(255) NOT NULL,

                customer_id INT,
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                carrier_address VARCHAR(255) NOT NULL,
                supplier_id INT,
                FOREIGN KEY (supplier_id) REFERENCES supplier(id),

                orders_id INT,
                FOREIGN KEY (orders_id) REFERENCES orders(id),

                supply_id INT,
                FOREIGN KEY (supply_id) REFERENCES supply(id),

                storage_id INT,
                FOREIGN KEY (storage_id) REFERENCES storage(id),

                carrier_license_type_id INT,
                FOREIGN KEY (carrier_license_type_id) REFERENCES license_types(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS storage (
                id INT AUTO_INCREMENT PRIMARY KEY,
                storage_name VARCHAR(255) NOT NULL,
                storage_address VARCHAR(255) NOT NULL,
                storage_phone_number VARCHAR(255) NOT NULL,
                storage_email VARCHAR(255) NOT NULL,
                storage_license_number VARCHAR(255) NOT NULL,
                square_of_storage DECIMAL(10,2) NOT NULL,
                storage_capacity INT NOT NULL,
                temperature_conditions VARCHAR(255) NOT NULL,
                number_of_employees INT NOT NULL,
                special_conditions TEXT,

                employees_id INT,
                FOREIGN KEY (employees_id) REFERENCES employees(id),
                
                storage_boss_id INT,
                FOREIGN KEY (storage_boss_id) REFERENCES employees(id),

                storage_license_type_id INT,
                FOREIGN KEY (storage_license_type_id) REFERENCES license_type(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                employee_first_name VARCHAR(255) NOT NULL,
                employee_last_name VARCHAR(255) NOT NULL,
                employee_phone_number VARCHAR(255) NOT NULL,
                employee_income DECIMAL(10,2) NOT NULL,
                employee_experience INT NOT NULL,

                fabric_id INT,
                FOREIGN KEY (fabric_id) REFERENCES fabric(id),

                storage_id INT,
                FOREIGN KEY (storage_id) REFERENCES storage(id),

                workplace ENUM('factory', 'storage') NOT NULL,

                directory_of_occupations_id INT,
                FOREIGN KEY (directory_of_occupations_id) REFERENCES directory_of_occupations(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS directory_of_occupations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                occupation VARCHAR(255) NOT NULL UNIQUE,
                qualification VARCHAR(255) NOT NULL UNIQUE,
                salary DECIMAL(10,2) NOT NULL
            );
        ''')

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

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS drug_types (
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_name VARCHAR(255) NOT NULL UNIQUE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS type_of_component (
                id INT AUTO_INCREMENT PRIMARY KEY,
                component_type VARCHAR(255) NOT NULL UNIQUE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS method_of_application (
                id INT AUTO_INCREMENT PRIMARY KEY,
                method VARCHAR(255) NOT NULL UNIQUE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS drug_characteristics (
                id INT AUTO_INCREMENT PRIMARY KEY,
                characteristics VARCHAR(255) NOT NULL UNIQUE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS type_of_packaging (
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_of_packaging VARCHAR(255) NOT NULL UNIQUE,
                number_in_pack INT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stage_of_sending (
                id INT AUTO_INCREMENT PRIMARY KEY,
                stage_of_sending VARCHAR(255) NOT NULL UNIQUE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS license_type (
                id INT AUTO_INCREMENT PRIMARY KEY,
                license_type VARCHAR(255) NOT NULL UNIQUE
            );
        ''')
        print("Tables created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating tables: {e}")

def insert_data(cursor):
    """Function to insert data into the database tables."""
    try:
        # Insert data into the 'fabric' table
        fabrics = [
            ("Фабрика 1", "вул. Заводська, 1, Київ", "Фармацевтична"),
            ("Фабрика 2", "вул. Промислова, 2, Львів", "Хімічна")
        ]
        cursor.executemany("INSERT IGNORE INTO fabric (fabric_name, fabric_address, fabric_type) VALUES (%s, %s, %s)", fabrics)

        # Insert data into the 'products' table
        products = [
            ("Продукт 1", 100.00, "Інструкція 1", 1, 1, 1, 1, 1),
            ("Продукт 2", 200.00, "Інструкція 2", 2, 2, 2, 2, 2)
        ]
        cursor.executemany("INSERT IGNORE INTO products (product_name, price, description_instruktsiya, components_id, drug_types_id, method_of_application_id, drug_characteristics_id, type_of_packaging_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", products)

        # Insert data into the 'availability' table
        availability = [
            (1, True, 100, True, False),
            (2, False, 50, False, True)
        ]
        cursor.executemany("INSERT IGNORE INTO availability (product_id, availability_status, total_amount, availability_in_stock, availability_in_order) VALUES (%s, %s, %s, %s, %s)", availability)

        # Insert data into the 'orders' table
        orders = [
            (1, 1, 1, 100.00, 10, "2023-01-01", True, "2023-01-02", "2023-01-05", "2023-01-05", "Опис замовлення 1"),
            (2, 2, 2, 200.00, 20, "2023-02-01", False, "2023-02-02", "2023-02-05", "2023-02-05", "Опис замовлення 2")
        ]
        cursor.executemany("INSERT IGNORE INTO orders (product_id, customers_id, carriers_id, total_price, total_amount, order_date, order_status, date_of_sending, approx_date_of_arrival, date_of_arrival, order_description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", orders)

        # Insert data into the 'supply' table
        supplies = [
            (1, 1, 500.00, 50, "2023-01-01", True, "2023-01-02", "2023-01-05", "2023-01-05", "Опис постачання 1"),
            (2, 2, 300.00, 30, "2023-02-01", False, "2023-02-02", "2023-02-05", "2023-02-05", "Опис постачання 2")
        ]
        cursor.executemany("INSERT IGNORE INTO supply (components_id, supplier_id, total_price, total_amount, supply_date, supply_status, date_of_sending, approx_date_of_arrival, date_of_arrival, other_description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", supplies)

        # Insert data into the 'customers' table
        customers = [
            ("Іван", "Петров", "ТОВ Покупець", "вул. Покупецька, 1, Київ", "380501234568", "petrov@customer.ua", "Л-4444", "UA9876543211", 1),
            ("Олена", "Сидорова", "ТОВ Замовник", "вул. Замовницька, 2, Львів", "380501234569", "sidorova@customer.ua", "Л-5555", "UA9876543212", 2)
        ]
        cursor.executemany('''
            INSERT IGNORE INTO customers (customer_first_name, customer_last_name, name_of_company_or_organization,
            customer_address_office_or_storage, customer_phone_number, customer_email, customer_license_number,
            customer_bank_account_number, customer_license_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', customers)

        # Insert data into the 'carriers' table
        carriers = [
            ("Сергій", "Коваль", "ТОВ Перевізник", "380501234570", "Л-6666", 1, "вул. Перевізницька, 1, Київ", 1, 1, 1, 1, 1),
            ("Марія", "Іванова", "ТОВ Доставка", "380501234571", "Л-7777", 2, "вул. Доставницька, 2, Львів", 2, 2, 2, 2, 2)
        ]
        cursor.executemany('''
            INSERT IGNORE INTO carriers (carrier_first_name, carrier_last_name, name_of_company_or_organization,
            carrier_phone_number, carrier_license_number, customer_id, carrier_address, supplier_id, orders_id,
            supply_id, storage_id, carrier_license_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', carriers)

        # Insert data into the 'storage' table
        storage_data = [
            ("Склад 1", "вул. Складська, 1, Київ", "380501234572", "storage1@warehouse.ua", "Л-8888", 1000.00, 500, "15-25°C", 10, "Особливі умови 1", 1, 1, 1),
            ("Склад 2", "вул. Складська, 2, Львів", "380501234573", "storage2@warehouse.ua", "Л-9999", 2000.00, 1000, "10-20°C", 20, "Особливі умови 2", 2, 2, 2)
        ]
        cursor.executemany('''
            INSERT IGNORE INTO storage (storage_name, storage_address, storage_phone_number, storage_email,
            storage_license_number, square_of_storage, storage_capacity, temperature_conditions, number_of_employees,
            special_conditions, employees_id, storage_boss_id, storage_license_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', storage_data)

        # Insert data into the 'employees' table
        employees = [
            ("Олександр", "Кузьменко", "380501234574", 15000.00, 5, 1, 1, "factory", 1),
            ("Наталія", "Шевченко", "380501234575", 20000.00, 10, 2, 2, "storage", 2)
        ]
        cursor.executemany('''
            INSERT IGNORE INTO employees (employee_first_name, employee_last_name, employee_phone_number,
            employee_income, employee_experience, fabric_id, storage_id, workplace, directory_of_occupations_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', employees)

        # Insert data into the 'directory_of_occupations' table
        occupations = [
            ("Інженер", "Вища", 15000.00),
            ("Менеджер", "Вища", 20000.00)
        ]
        cursor.executemany("INSERT IGNORE INTO directory_of_occupations (occupation, qualification, salary) VALUES (%s, %s, %s)", occupations)

        # Insert data into other tables (e.g., drug_types, method_of_application)
        # Repeat the same process as shown above for the remaining tables

        print("Data inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")

def main():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",       # MySQL server address
            user="root",            # Your MySQL username
            password="1233",        # Your MySQL password
            database="sql_kursova"  # Your database name
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Create tables
        create_database(cursor)

        # Insert data into tables
        insert_data(cursor)

        # Commit changes
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed successfully.")

if __name__ == '__main__':
    main()