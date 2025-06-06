# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.

# 1. Чтение содержимого файла и вывод на экран
with open('text18-9.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)

# 2. Подсчет букв в нижнем регистре
lowercase_count = sum(1 for char in content if char.islower())
print(f"\nКоличество букв в нижнем регистре: {lowercase_count}")

# 3. Создание нового файла с измененным стихотворением
if '\n' in content:
    lines = content.split('\n')
    last_line = lines[-1]

    user_phrase = input("\nВведите фразу для замены последней строки: ")
    lines[-1] = user_phrase

    with open('poem_with_new_ending.txt', 'w', encoding='utf-8') as new_file:
        new_file.write('\n'.join(lines))
    print("\nНовый файл 'poem_with_new_ending.txt' успешно создан!")
else:
    print("\nФайл не содержит нескольких строк. Нельзя заменить последнюю строку.")