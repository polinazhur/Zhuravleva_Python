# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.
def uppercase_generator(text):
    """Генератор, который преобразует все буквы в тексте в заглавные"""
    for char in text:
        yield char.upper()

# Пример использования генератора
input_text = input("Введите текст: ")
print("Текст в верхнем регистре:")

# Создаем генератор
generator = uppercase_generator(input_text)

# Используем генератор
for uppercase_char in generator:
    print(uppercase_char, end='')