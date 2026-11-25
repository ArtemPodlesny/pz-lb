import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
1

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    login TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
)
""")

conn.commit()



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def add_user():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    full_name = input("Введіть ПІБ: ")

    cursor.execute(
        "SELECT login FROM users WHERE login = ?",
        (login,)
    )

    if cursor.fetchone():
        print("Такий користувач вже існує!")
    else:
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (login, hash_password(password), full_name)
        )
        conn.commit()
        print("Користувача успішно додано!")



def update_password():
    login = input("Введіть логін: ")
    password = input("Введіть старий пароль: ")

    cursor.execute(
        "SELECT * FROM users WHERE login = ? AND password = ?",
        (login, hash_password(password))
    )

    if cursor.fetchone():
        new_password = input("Введіть новий пароль: ")

        cursor.execute(
            "UPDATE users SET password = ? WHERE login = ?",
            (hash_password(new_password), login)
        )
        conn.commit()
        print("Пароль успішно оновлено!")
    else:
        print("Неправильний логін або пароль!")



def authentication():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    cursor.execute(
        "SELECT full_name FROM users WHERE login = ? AND password = ?",
        (login, hash_password(password))
    )

    user = cursor.fetchone()

    if user:
        print("Вхід виконано успішно!")
        print("Вітаємо,", user[0])
    else:
        print("Неправильний логін або пароль!")



while True:
    print("\nМеню:")
    print("1. Додати користувача")
    print("2. Оновити пароль")
    print("3. Увійти в обліковий запис")
    print("0. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        update_password()
    elif choice == "3":
        authentication()
    elif choice == "0":
        break
    else:
        print("Невірний пункт меню!")

conn.close()