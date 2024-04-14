# Задание 1: Создание и использование словаря
#menu = {
#    "Американо": 3000,
#    "Капучино": 3500,
#    "Латте": 4500,
#    "Моккачино": 3600,
#}
#def print_price(beverage):
#    if beverage in menu:
#        print(f"Цена {beverage}: {menu[beverage]} KRW")
#    else:
#        print(f"Напиток {beverage} не найден в меню.")
#print_price("Латте")
#print_price("Эспрессо")

# Задание 2: Изменение и удаление элементов словаря
#menu["Флэт Уайт"] = 3800 
#if "Моккачино" in menu:
#    del menu["Моккачино"]  
#print("Итоговое меню кафе:")
#for beverage, price in menu.items():
#    print(f"{beverage}: {price} KRW")

# Задание 3: Работа с JSON
#import json
#book_info = {
#    "title": "The Great Gatsby",
#    "author": "F. Scott Fitzgerald",
#    "year": 1925
#}
#json_string = json.dumps(book_info)
#print("Строка JSON, представляющая информацию о книге:", json_string)
#parsed_book_info = json.loads(json_string)
#print("Словарь, полученный из строки JSON:", parsed_book_info)

# Задание 4: Использование методов словаря
#print("Список ключей:", list(menu.keys()))
#print("Список значений:", list(menu.values()))
#print("Список пар ключ-значение:", list(menu.items()))

# Задание 5: Словари и условные выражения
#def print_cheaper_than(menu, price_limit):
#    print(f"Напитки по цене ниже или равной {price_limit} KRW:")
#    for beverage, price in menu.items():
#        if price <= price_limit:
#            print(f"- {beverage}: {price} KRW")
#print_cheaper_than(menu, 3600)
