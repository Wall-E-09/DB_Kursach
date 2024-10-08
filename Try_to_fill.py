import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1233",
    database="sql_kursova"
)

cursor = conn.cursor()
# Вставка даних у таблицю license_type
cursor.execute("INSERT IGNORE INTO license_type (license_type) VALUES ('Фармацевтична ліцензія')")  # Ліцензія на фармацевтичну діяльність
cursor.execute("INSERT IGNORE INTO license_type (license_type) VALUES ('Ліцензія на імпорт медичних товарів')")  # Ліцензія на імпорт
cursor.execute("INSERT IGNORE INTO license_type (license_type) VALUES ('Ліцензія на виробництво медичних препаратів')")  # Ліцензія на виробництво
cursor.execute("INSERT IGNORE INTO license_type (license_type) VALUES ('Ліцензія на експорт медичних товарів')")  # Ліцензія на експорт
cursor.execute("INSERT IGNORE INTO license_type (license_type) VALUES ('Ліцензія на роздрібну торгівлю медичними препаратами')")  # Ліцензія на роздрібну торгівлю

# Вставка даних у таблицю drug_types
cursor.execute("INSERT IGNORE INTO drug_types (type_name) VALUES ('Антибіотики')")  # Тип ліків
cursor.execute("INSERT IGNORE INTO drug_types (type_name) VALUES ('Анальгетики')")  # Знеболювальні
cursor.execute("INSERT IGNORE INTO drug_types (type_name) VALUES ('Противірусні засоби')")  # Противірусні препарати
cursor.execute("INSERT IGNORE INTO drug_types (type_name) VALUES ('Протизапальні засоби')")  # Протизапальні
cursor.execute("INSERT IGNORE INTO drug_types (type_name) VALUES ('Вітаміни')")  # Вітамінні добавки

# Вставка даних у таблицю components
cursor.execute("INSERT IGNORE INTO components (components, type_of_component, total_amount, price) VALUES ('Амоксицилін', 1, 500, 50.00)")  # Компонент
cursor.execute("INSERT IGNORE INTO components (components, type_of_component, total_amount, price) VALUES ('Ібупрофен', 2, 300, 30.00)")  # Компонент
cursor.execute("INSERT IGNORE INTO components (components, type_of_component, total_amount, price) VALUES ('Аспірин', 2, 400, 40.00)")  # Компонент
cursor.execute("INSERT IGNORE INTO components (components, type_of_component, total_amount, price) VALUES ('Парацетамол', 1, 600, 60.00)")  # Компонент
cursor.execute("INSERT IGNORE INTO components (components, type_of_component, total_amount, price) VALUES ('Вітамін C', 2, 700, 70.00)")  # Компонент

# Вставка даних у таблицю type_of_component
cursor.execute("INSERT IGNORE INTO type_of_component (component_type) VALUES ('Хімічна речовина')")  # Тип компонента
cursor.execute("INSERT IGNORE INTO type_of_component (component_type) VALUES ('Природний компонент')")  # Тип компонента
cursor.execute("INSERT IGNORE INTO type_of_component (component_type) VALUES ('Синтетичний компонент')")  # Тип компонента
cursor.execute("INSERT IGNORE INTO type_of_component (component_type) VALUES ('Біологічний компонент')")  # Тип компонента
cursor.execute("INSERT IGNORE INTO type_of_component (component_type) VALUES ('Мінеральний компонент')")  # Тип компонента

# Вставка даних у таблицю method_of_application
cursor.execute("INSERT IGNORE INTO method_of_application (method) VALUES ('Орально')")  # Спосіб застосування
cursor.execute("INSERT IGNORE INTO method_of_application (method) VALUES ('Інєкція')")  # Спосіб застосування
cursor.execute("INSERT IGNORE INTO method_of_application (method) VALUES ('Назально')")  # Спосіб застосування
cursor.execute("INSERT IGNORE INTO method_of_application (method) VALUES ('Ректально')")  # Спосіб застосування
cursor.execute("INSERT IGNORE INTO method_of_application (method) VALUES ('Трансдермально')")  # Спосіб застосування

