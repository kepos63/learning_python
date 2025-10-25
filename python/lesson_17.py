# Работа с файлами(txt, csv, json, xml)
import csv, json
from dis import pretty_flags
from os import write
import xml.etree.ElementTree as ET
from xml.dom import minidom



"""
XML (eXtensible Markup Language): Язык разметки для хранения и передачи структурированных данных.
Имеет древовидную структуру с тегами и атрибутами. Громоздкий, но строгий.
JSON (JavaScript Object Notation): Текстовый формат обмена данными, основанный на синтаксисе JavaScript.
Представляет данные как простые структуры (словари, списки, строки, числа). Более легковесный и простой для чтения и парсинга, чем XML.
CSV (Comma-Separated Values): Текстовый формат для представления табличных данных.
Каждая строка файла — это строка таблицы, а значения колонок разделены запятыми (или другими разделителями).

"""
"""
# Режим открытие на чтение 
file = open('files/file.txt', 'r', encoding='utf-8') # Переменная для обращения к файлу file.txt, обязательно вводим 3 параметра
read_file = file.read().split('\n')
for line in read_file:
    print(line) # Чтение из файла
file.close() # Закрыть файл

# Режим открытие на запись 
with open('files/file.txt', 'w', encoding='utf-8') as file:
    file.write('Вы записали текстовый файл!')
    file.write('\nВы записали второй раз\nтекстовый файл!\n')

# Режим открытие на добавление 
with open('files/file.txt', 'a', encoding='utf-8') as file:
    file.write('раз\n')
    file.write('два\n')

"""

# 1. Чтение из TXT файла и преобразование в структурированные данные
users_from_txt = []
with open('files/users.txt', 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        # Убираем символ переноса строки и разбиваем строку по запятой
        cleaned_line = line.strip().split(',')  #
        user_dict = {'Имя': cleaned_line[0], 'Возраст': cleaned_line[1], 'Город': cleaned_line[2]}
        users_from_txt.append(user_dict)
print('Данные из ТХТ:', users_from_txt)
"""
# 2. Запись этих данных в CSV файл
with open('files/users.csv', 'w', newline='', encoding='utf-8') as csv_file:
        field_names = ['Имя', 'Возраст', 'Город']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)  #
        writer.writeheader() # Записываем заголовок
        writer.writerows(users_from_txt) # Записываем все данные
print('Данные из CSV:', users_from_txt)

# 3. Конвертация в JSON файл и запись в файл
json_data = {'Пользователи': users_from_txt}
with open('files/users.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False) # indent - отступ 4 пробела, ensure_ascii=False для кириллицы
print('JSON файл успешно создан!')

# 4. Чтение из созданного JSON файла
with open('files/users.json', 'r', encoding='utf-8') as json_file:
    data_from_json = json.load(json_file)
print('\nДанные, прочитанные из JSON файла: ')
for user in data_from_json['Пользователи']:
    print(f'-{user['Имя']} - {user['Возраст']} лет, {user['Город']}')
"""
# 5 Создание XML из данных, полученных из TXT
root = ET.Element('Пользователи')
for user in users_from_txt:
    user_elem = ET.SubElement(root, 'Пользователь')
    for key, value in user.items():
        filed = ET.SubElement(user_elem, key)
        filed.text = value
xml_str = ET.tostring(root, encoding='unicode')
parsed_xml = minidom.parseString(xml_str)
pretty_xml_str = parsed_xml.toprettyxml(indent='    ')

with open('files/users.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(pretty_xml_str)
print('XML файл успешно сгенерирован!')


