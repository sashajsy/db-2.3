import sqlite3
from datetime import datetime


# Функція для створення нового клієнта та його бонусної картки
def create_new_record(connection):
    cursor = connection.cursor()
    customer_name = input("Введіть ім'я клієнта: ")
    email = input("Введіть email клієнта: ")
    phone = input("Введіть телефон клієнта: ")
    bonus_points = int(input("Введіть кількість бонусних балів: "))

    # Додаємо нового клієнта
    cursor.execute("INSERT INTO Customers (Name, Email, Phone) VALUES (?, ?, ?)", (customer_name, email, phone))
    customer_id = cursor.lastrowid  # Отримуємо ID нового клієнта

    # Додаємо бонусну картку для нового клієнта
    cursor.execute("INSERT INTO LoyaltyCards (CustomerID, BonusPoints, IssueDate) VALUES (?, ?, ?)",
                   (customer_id, bonus_points, datetime.now().strftime('%Y-%m-%d')))

    connection.commit()
    print(f"Новий запис для клієнта {customer_name} успішно додано.")


# Функція для видалення записів з таблиці Customers
def delete_record(connection):
    cursor = connection.cursor()
    customer_name = input("Введіть ім'я клієнта, якого потрібно видалити: ")

    # Видаляємо дані з таблиці Customers, це призведе до каскадного видалення
    cursor.execute("DELETE FROM Customers WHERE Name = ?", (customer_name,))
    connection.commit()
    print(f"Записи клієнта {customer_name} успішно видалені.")


# Функція для оновлення запису
def update_record(connection):
    cursor = connection.cursor()
    old_name = input("Введіть ім'я клієнта, яке потрібно змінити: ")
    new_name = input("Введіть нове ім'я клієнта: ")

    cursor.execute("UPDATE Customers SET Name = ? WHERE Name = ?", (new_name, old_name))
    connection.commit()
    print(f"Ім'я клієнта {old_name} змінено на {new_name}.")


# Функція для відображення всіх даних з таблиці
def view_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"Дані з таблиці {table_name}:")
    for row in rows:
        print(row)
    print()
