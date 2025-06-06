# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re
text = open("Dostoevsky.txt", "r+", encoding="utf-8").read()

ex = re.compile(r"«\w+»")
print(ex.findall(text))