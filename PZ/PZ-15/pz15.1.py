# Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов
# торговой фирмы. Таблица Заказы должна содержать информацию о товарах со
# следующей структурой записи: Код товара, Наименование товара, Заказчик
# (наименование организации, возможны повторяющиеся значения), Дата заказа, Срок
# исполнения (от 1 до 10 дней), Стоимость заказа. 

import sqlite3

conn = sqlite3.connect("orders.db")

def execute_sql_from_file(conn, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()

execute_sql_from_file(conn, 'code.sql')
conn.close()