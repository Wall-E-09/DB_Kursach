import mysql.connector

conn = mysql.connector.connect(
    host="localhost",       # Або IP-адреса сервера MySQL
    user="root",            # Ваш логін до MySQL
    password="1233",        # Ваш пароль до MySQL
    database="sql_kursova"  # Ім'я бази даних
)

cursor = conn.cursor()

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
        FOREIGN KEY (supply_id) REFERENCES suply(id),

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

conn.commit()

cursor.close()
conn.close()
print("З'єднання з базою даних закрито")
