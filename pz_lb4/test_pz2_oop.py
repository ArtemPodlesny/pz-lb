import pytest

from pz2_oop import (
    User,
    Administrator,
    RegularUser,
    GuestUser,
    AccessControl,
)


# User.verify_password — два тести
def test_verify_password_correct():
    user = User("student", "secret")
    assert user.verify_password("secret") is True


def test_verify_password_incorrect():
    user = User("student", "secret")
    assert user.verify_password("wrong") is False


# Administrator.show_permissions — два тести
def test_administrator_has_expected_permissions():
    admin = Administrator("admin", "12345")
    assert admin.permissions == ["add_user", "delete_user", "change_settings"]


def test_show_permissions_prints_permissions(capsys):
    admin = Administrator("admin", "12345")
    admin.show_permissions()
    output = capsys.readouterr().out
    assert "Права адміністратора:" in output
    assert "add_user" in output


# AccessControl.add_user — два тести
def test_add_user_stores_user_by_username():
    system = AccessControl()
    user = RegularUser("student", "11111")

    system.add_user(user)

    assert system.users["student"] is user


def test_add_user_replaces_user_with_same_username():
    system = AccessControl()
    first_user = User("student", "11111")
    second_user = User("student", "22222")

    system.add_user(first_user)
    system.add_user(second_user)

    assert system.users["student"] is second_user


# AccessControl.authenticate_user — щонайменше два тести; тут перевірені всі гілки
def test_authenticate_user_returns_user_for_correct_credentials():
    system = AccessControl()
    user = RegularUser("student", "11111")
    system.add_user(user)

    assert system.authenticate_user("student", "11111") is user


def test_authenticate_user_returns_none_for_wrong_password():
    system = AccessControl()
    system.add_user(User("student", "11111"))

    assert system.authenticate_user("student", "wrong") is None


def test_authenticate_user_returns_none_for_inactive_account():
    system = AccessControl()
    system.add_user(User("student", "11111", is_active=False))

    assert system.authenticate_user("student", "11111") is None


def test_authenticate_user_returns_none_for_unknown_username():
    system = AccessControl()

    assert system.authenticate_user("unknown", "11111") is None


# Перевірка специфічних атрибутів класів-нащадків
def test_regular_user_initial_last_login():
    user = RegularUser("student", "11111")
    assert user.last_login == "Ще не входив"


def test_guest_user_access_level():
    guest = GuestUser("guest", "00000")
    assert guest.access_level == "Обмежений доступ"


def test_main_runs_demo_program(capsys):
    from pz2_oop import main

    main()
    output = capsys.readouterr().out
    assert "Вхід виконано успішно!" in output
    assert "Ім'я користувача: admin" in output
