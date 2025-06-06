# Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
# который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
# Пол: пол".

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")

person1 = Person("Полина", 18, "Женский")
person2 = Person("Владимир", 17, "Боевой вертолет APAche")
print(person1.gender)
person2.display_info()