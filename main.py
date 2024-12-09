from db import create_connection, create_tables
from utils import create_new_record, update_record, delete_record, view_table

def main():
    # Створення підключення до бази даних
    connection = create_connection()

    # Створення таблиць, якщо вони не існують
    create_tables(connection)

    # Показуємо користувачу доступні операції
    while True:
        print("\nДоступні операції:")
        print("1. Додати нового клієнта та бонусну картку")
        print("2. Оновити інформацію про клієнта")
        print("3. Видалити клієнта")
        print("4. Переглянути таблицю Customers")
        print("5. Переглянути таблицю LoyaltyCards")
        print("6. Вийти")

        choice = input("Виберіть операцію (1-6): ")

        if choice == '1':
            create_new_record(connection)
        elif choice == '2':
            update_record(connection)
        elif choice == '3':
            delete_record(connection)
        elif choice == '4':
            view_table(connection, "Customers")
        elif choice == '5':
            view_table(connection, "LoyaltyCards")
        elif choice == '6':
            print("Завершення роботи...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

    # Закриття підключення до бази даних
    connection.close()

# Виконання головної функції при запуску скрипта
if __name__ == "__main__":
    main()