# Вставка даних у таблицю drug_characteristics
cursor.execute("INSERT IGNORE INTO drug_characteristics (characteristics) VALUES ('Швидкодіючий')")  # Характеристика
cursor.execute("INSERT IGNORE INTO drug_characteristics (characteristics) VALUES ('Тривалий вплив')")  # Характеристика
cursor.execute("INSERT IGNORE INTO drug_characteristics (characteristics) VALUES ('Без побічних ефектів')")  # Характеристика
cursor.execute("INSERT IGNORE INTO drug_characteristics (characteristics) VALUES ('Підходить для дітей')")  # Характеристика
cursor.execute("INSERT IGNORE INTO drug_characteristics (characteristics) VALUES ('Підходить для вагітних')")  # Характеристика

# Вставка даних у таблицю type_of_packaging
cursor.execute("INSERT IGNORE INTO type_of_packaging (type_of_packaging, number_in_pack) VALUES ('Блістер', 10)")  # Упаковка
cursor.execute("INSERT IGNORE INTO type_of_packaging (type_of_packaging, number_in_pack) VALUES ('Флакон', 1)")  # Упаковка
cursor.execute("INSERT IGNORE INTO type_of_packaging (type_of_packaging, number_in_pack) VALUES ('Тюбик', 1)")  # Упаковка
cursor.execute("INSERT IGNORE INTO type_of_packaging (type_of_packaging, number_in_pack) VALUES ('Пакет', 5)")  # Упаковка
cursor.execute("INSERT IGNORE INTO type_of_packaging (type_of_packaging, number_in_pack) VALUES ('Коробка', 20)")  # Упаковка

# Вставка даних у таблицю customers
cursor.execute("""INSERT IGNORE INTO customers (customer_first_name, customer_last_name, name_of_company_or_organization, 
    customer_address_office_or_storage, customer_phone_number, customer_email, customer_license_number, 
    customer_bank_account_number, customer_license_type) 
    VALUES ('Олег', 'Шевченко', 'ТОВ "Фармацентр"', 'вул. Незалежності, 15, Київ', '380671234567', 
    'shevchenko@pharma.ua', 'Л-12345', 'UA1234567890', 1)""")

cursor.execute("""INSERT IGNORE INTO customers (customer_first_name, customer_last_name, name_of_company_or_organization, 
    customer_address_office_or_storage, customer_phone_number, customer_email, customer_license_number, 
    customer_bank_account_number, customer_license_type) 
    VALUES ('Ірина', 'Гончарук', 'ТОВ "Медсервіс"', 'вул. Лесі Українки, 23, Львів', '380987654321', 
    'honcharuk@medservis.ua', 'Л-67890', 'UA0987654321', 2)""")

cursor.execute("""INSERT IGNORE INTO customers (customer_first_name, customer_last_name, name_of_company_or_organization, 
    customer_address_office_or_storage, customer_phone_number, customer_email, customer_license_number, 
    customer_bank_account_number, customer_license_type) 
    VALUES ('Василь', 'Ковальчук', 'ТОВ "Медіком"', 'вул. Петра Могили, 45, Одеса', '380123456789', 
    'kovalchyk@medicom.ua', 'Л-54321', 'UA6789054321', 1)""")

# Вставка даних у таблицю products
cursor.execute("""INSERT IGNORE INTO products (product_name, price, description_instruktsiya, components_id, drug_types_id, 
    method_of_application_id, drug_characteristics_id, type_of_packaging_id) 
    VALUES ('Парацетамол', 80.00, 'Жарознижувальний та знеболювальний засіб', 4, 2, 1, 1, 1)""")
