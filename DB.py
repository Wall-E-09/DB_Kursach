import mysql.connector


def create_database(cursor):
    """Function to create tables in the database."""
    try:
            # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fabric (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fabric_name VARCHAR(255) NOT NULL,
                fabric_address VARCHAR(255) NOT NULL,
                fabric_type ENUM('Фармацевтична', 'Хімічна', 'Біологічна') NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                description_instruktsiya TEXT,
                components_id INT,
                drug_types_id INT,
                method_of_application ENUM('Перорально', 'Інєкційно', 'Назально') NOT NULL,
                drug_characteristics ENUM('Швидкодіючий', 'Довготривалий') NOT NULL,
                type_of_packaging ENUM('Блістер', 'Флакон') NOT NULL,
                FOREIGN KEY (components_id) REFERENCES components(id),
                FOREIGN KEY (drug_types_id) REFERENCES drug_types(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS availability (
                product_id INT,
                availability_status BOOLEAN,
                total_amount INT,
                availability_in_stock BOOLEAN,
                availability_in_order BOOLEAN,
                FOREIGN KEY (product_id) REFERENCES products(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_id INT,
                customers_id INT,
                carriers_id INT,
                total_price DECIMAL(10,2),
                total_amount INT,
                order_date DATE,
                order_status BOOLEAN,
                date_of_sending DATE,
                approx_date_of_arrival DATE,
                date_of_arrival DATE,
                order_description TEXT,
                FOREIGN KEY (product_id) REFERENCES products(id),
                FOREIGN KEY (customers_id) REFERENCES customers(id),
                FOREIGN KEY (carriers_id) REFERENCES carriers(id)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS supply (
                id INT AUTO_INCREMENT PRIMARY KEY,
                components_id INT,
                supplier_id INT,
                total_price DECIMAL(10,2),
                total_amount INT,
                supply_date DATE,
                supply_status BOOLEAN,
                date_of_sending DATE,
                approx_date_of_arrival DATE,
                date_of_arrival DATE,
                other_description TEXT,
                FOREIGN KEY (components_id) REFERENCES components(id),
                FOREIGN KEY (supplier_id) REFERENCES supplier(id)
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
                supplier_license_type ENUM('Тип 1', 'Тип 2') NOT NULL
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
                customer_license_type ENUM('Тип 1', 'Тип 2') NOT NULL
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
                carrier_address VARCHAR(255) NOT NULL,
                supplier_id INT,
                orders_id INT,
                supply_id INT,
                storage_id INT,
                carrier_license_type ENUM('Тип 1', 'Тип 2') NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (supplier_id) REFERENCES supplier(id),
                FOREIGN KEY (orders_id) REFERENCES orders(id),
                FOREIGN KEY (supply_id) REFERENCES supply(id)
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
                storage_boss_id INT,
                storage_license_type ENUM('Тип 1', 'Тип 2') NOT NULL,
                FOREIGN KEY (employees_id) REFERENCES employees(id),
                FOREIGN KEY (storage_boss_id) REFERENCES employees(id)
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
                storage_id INT,
                workplace ENUM('factory', 'storage') NOT NULL,
                directory_of_occupations_id INT,
                FOREIGN KEY (fabric_id) REFERENCES fabric(id),
                FOREIGN KEY (storage_id) REFERENCES storage(id),
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
                type_of_component ENUM('Активний', 'Допоміжний') NOT NULL,
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
        print("Tables created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating tables: {e}")

def insert_data(cursor):
    """Function to insert data into the database tables."""
    try:
        print("Data inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")

        
def user_input(cursor):
    print("1. Додати новий продукт")
    print("2. Додати нове замовлення")  
    print("3. Додати нового постачальника")
    print("4. Додати нового клієнта")
    print("5. Додати нового перевізника")
    print("6. Додати новий склад")
    print("7. Додати нового працівника")
    print("8. Додати нову посаду")
    print("9. Додати новий компонент")
    print("10. Додати новий тип ліків")
    print("11. Додати новий тип компоненту")
    print("12. Додати новий метод застосування")
    print("13. Додати нову характеристику ліків")
    print("14. Додати новий тип упаковки")
    print("15. Додати новий етап відправлення")
    print("16. Додати новий тип ліцензії")
    print("17. Вийти")
    choice = int(input("Виберіть опцію: "))
    if choice == 1:
    # Adding a product
        product_name = input("Введіть назву продукту: ")
        price = float(input("Введіть ціну продукту: "))
        description_instruktsiya = input("Введіть інструкцію: ")
        components_id = int(input("Введіть ID компоненту: "))
        drug_types_id = int(input("Введіть ID типу ліків: "))
        method_of_application_id = int(input("Введіть ID методу застосування: "))
        drug_characteristics_id = int(input("Введіть ID характеристики ліків: "))
        type_of_packaging_id = int(input("Введіть ID типу упаковки: "))
        
        cursor.execute('''
            INSERT INTO products (
                product_name, price, description_instruktsiya, components_id, 
                drug_types_id, method_of_application_id, drug_characteristics_id, type_of_packaging_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            product_name, price, description_instruktsiya, components_id, 
            drug_types_id, method_of_application_id, drug_characteristics_id, type_of_packaging_id
        ))
        print("Продукт додано успішно.")

    elif choice == 2:
        # Adding an order
        product_id = int(input("Введіть ID продукту: "))
        customers_id = int(input("Введіть ID клієнта: "))
        carriers_id = int(input("Введіть ID перевізника: "))
        total_price = float(input("Введіть загальну ціну: "))
        total_amount = int(input("Введіть загальну кількість: "))
        order_date = input("Введіть дату замовлення: ")
        order_status = bool(input("Введіть статус замовлення (0 або 1): "))
        date_of_sending = input("Введіть дату відправлення: ")
        approx_date_of_arrival = input("Введіть приблизну дату прибуття: ")
        date_of_arrival = input("Введіть дату прибуття: ")
        order_description = input("Введіть опис замовлення: ")

        cursor.execute('''
            INSERT INTO orders (
                product_id, customers_id, carriers_id, total_price, 
                total_amount, order_date, order_status, date_of_sending, 
                approx_date_of_arrival, date_of_arrival, order_description
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            product_id, customers_id, carriers_id, total_price, 
            total_amount, order_date, order_status, date_of_sending, 
            approx_date_of_arrival, date_of_arrival, order_description
        ))
        print("Замовлення додано успішно.")

    elif choice == 3:
        # Adding a supplier
        supplier_first_name = input("Введіть ім'я постачальника: ")
        supplier_last_name = input("Введіть прізвище постачальника: ")
        name_of_company_or_organization = input("Введіть назву компанії або організації: ")
        supplier_address_office_or_storage = input("Введіть адресу офісу або складу постачальника: ")
        supplier_phone_number = input("Введіть номер телефону постачальника: ")
        supplier_email = input("Введіть електронну пошту постачальника: ")
        supplier_license_number = input("Введіть номер ліцензії постачальника: ")
        supplier_bank_account_number = input("Введіть номер банківського рахунку постачальника: ")
        supplier_license_type = int(input("Введіть ID типу ліцензії постачальника: "))

        cursor.execute('''
            INSERT INTO supplier (
                supplier_first_name, supplier_last_name, name_of_company_or_organization, 
                supplier_address_office_or_storage, supplier_phone_number, supplier_email, 
                supplier_license_number, supplier_bank_account_number, supplier_license_type
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            supplier_first_name, supplier_last_name, name_of_company_or_organization, 
            supplier_address_office_or_storage, supplier_phone_number, supplier_email, 
            supplier_license_number, supplier_bank_account_number, supplier_license_type
        ))
        print("Постачальника додано успішно.")

    elif choice == 4:
        # Adding a customer
        customer_first_name = input("Введіть ім'я клієнта: ")
        customer_last_name = input("Введіть прізвище клієнта: ")
        name_of_company_or_organization = input("Введіть назву компанії або організації клієнта: ")
        customer_address_office_or_storage = input("Введіть адресу офісу або складу клієнта: ")
        customer_phone_number = input("Введіть номер телефону клієнта: ")
        customer_email = input("Введіть електронну пошту клієнта: ")
        customer_license_number = input("Введіть номер ліцензії клієнта: ")
        customer_bank_account_number = input("Введіть номер банківського рахунку клієнта: ")
        customer_license_type = int(input("Введіть ID типу ліцензії клієнта: "))

        cursor.execute('''
            INSERT INTO customers (
                customer_first_name, customer_last_name, name_of_company_or_organization, 
                customer_address_office_or_storage, customer_phone_number, customer_email, 
                customer_license_number, customer_bank_account_number, customer_license_type
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            customer_first_name, customer_last_name, name_of_company_or_organization, 
            customer_address_office_or_storage, customer_phone_number, customer_email, 
            customer_license_number, customer_bank_account_number, customer_license_type
        ))
        print("Клієнта додано успішно.")

    elif choice == 5:
        carrier_first_name = input("Введіть ім'я перевізника: ")
        carrier_last_name = input("Введіть прізвище перевізника: ")
        name_of_company_or_organization = input("Введіть назву компанії або організації перевізника: ")
        carrier_phone_number = input("Введіть номер телефону перевізника: ")
        carrier_license_number = input("Введіть номер ліцензії перевізника: ")
        customer_id = int(input("Введіть ID клієнта: "))
        carrier_address = input("Введіть адресу перевізника: ")
        supplier_id = int(input("Введіть ID постачальника: "))
        orders_id = int(input("Введіть ID замовлення: "))
        supply_id = int(input("Введіть ID постачання: "))
        storage_id = int(input("Введіть ID складу: "))
        carrier_license_type_id = int(input("Введіть ID типу ліцензії перевізника: "))
        
        cursor.execute('''
            INSERT INTO carriers (
                carrier_first_name, carrier_last_name, name_of_company_or_organization, 
                carrier_phone_number, carrier_license_number, customer_id, carrier_address, 
                supplier_id, orders_id, supply_id, storage_id, carrier_license_type_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            carrier_first_name, carrier_last_name, name_of_company_or_organization, 
            carrier_phone_number, carrier_license_number, customer_id, carrier_address, 
            supplier_id, orders_id, supply_id, storage_id, carrier_license_type_id
        ))
        
        print("Перевізника додано успішно.")

    elif choice == 6:
        storage_name = input("Введіть назву складу: ")
        storage_address = input("Введіть адресу складу: ")
        storage_phone_number = input("Введіть номер телефону складу: ")
        storage_email = input("Введіть електронну пошту складу: ")
        storage_license_number = input("Введіть номер ліцензії складу: ")
        square_of_storage = float(input("Введіть площу складу: "))
        storage_capacity = int(input("Введіть місткість складу: "))
        temperature_conditions = input("Введіть температурні умови: ")
        number_of_employees = int(input("Введіть кількість працівників: "))
        special_conditions = input("Введіть особливі умови: ")
        employees_id = int(input("Введіть ID працівника: "))
        storage_boss_id = int(input("Введіть ID начальника складу: "))
        storage_license_type_id = int(input("Введіть ID типу ліцензії складу: "))
        
        cursor.execute('''
            INSERT INTO storage (
                storage_name, storage_address, storage_phone_number, storage_email, 
                storage_license_number, square_of_storage, storage_capacity, 
                temperature_conditions, number_of_employees, special_conditions, 
                employees_id, storage_boss_id, storage_license_type_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (storage_name, storage_address, storage_phone_number, storage_email, 
            storage_license_number, square_of_storage, storage_capacity, 
            temperature_conditions, number_of_employees, special_conditions, 
            employees_id, storage_boss_id, storage_license_type_id))
        
        print("Склад додано успішно.")

    elif choice == 7:
        employee_first_name = input("Введіть ім'я працівника: ")
        employee_last_name = input("Введіть прізвище працівника: ")
        employee_phone_number = input("Введіть номер телефону працівника: ")
        employee_income = float(input("Введіть дохід працівника: "))
        employee_experience = int(input("Введіть досвід працівника: "))
        fabric_id = int(input("Введіть ID фабрики: "))
        storage_id = int(input("Введіть ID складу: "))
        workplace = input("Введіть місце роботи (factory/storage): ")
        directory_of_occupations_id = int(input("Введіть ID посади: "))
        
        cursor.execute('''
            INSERT INTO employees (
                employee_first_name, employee_last_name, employee_phone_number, 
                employee_income, employee_experience, fabric_id, storage_id, 
                workplace, directory_of_occupations_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (employee_first_name, employee_last_name, employee_phone_number, 
            employee_income, employee_experience, fabric_id, storage_id, 
            workplace, directory_of_occupations_id))
        
        print("Працівника додано успішно.")

    elif choice == 8:
        occupation = input("Введіть назву посади: ")
        qualification = input("Введіть кваліфікацію: ")
        salary = float(input("Введіть зарплату: "))
        
        cursor.execute('''
            INSERT INTO directory_of_occupations (occupation, qualification, salary)
            VALUES (%s, %s, %s)
        ''', (occupation, qualification, salary))
        
        print("Посаду додано успішно.")

    elif choice == 9:
        components = input("Введіть назву компоненту: ")
        type_of_component = int(input("Введіть ID типу компоненту: "))
        total_amount = int(input("Введіть загальну кількість: "))
        price = float(input("Введіть ціну: "))
        
        cursor.execute('''
            INSERT INTO components (components, type_of_component, total_amount, price)
            VALUES (%s, %s, %s, %s)
        ''', (components, type_of_component, total_amount, price))
        
        print("Компонент додано успішно.")

    elif choice == 10:
        type_name = input("Введіть назву типу ліків: ")
        
        cursor.execute('''
            INSERT INTO drug_types (type_name)
            VALUES (%s)
        ''', (type_name,))
        
        print("Тип ліків додано успішно.")

    elif choice == 11:
        component_type = input("Введіть тип компоненту: ")
        
        cursor.execute('''
            INSERT INTO type_of_component (component_type)
            VALUES (%s)
        ''', (component_type,))
        
        print("Тип компоненту додано успішно.")

    elif choice == 12:
        method = input("Введіть метод застосування: ")
        
        cursor.execute('''
            INSERT INTO method_of_application (method)
            VALUES (%s)
        ''', (method,))
        
        print("Метод застосування додано успішно.")

    elif choice == 13:
        characteristics = input("Введіть характеристику ліків: ")
        
        cursor.execute('''
            INSERT INTO drug_characteristics (characteristics)
            VALUES (%s)
        ''', (characteristics,))
        
        print("Характеристику ліків додано успішно.")

    elif choice == 14:
        type_of_packaging = input("Введіть тип упаковки: ")
        number_in_pack = int(input("Введіть кількість в упаковці: "))
        
        cursor.execute('''
            INSERT INTO type_of_packaging (type_of_packaging, number_in_pack)
            VALUES (%s, %s)
        ''', (type_of_packaging, number_in_pack))
        
        print("Тип упаковки додано успішно.")

    elif choice == 15:
        stage_of_sending = input("Введіть етап відправлення: ")
        
        cursor.execute('''
            INSERT INTO stage_of_sending (stage_of_sending)
            VALUES (%s)
        ''', (stage_of_sending,))
        
        print("Етап відправлення додано успішно.")

    elif choice == 16:
        license_type = input("Введіть тип ліцензії: ")
        
        cursor.execute('''
            INSERT INTO license_type (license_type)
            VALUES (%s)
        ''', (license_type,))
        
        print("Тип ліцензії додано успішно.")

    elif choice == 17:
        print("Вихід з програми.")
        return

    else:
        print("Невірний вибір. Спробуйте ще раз.")


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

        # User input
        user_input(cursor)

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