def analyze_log_file(log_file_path):
    codes = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split('"')
                if len(parts) >= 3:
                    response = parts[2].split()
                    if len(response) > 0:
                        code = response[0]
                        if code in codes:
                            codes[code] += 1
                        else:
                            codes[code] = 1
    except FileNotFoundError:
        print('Помилка: файл не знайден.')
    except IOError:
        print('Помилка при чтанні файлу.')

    return codes


result = analyze_log_file('apache_logs.txt')
print('Кількість HTTP-кодов:')
for code in result:
    print(code, '-', result[code])
