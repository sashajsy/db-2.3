import sqlite3

# Функція для створення підключення до бази даних
def create_connection():
    connection = sqlite3.connect('loyalty_system.db')
    return connection

# Функція для створення таблиць у базі даних
def create_tables(connection):
    cursor = connection.cursor()

    # Створення таблиці клієнтів
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Email TEXT,
        Phone TEXT
    )
    """)

    # Створення таблиці бонусних карток, пов'язаної з таблицею Customers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LoyaltyCards (
        CardID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        BonusPoints INTEGER DEFAULT 0,
        IssueDate DATE,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
    )
    """)

    # Створення таблиці товарів
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT,
        Price REAL
    )
    """)

    # Створення таблиці замовлень, пов'язаної з таблицею Customers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        OrderDate DATE,
        TotalAmount REAL,
        BonusUsed INTEGER,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
    )
    """)

    # Створення таблиці транзакцій, пов'язаної з таблицями LoyaltyCards та Orders
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        CardID INTEGER,
        OrderID INTEGER,
        TransactionDate DATE,
        PointsEarned INTEGER,
        PointsSpent INTEGER,
        FOREIGN KEY (CardID) REFERENCES LoyaltyCards(CardID),
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    )
    """)
    connection.commit()  # Зберігаємо зміни в базі даних
