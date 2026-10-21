import hashlib


def generate_file_hashes(*file_paths):
    hashes = {}

    for path in file_paths:
        try:
            with open(path, 'rb') as file:
                data = file.read()
                file_hash = hashlib.sha256(data).hexdigest()
                hashes[path] = file_hash
        except FileNotFoundError:
            print('Файл не знайдено:', path)
        except IOError:
            print('Помилка четання файлу:', path)

    return hashes


result = generate_file_hashes('apache_logs.txt', 'task1.py', 'task2.py')
for path in result:
    print(path, '-', result[path])