cursor.execute("""INSERT IGNORE INTO products (product_name, price, description_instruktsiya, components_id, drug_types_id, 
    method_of_application_id, drug_characteristics_id, type_of_packaging_id) 
    VALUES ('Цефтріаксон', 200.00, 'Антибіотик для інєкцій', 1, 1, 1, 1, 1)""")

# Вставка даних у таблицю suppliers
cursor.execute("""INSERT IGNORE INTO supplier (supplier_first_name, supplier_last_name, name_of_company_or_organization, 
    supplier_address_office_or_storage, supplier_phone_number, supplier_email, supplier_license_number, 
    supplier_bank_account_number, supplier_license_type) 
    VALUES ('Іван', 'Петренко', 'ТОВ "Медпостач"', 'вул. Січових Стрільців, 20, Львів', '380501234571', 
    'petrenko@medpostach.ua', 'Л-4444', 'UA9876543211', 2)""")
cursor.execute("""INSERT IGNORE INTO supplier (supplier_first_name, supplier_last_name, name_of_company_or_organization, 
    supplier_address_office_or_storage, supplier_phone_number, supplier_email, supplier_license_number, 
    supplier_bank_account_number, supplier_license_type) 
    VALUES ('Олена', 'Коваль', 'ТОВ "Фармпостач"', 'вул. Володимирська, 15, Київ', '380501234572', 
    'koval@pharmpostach.ua', 'Л-5555', 'UA9876543212', 3)""")
cursor.execute("""INSERT IGNORE INTO supplier (supplier_first_name, supplier_last_name, name_of_company_or_organization, 
    supplier_address_office_or_storage, supplier_phone_number, supplier_email, supplier_license_number, 
    supplier_bank_account_number, supplier_license_type) 
    VALUES ('Сергій', 'Мельник', 'ТОВ "Медснаб"', 'вул. Пушкіна, 25, Одеса', '380501234573', 
    'melnik@medsnab.ua', 'Л-6666', 'UA9876543213', 1)""")

# Вставка даних у таблицю orders
cursor.execute("""INSERT IGNORE INTO orders (product_id, customers_id, carriers_id, total_price, total_amount, 
    order_date, order_status, date_of_sending, approx_date_of_arrival, date_of_arrival, order_description) 
    VALUES (1, 1, 1, 150.00, 10, '2024-01-01', TRUE, '2024-01-02', '2024-01-05', '2024-01-06', 'Замовлення антибіотиків')""")
cursor.execute("""INSERT IGNORE INTO orders (product_id, customers_id, carriers_id, total_price, total_amount, 
    order_date, order_status, date_of_sending, approx_date_of_arrival, date_of_arrival, order_description) 
    VALUES (2, 2, 2, 300.00, 20, '2024-02-01', TRUE, '2024-02-02', '2024-02-05', '2024-02-06', 'Замовлення знеболювальних засобів')""")
cursor.execute("""INSERT IGNORE INTO orders (product_id, customers_id, carriers_id, total_price, total_amount, 
    order_date, order_status, date_of_sending, approx_date_of_arrival, date_of_arrival, order_description) 
    VALUES (3, 3, 3, 400.00, 30, '2024-03-01', TRUE, '2024-03-02', '2024-03-05', '2024-03-06', 'Замовлення вітамінів')""")
cursor.execute("""INSERT IGNORE INTO orders (product_id, customers_id, carriers_id, total_price, total_amount, 
    order_date, order_status, date_of_sending, approx_date_of_arrival, date_of_arrival, order_description) 
    VALUES (4, 4, 4, 500.00, 40, '2024-04-01', TRUE, '2024-04-02', '2024-04-05', '2024-04-06', 'Замовлення жарознижувальних засобів')""")

# Вставка даних у таблицю availability
cursor.execute("""INSERT IGNORE INTO availability (product_id, availability_status, total_amount, availability_in_stock, availability_in_order) 
    VALUES (1, TRUE, 50, TRUE, FALSE)""")
cursor.execute("""INSERT IGNORE INTO availability (product_id, availability_status, total_amount, availability_in_stock, availability_in_order) 
    VALUES (2, TRUE, 30, TRUE, TRUE)""")
