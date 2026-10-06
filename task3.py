# Завдання 3 — Система управління задачами

tasks = {
    "Зробити лабораторну": "в процесі",
    "Вивчити Python": "очікує",
    "Здати ПЗ": "виконано"
}


def add_task(name, status):
    tasks[name] = status


def delete_task(name):
    if name in tasks:
        del tasks[name]


def change_status(name, new_status):
    if name in tasks:
        tasks[name] = new_status


add_task("Зробити домашнє завдання", "очікує")

delete_task("Здати ПЗ")

change_status("Вивчити Python", "в процесі")

waiting_tasks = []

for task in tasks:
    if tasks[task] == "очікує":
        waiting_tasks.append(task)

print("Усі задачі:")
print(tasks)

print("Задачі, які мають статус 'очікує':")
print(waiting_tasks)
