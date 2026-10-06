# Завдання 2 — Статистика продажів

sales = [
    {"продукт": "Ноутбук", "кількість": 2, "ціна": 30000},
    {"продукт": "Мишка", "кількість": 5, "ціна": 500},
    {"продукт": "Клавіатура", "кількість": 3, "ціна": 1200},
    {"продукт": "Ноутбук", "кількість": 1, "ціна": 30000},
    {"продукт": "Мишка", "кількість": 3, "ціна": 500}
]


def calculate_income(sales):
    income = {}

    for sale in sales:
        product = sale["продукт"]
        quantity = sale["кількість"]
        price = sale["ціна"]

        total = quantity * price

        if product not in income:
            income[product] = total
        else:
            income[product] += total

    return income


income = calculate_income(sales)

print("Загальний дохід:")
print(income)

big_income_products = []

for product in income:
    if income[product] > 1000:
        big_income_products.append(product)

print("Продукти, які принесли дохід більший ніж 1000:")
print(big_income_products)