cursor.execute("""INSERT IGNORE INTO availability (product_id, availability_status, total_amount, availability_in_stock, availability_in_order) 
    VALUES (3, TRUE, 60, TRUE, FALSE)""")
cursor.execute("""INSERT IGNORE INTO availability (product_id, availability_status, total_amount, availability_in_stock, availability_in_order) 
    VALUES (4, TRUE, 70, TRUE, TRUE)""")
cursor.execute("""INSERT IGNORE INTO availability (product_id, availability_status, total_amount, availability_in_stock, availability_in_order) 
    VALUES (5, TRUE, 80, TRUE, FALSE)""")

# Вставка даних у таблицю employees
cursor.execute("""INSERT IGNORE INTO employees (employee_first_name, employee_last_name, employee_phone_number, 
    employee_income, employee_experience, fabric_id, storage_id, workplace, directory_of_occupations_id) 
    VALUES ('Марія', 'Іванова', '380661112224', 25000.00, 6, 2, 2, 'factory', 2)""")
cursor.execute("""INSERT IGNORE INTO employees (employee_first_name, employee_last_name, employee_phone_number, 
    employee_income, employee_experience, fabric_id, storage_id, workplace, directory_of_occupations_id) 
    VALUES ('Петро', 'Сидоренко', '380661112225', 30000.00, 7, 3, 3, 'factory', 3)""")
cursor.execute("""INSERT IGNORE INTO employees (employee_first_name, employee_last_name, employee_phone_number, 
    employee_income, employee_experience, fabric_id, storage_id, workplace, directory_of_occupations_id) 
    VALUES ('Олександр', 'Кравченко', '380661112226', 35000.00, 8, 4, 4, 'factory', 4)""")

# Вставка даних у таблицю directory_of_occupations
cursor.execute("""INSERT IGNORE INTO directory_of_occupations (occupation, qualification, salary) 
    VALUES ('Лаборант', 'Вища освіта', 20000.00)""")
cursor.execute("""INSERT IGNORE INTO directory_of_occupations (occupation, qualification, salary) 
    VALUES ('Менеджер', 'Вища освіта', 30000.00)""")
cursor.execute("""INSERT IGNORE INTO directory_of_occupations (occupation, qualification, salary) 
    VALUES ('Водій', 'Середня освіта', 18000.00)""")

# Вставка даних у таблицю storage
cursor.execute("""INSERT IGNORE INTO storage (storage_name, storage_address, storage_phone_number, storage_email, 
    storage_license_number, square_of_storage, storage_capacity, temperature_conditions, number_of_employees, 
    special_conditions, employees_id, storage_boss_id, storage_license_type_id) 
    VALUES ('Склад Фарма 2', 'вул. Лесі Українки, 50, Львів', '380441234568', 'storage2@pharma.ua', 
    'Л-8888', 200.0, 2000, '15-25°C', 60, 'Температурний контроль', 2, 2, 2)""")
cursor.execute("""INSERT IGNORE INTO storage (storage_name, storage_address, storage_phone_number, storage_email, 
    storage_license_number, square_of_storage, storage_capacity, temperature_conditions, number_of_employees, 
    special_conditions, employees_id, storage_boss_id, storage_license_type_id) 
    VALUES ('Склад Фарма 3', 'вул. Грушевського, 30, Одеса', '380441234569', 'storage3@pharma.ua', 
    'Л-7777', 300.0, 3000, '15-25°C', 70, 'Температурний контроль', 3, 3, 3)""")
cursor.execute("""INSERT IGNORE INTO storage (storage_name, storage_address, storage_phone_number, storage_email, 
    storage_license_number, square_of_storage, storage_capacity, temperature_conditions, number_of_employees, 
    special_conditions, employees_id, storage_boss_id, storage_license_type_id) 
    VALUES ('Склад Фарма 4', 'вул. Пушкіна, 40, Харків', '380441234570', 'storage4@pharma.ua', 
    'Л-6666', 400.0, 4000, '15-25°C', 80, 'Температурний контроль', 4, 4, 4)""")

