# Моделі бази даних (Таблиці)

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class LoyaltyCard:
    def __init__(self, customer_id, bonus_points, issue_date):
        self.customer_id = customer_id
        self.bonus_points = bonus_points
        self.issue_date = issue_date

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class Order:
    def __init__(self, customer_id, order_date, total_amount, bonus_used):
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.bonus_used = bonus_used

class Transaction:
    def __init__(self, card_id, order_id, transaction_date, points_earned, points_spent):
        self.card_id = card_id
        self.order_id = order_id
        self.transaction_date = transaction_date
        self.points_earned = points_earned
        self.points_spent = points_spent
