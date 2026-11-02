
class User:
    def __init__(self, username, password_hash, is_active=True):
        self.username = username
        self.password_hash = password_hash
        self.is_active = is_active

    def verify_password(self, password):
        if self.password_hash == password:
            return True
        else:
            return False


class Administrator(User):
    def __init__(self, username, password_hash, is_active=True):
        super().__init__(username, password_hash, is_active)
        self.permissions = ["add_user", "delete_user", "change_settings"]

    def show_permissions(self):
        print("Права адміністратора:", self.permissions)


class RegularUser(User):
    def __init__(self, username, password_hash, is_active=True):
        super().__init__(username, password_hash, is_active)
        self.last_login = "Ще не входив"


class GuestUser(User):
    def __init__(self, username, password_hash, is_active=True):
        super().__init__(username, password_hash, is_active)
        self.access_level = "Обмежений доступ"


class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user
        print("Користувача додано:", user.username)

    def authenticate_user(self, username, password):
        if username in self.users:
            user = self.users[username]

            if user.is_active:
                if user.verify_password(password):
                    print("Вхід виконано успішно!")
                    return user
                else:
                    print("Неправильний пароль!")
            else:
                print("Обліковий запис неактивний!")
        else:
            print("Користувача не знайдено!")

        return None


system = AccessControl()

admin = Administrator("admin", "12345")
user1 = RegularUser("student", "11111")
guest = GuestUser("guest", "00000")

system.add_user(admin)
system.add_user(user1)
system.add_user(guest)

print()

result = system.authenticate_user("admin", "12345")

if result != None:
    print("Ім'я користувача:", result.username)
    print("Обліковий запис активний:", result.is_active)

print()

admin.show_permissions()