# Вставка даних у таблицю carriers
cursor.execute("""INSERT IGNORE INTO carriers (carrier_first_name, carrier_last_name, name_of_company_or_organization, 
    carrier_phone_number, carrier_license_number, customer_id, supplier_id, orders_id, supply_id, 
    storage_id, carrier_license_type_id) 
    VALUES ('Олексій', 'Сидоренко', 'ТОВ "Експрес Доставка"', '380501234574', 'Л-9999', 2, 2, 2, 2, 2, 2)""")
cursor.execute("""INSERT IGNORE INTO carriers (carrier_first_name, carrier_last_name, name_of_company_or_organization, 
    carrier_phone_number, carrier_license_number, customer_id, supplier_id, orders_id, supply_id, 
    storage_id, carrier_license_type_id) 
    VALUES ('Ірина', 'Ковальчук', 'ТОВ "Швидка Пошта"', '380501234575', 'Л-7777', 3, 3, 3, 3, 3, 3)""")
cursor.execute("""INSERT IGNORE INTO carriers (carrier_first_name, carrier_last_name, name_of_company_or_organization, 
    carrier_phone_number, carrier_license_number, customer_id, supplier_id, orders_id, supply_id, 
    storage_id, carrier_license_type_id) 
    VALUES ('Віктор', 'Мельник', 'ТОВ "Нова Пошта"', '380501234576', 'Л-6666', 4, 4, 4, 4, 4, 4)""")

# Вставка даних у таблицю fabric
cursor.execute("""INSERT IGNORE INTO fabric (fabric_name, fabric_address, fabric_type) 
    VALUES ('ТОВ "Фармафабрика"', 'вул. Котляревського, 15, Харків', 'Виробництво медичних препаратів')""")
cursor.execute("""INSERT IGNORE INTO fabric (fabric_name, fabric_address, fabric_type) 
    VALUES ('ТОВ "ФармаГруп"', 'вул. Грушевського, 20, Київ', 'Виробництво ліків')""")
cursor.execute("""INSERT IGNORE INTO fabric (fabric_name, fabric_address, fabric_type) 
    VALUES ('ТОВ "Медичні Технології"', 'вул. Тараса Шевченка, 45, Львів', 'Виробництво медичних засобів')""")

# Вставка даних у таблицю suply
cursor.execute("""INSERT IGNORE INTO suply (components_id, supplier_id, total_price, total_amount, supply_date, supply_status, 
    date_of_sending, approx_date_of_arrival, date_of_arrival, other_description) 
    VALUES (1, 1, 2500.00, 100, '2024-01-15', TRUE, '2024-01-16', '2024-01-20', '2024-01-22', 'Постачання амоксициліну')""")
cursor.execute("""INSERT IGNORE INTO suply (components_id, supplier_id, total_price, total_amount, supply_date, supply_status, 
    date_of_sending, approx_date_of_arrival, date_of_arrival, other_description) 
    VALUES (2, 2, 1500.00, 200, '2024-02-10', TRUE, '2024-02-11', '2024-02-15', '2024-02-17', 'Постачання ібупрофену')""")
cursor.execute("""INSERT IGNORE INTO suply (components_id, supplier_id, total_price, total_amount, supply_date, supply_status, 
    date_of_sending, approx_date_of_arrival, date_of_arrival, other_description) 
    VALUES (3, 3, 3000.00, 150, '2024-03-05', TRUE, '2024-03-06', '2024-03-10', '2024-03-12', 'Постачання аспірину')""")


# Фіксація змін
conn.commit()

# Закриття з'єднання
cursor.close()
conn.close()

print("Дані успішно додані до бази даних")


conn.commit()


# Закриття з'єднання
cursor.close()
conn.close()

print("Дані успішно додані до бази")
