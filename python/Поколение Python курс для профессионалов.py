# "Поколение Python": курс для профессионалов

# конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект

# ===== Модуль datetime =====
"""
from datetime import *

# ===== Класс date =====
date(year, month, day)                   # создаёт объект даты
date.today()                             # текущая локальная дата
date.min                                 # минимально допустимая дата
date.max                                 # максимально допустимая дата
date.fromordinal(n)                      # дата из порядкового числа (1.1.0001 = 1)
date.toordinal()                         # преобразует дату в порядковое число
date.replace(...)                        # возвращает копию с изменёнными параметрами
date.weekday()                           # день недели (0 — понедельник, 6 — воскресенье)
date.isoweekday()                        # день недели (1 — понедельник, 7 — воскресенье)
date.strftime(fmt)                       # форматирует дату в строку
date.isoformat()                         # строка в формате YYYY-MM-DD
.date.year                               # год
.date.month                              # месяц
.date.day                                # день

# ===== Класс time =====
time(hour=0, minute=0, second=0, microsecond=0)   # создаёт объект времени
time.replace(...)                        # копия объекта с заменёнными параметрами
time.strftime(fmt)                       # форматирует объект time в строку по fmt
time.isoformat()                         # строка в формате HH:MM:SS(.ffffff)
.time.hour                               # часы
.time.minute                             # минуты
.time.second                             # секунды
.time.microsecond                        # микросекунды

# ===== Класс datetime =====
datetime(...)                            # создаёт дату + время
datetime.combine(date_obj, time_obj)     # объединяет date и time
datetime.now(tz=None)                    # локальное текущее время (можно указать tz)
datetime.utcnow()                        # UTC-время (устарело с Python 3.12)
datetime.today()                         # эквивалент now() без tz
datetime.fromtimestamp(sec)              # datetime из секунд с эпохи
datetime.strptime(str, fmt)              # строка → datetime по формату
datetime.replace(...)                    # копия объекта с заменёнными параметрами
datetime.timestamp()                     # кол-во секунд от начала эпохи
datetime.isoformat()                     # строка ISO: YYYY-MM-DDTHH:MM:SS(.ffffff)
datetime.strftime(fmt)                   # форматирование в строку

.datetime.year                           # год
.datetime.month                          # месяц
.datetime.day                            # день
.datetime.hour                           # час
.datetime.minute                         # минута
.datetime.second                         # секунда
.datetime.microsecond                    # микросекунда

datetime.date()                         # извлекает компоненту date
datetime.time()                         # извлекает компоненту time

# ===== Класс timedelta =====
timedelta(...)                           # создаёт временной интервал
timedelta.total_seconds()                # общее кол-во секунд (float)
.timedelta.days                          # количество дней
.timedelta.seconds                       # количество секунд (<86400)
.timedelta.microseconds                  # микросекунды (<1_000_000)

# ===== Таблица форматирования =====
| Формат | Значение
| %a | Сокращенное название дня недели
| %A | Полное название дня недели
| %w | Номер дня недели [0, …, 6]
| %d | День месяца [01, …, 31]
| %b | Сокращенное название месяца
| %B | Полное название месяца
| %m | Номер месяца [01, …,12]
| %y | Год без века [00, …, 99]
| %Y | Год с веком
| %H | Час (24-часовой формат) [00, …, 23]
| %I | Час (12-часовой формат) [01, …, 12]
| %p | До полудня или после (при 12-часовом формате)
| %M | Число минут [00, …, 59]
| %S | Число секунд [00, …, 59]
| %f | Число микросекунд
| %z | Разница с UTC в формате ±HHMM[SS[.ffffff]]
| %Z | Временная зона
| %j | День года [001,366]
| %U | Номер недели в году (неделя начинается с воскр.)
| %W | Номер недели в году (неделя начинается с пон.)
| %c | Дата и время
| %x | Дата
| %X | Время

# ===== Операции с timedelta =====
+                                        # сложение интервалов
-                                        # разность интервалов
*                                        # умножение на число
/                                        # деление на число (float)
/ /                                      # целочисленное деление
%                                        # остаток от деления
abs()                                    # модуль (положительное значение)

# ===== Операции с datetime и date =====
datetime ± timedelta → datetime          # сдвиг даты/времени
date ± timedelta → date                  # сдвиг даты (неполные дни отбрасываются)
datetime - datetime → timedelta          # разность между datetime
date - date → timedelta                  # разность между датами

# ===== Сравнение объектов =====
==, !=, <, >, <=, >=                     # сравнение date/time/datetime/timedelta

# ===== Встроенные функции =====
str(obj)                                 # строковое представление
repr(obj)                                # тех. представление (в виде конструктора)
min(), max(), sorted()                   # работают с date/datetime/timedelta
abs(timedelta)                           # модуль

# ===== Локализация =====
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')     # установка русской локали
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')     # установка английской локали

# ===== Константы =====
datetime.MINYEAR                         # минимальный год — 1
datetime.MAXYEAR                         # максимальный год — 9999

# ===== Важные примечания =====
# datetime и timedelta — неизменяемые типы (hashable)
# datetime наследует методы и атрибуты от date
# strftime() работает одинаково для date/time/datetime
# isoformat() для datetime добавляет "T" между датой и временем
# timedelta не имеет .hours и .minutes — извлекаются из .seconds вручную
# timedelta может быть отрицательным
# timedelta нормализует значения: минуты → секунды, часы → дни и т.д.
# сравнение timedelta с int/str вызывает TypeError (кроме ==, !=)
# str(obj) автоматически вызывается при print()
# при strptime формат и строка должны строго совпадать — иначе ValueError
# date + timedelta с неполными сутками округляется в сторону дней
# timedelta / timedelta → float, // → int
"""
# ===== Модуль calendar =====
"""
Подробный разбор модуля calendar: атрибуты и функции

Импорт:
-------
import calendar

Атрибуты:
---------
- calendar.day_name
    Итератор полных названий дней недели в текущей локали.
    Пример:
        import locale
        import calendar
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        print(list(calendar.day_name))  # ['Понедельник', 'Вторник', ...]

- calendar.day_abbr
    Итератор сокращённых названий дней недели.
    Пример:
        print(list(calendar.day_abbr))  # ['Пн', 'Вт', 'Ср', ...]

- calendar.month_name
    Итератор полных названий месяцев, индекс 1-12 (0 - пустая строка).
    Пример:
        print(list(calendar.month_name))  # ['', 'Январь', 'Февраль', ...]

- calendar.month_abbr
    Итератор сокращённых названий месяцев.
    Пример:
        print(list(calendar.month_abbr))  # ['', 'Янв', 'Фев', ...]


Основные функции:
-----------------

1. calendar.setfirstweekday(weekday)
    Устанавливает первый день недели по всему модулю.
    weekday: 0=понедельник, 6=воскресенье
    Пример:
        calendar.setfirstweekday(calendar.SUNDAY)

2. calendar.firstweekday()
    Возвращает текущий выбранный первый день недели.
    Пример:
        print(calendar.firstweekday())  # возвращает число 0-6

3. calendar.isleap(year)
    Проверяет, является ли год високосным. Возвращает True/False.
    Пример:
        print(calendar.isleap(2024))  # True

4. calendar.leapdays(y1, y2)
    Возвращает количество високосных лет в интервале [y1, y2), y2 не включён.
    Пример:
        print(calendar.leapdays(2000, 2024))  # кол-во високосных годов

5. calendar.weekday(year, month, day)
    Возвращает день недели для даты (0=понедельник, …, 6=воскресенье).
    Пример:
        print(calendar.weekday(2025, 8, 15))  # 4 (пятница)

6. calendar.monthrange(year, month)
    Возвращает кортеж (день недели первого дня месяца, количество дней в месяце).
    Пример:
        first_day, days_in_month = calendar.monthrange(2025, 8)
        print(first_day, days_in_month)  # 4 31

7. calendar.monthcalendar(year, month)
    Возвращает список списков — недели месяца.
    Каждый вложенный список — неделя, содержащая 7 чисел: дни месяца, нули где нет дней.
    Пример:
        weeks = calendar.monthcalendar(2025, 8)
        for w in weeks:
            print(w)

8. calendar.month(year, month, w=0, l=0)
    Возвращает строку с календарём месяца.
    Параметры w — ширина поля для дня, l — количество строк на неделю.
    Пример:
        print(calendar.month(2025, 8))

9. calendar.calendar(year, w=2, l=1, c=3)
    Возвращает строку с календарём всего года.
    w — ширина числа, l — количество строк на неделю, c — кол-во месяцев в строке.
    Пример:
        print(calendar.calendar(2025))

10. calendar.prmonth(year, month, w=0, l=0)
    Печатает календарь месяца.
    Аналогично calendar.month, но сразу выводит в консоль.

11. calendar.prcal(year, w=0, l=0, c=3)
    Печатает календарь года.

Дополнительно:
--------------
- calendar.MONDAY, calendar.TUESDAY, ..., calendar.SUNDAY — константы дней недели (0..6).
- Можно менять первый день недели для более удобного локального отображения.
- Атрибуты day_name и др. зависят от локали, поддерживают вывод на русском.

Пример использования:

import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

calendar.setfirstweekday(calendar.MONDAY)

print('Дни недели:', list(calendar.day_name))
print('Календарь августа 2025:\n', calendar.month(2025, 8))

first_day, days = calendar.monthrange(2025, 8)
print(f"Первый день недели: {first_day}, дней в месяце: {days}")

weeks = calendar.monthcalendar(2025, 8)
print("Недели месяца (списки дней):")
for week in weeks:
    print(week)

print("Високосный 2024?", calendar.isleap(2024))
print("Количество високосных между 2000 и 2025:", calendar.leapdays(2000, 2025))

calendar.prmonth(2025, 8)
calendar.prcal(2025)

"""
# ===== Потоковый ввод stdin и вывод stdout =====
"""
# --- Потоковый ввод stdin ---
# import sys
# sys.stdin — поток для стандартного ввода (например, при запуске скрипта с данными из файла или пайпа)
#
# Варианты работы:
# Все данные одной строкой:
# data = sys.stdin.read()
#
# По строкам:
# lines = sys.stdin.readlines()
#
# Построчно в цикле:
# for line in sys.stdin:
#     print(line)
#
# В обычных задачах для интерактивного ввода пользуются input()

# --- Потоковый вывод stdout ---
# print("text") — стандартный способ вывести в stdout
#
# import sys
# sys.stdout.write("text\n") — запись в поток без автоперевода строк

# --- Пример: чтение всех строк и вывод в обратном порядке ---
# import sys
# lines = sys.stdin.readlines()
# for line in reversed(lines):
#     sys.stdout.write(line)
"""
# ===== Работа с csv файлами =====
"""
# --- Открытие/создание текстового файла ---
# with open('filename.txt', mode) as f:
#     f.write('text')   # записать строку
#     f.read()          # читать всё содержимое

# --- Режимы ---
# 'r'   — только чтение
# 'w'   — запись с перезаписью
# 'a'   — добавление (append)
# 'x'   — создать новый файл

# --- Форматы файлов ---
# CSV (comma-separated values)       — данные разделены запятыми
# TSV (tab-separated values)         — разделители табуляции (\t)
# DSV (delimiter-separated values)   — любой символ-разделитель

# --- Модуль csv ---
import csv

# --- Чтение CSV файла ---
with open('products.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

# --- Запись CSV файла ---
with open('out.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'price'])      # одна строка
    writer.writerows([['apple', 70], ['banana', 50]])  # несколько строк

# --- DictReader: чтение CSV как словаря ---
with open('products.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Product'], row['Price'])

# --- writerow, writerows: запись строковых и списочных данных ---
with open('products.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product', 'Price'])
    writer.writerows([['apple', 70], ['banana', 50]])

# --- Пример с табуляцией (tsv) ---
with open('data.tsv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)

# --- Пример с dsv, свой разделитель ---
with open('data.dsv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        print(row)
"""
# ===== Работа с json файлами =====
"""


import json

# --- Основы JSON и модуль json ---
# JSON (JavaScript Object Notation) — текстовый формат для обмена данными.
# Python предоставляет модуль json для сериализации (преобразования Python-объектов в JSON)
# и десериализации (обратного преобразования JSON в Python-объекты).

# --- Сериализация Python-объектов в JSON ---

# json.dumps(obj, *, indent=None, sort_keys=False, separators=None, ensure_ascii=True)
# Преобразует Python-объект `obj` в JSON-строку.
# Параметры:
# indent — количество пробелов для отступов (для красивого форматирования).
# sort_keys — сортировать ключи словаря в алфавитном порядке.
# separators — кортеж разделителей (между элементами и ключами), например (',', ':').
# ensure_ascii — если True, не-ASCII символы будут экранироваться.

# Пример:
data = {'name': 'Иван', 'age': 30, 'skills': ['Python', 'Django']}
json_string = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
print(json_string)
# Выводит красиво форматированную JSON-строку с сортированными ключами.


# --- Запись JSON в файл ---

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
# dump() сериализует и сразу записывает в файл.


# --- Загрузка JSON из файла ---

with open('data.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
print(loaded_data)
# load() читает JSON из файла и преобразует в Python-объекты.



# --- Десериализация JSON из строки ---

json_str = '{"name": "Иван", "age": 30}'
obj = json.loads(json_str)
# loads() десериализует из строки.



# --- json.dumps с параметрами форматирования ---

# indent — количество пробелов для отступов (красивый формат)
json_pretty = json.dumps(data, indent=4, ensure_ascii=False)
print(json_pretty)
# {
#     "name": "Иван",
#     "age": 30,
#     "skills": [
#         "Python",
#         "Django"
#     ]
# }

# sort_keys — сортировка ключей словаря по алфавиту
json_sorted = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
print(json_sorted)
# Ключи будут в алфавитном порядке: age, name, skills

# separators — поменять разделители
# по умолчанию (', ', ': ') — после запятой и двоеточия идут пробелы
json_compact = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
print(json_compact)
# {"name":"Иван","age":30,"skills":["Python","Django"]}

# ensure_ascii=False — чтобы сохранять русские символы без экранирования



# --- Таблица типов данных JSON ↔ Python ---

# JSON             | Python
# -----------------|---------
# string           | str
# number (int)     | int
# number (float)   | float
# true             | True
# false            | False
# null             | None
# array            | list
# object           | dict

# --- Важные функции модуля json ---
# dump(obj, fp, *, indent=None, sort_keys=False, ensure_ascii=True) - запись в файл
# dumps(obj, *, indent=None, sort_keys=False, ensure_ascii=True) - в строку
# load(fp) - чтение из файла
# loads(s) - чтение из строки

# --- Настройка форматирования: ---
# indent — число пробелов для вывода JSON с отступами
# sort_keys=True — сортирует ключи словаря по алфавиту
# separators — кортеж из двух строк для разделения элементов и ключей (например (',', ':'))

# --- Пример с настройками separators ---

json.dumps(data, separators=(',', ':'), ensure_ascii=False)
# Выведет JSON без пробелов после запятых и двоеточий.

# --- Итог ---
# Работа с JSON в Python проста и гибка благодаря модулю json, позволяющему удобно читать, записывать и преобразовывать данные.


"""
# ===== Работа с ZIP-файлами =====
'''
from zipfile import ZipFile, is_zipfile

# --- Открытие и чтение архива ZIP ---
with ZipFile('test.zip', 'r') as zip_file:
    # Вывести таблицу с информацией о содержимом архива
    zip_file.printdir()

    print('\n----------------------------------------------------\n')

    # Получить подробную информацию о каждом файле и папке (список объектов ZipInfo)
    info = zip_file.infolist()

    # Пример работы с объектом ZipInfo (6-й файл):
    print(info[6].file_size)       # размер файла в байтах
    print(info[6].compress_size)   # размер сжатого файла
    print(info[6].filename)        # имя файла в архиве
    print(info[6].date_time)       # дата и время добавления в архив

    # Вывести имена некоторых файлов
    print(info[8].filename)
    print(info[10].filename)
    print(info[12].filename)
    print(info[13].filename)

    print('\n----------------------------------------------------\n')

    # Проверить, является ли элемент директорией (папкой)
    print(info[0].is_dir())        # True если папка, иначе False
    print(info[6].is_dir())

    print('\n----------------------------------------------------\n')

    # Получить список всех имён файлов и папок в архиве
    name_list = zip_file.namelist()
    print(*name_list, sep='\n')

    print('\n----------------------------------------------------\n')

    # Получить информацию о конкретном файле по имени (четвёртый с конца)
    last_file = zip_file.getinfo(name_list[-4])
    print(last_file.file_size)
    print(last_file.compress_size)
    print(last_file.filename)
    print(last_file.date_time)

    print('\n----------------------------------------------------\n')

    # Чтение содержимого файла из архива (пример с декодированием из utf-8)
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read().decode('utf-8'))

# --- Запись файлов в архив ---
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py')                     # записать файл в архив с тем же именем
#     zip_file.write('lse.jpeg')                       # записать файл
#     print(zip_file.namelist())                       # список файлов в архиве
                                                       # записать с переименованием
#     zip_file.write('program.py', 'new_program.py')   # первый аргумент - это имя файла
#     zip_file.write('lse.jpeg', 'lse1.jpeg')          # второй аргумент - это новое имя файла в архиве


print('\n----------------------------------------------------\n')

# --- Извлечение файлов из архива ---
with ZipFile('test.zip', 'r') as zip_file:
    # Извлечь один файл с указанием пути для распаковки
    # ("название файла", "путь для извлечения")
    zip_file.extract('test/Картинки/avatar.png', 'C:/Users/user/Desktop/coding/git-lessons/test')

    # Извлечь весь архив в текущую папку (путь можно указать)
    # ("путь для извлечения")
    zip_file.extractall()

print('\n----------------------------------------------------\n')

# --- Проверка файла на архив ZIP ---
print(is_zipfile('C:/Users/user/Desktop/coding/git-lessons/test.zip'))  # True или False
'''
# ===== Работа с модулем pickle =====
'''
import pickle

# Сохраняет любые Python объекты (списки, словари, функции, классы) в файл (сериализация) и загружает обратно (десериализация).
# Аналогичен json, но поддерживает больше типов и только для Python.

# --- Запись в файл ---
with open('data.pkl', 'wb') as f:
    pickle.dump(obj, f)      # obj — любой Python объект

# --- Чтение из файла ---
with open('data.pkl', 'rb') as f:
    obj = pickle.load(f)

# --- В строку и обратно ---
b = pickle.dumps(obj)         # объект → байты
obj = pickle.loads(b)         # байты → объект

# --- Важно ---
# Работает только с Python, расширение .pkl.
# При загрузке файл должен быть безопасным (pickle не защищен).
'''
# ===== Самостоятельное изучение Модуля OS (примеры в папке test_os)=====
'''
# Модуль os позволяет работать с операционной системой из Python.
# Управляет файлами, папками, переменными среды и многое другое.

# Получение информации об ОС
import os
print(os.name)          # Имя ОС: 'nt' для Windows, 'posix' для Unix, 'java' для Jython
print(os.environ)       # Словарь с переменными окружения
print(os.getenv('TMP')) # Получить конкретную переменную среды

# Работа с директориями
print(os.getcwd())         # Текущая рабочая директория
os.chdir("D:/folder")      # Сменить рабочую директорию (пример Windows)
os.mkdir("D:/folder")      # Создать папку
os.makedirs("D:/a/b/c")    # Создать вложенные папки сразу
os.rmdir("D:/folder")      # Удалить пустую папку
os.removedirs("D:/a/b/c")  # Удалить вложенные пустые папки

# Проверка путей
print(os.path.exists("D:/test.txt"))   # Проверяет наличие файла или папки
print(os.path.isfile("D:/test.txt"))   # Проверяет, что это файл
print(os.path.isdir("D:/folder"))      # Проверяет, что это папка

# Работа с файлами
os.remove("D:/test.txt")                # Удалить файл
os.rename("D:/oldname.txt", "D:/newname.txt")   # Переименование файла или папки
os.renames("D:/a/b", "D:/x/y")         # Переименование вложенных папок

# Получение информации о файлах и каталогах
print(os.path.basename("D:/folder/file.txt"))  # Имя файла с расширением
print(os.path.dirname("D:/folder/file.txt"))   # Путь к папке
print(os.path.getsize("D:/file.txt"))          # Размер файла в байтах
print(os.stat("D:/file.txt"))                   # Расширенная информация о файле

# Содержимое каталогов
print(os.listdir("D:/folder"))          # Список файлов и папок в каталоге
for root, dirs, files in os.walk("D:/folder"):
    print(root)                         # Текущая папка
    print(dirs)                         # Список вложенных папок
    print(files)                        # Список файлов

# Запуск файлов и папок
os.startfile("D:/file.txt")             # Открыть файл или папку стандартным приложением

# Работа с путями
print(os.path.split("D:/folder/file.txt"))  # Разделить на путь и имя файла
print(os.path.join("D:/folder", "file.txt"))# Соединить путь и имя файла

# Примечания
# Для Windows пути лучше писать как raw-строки с префиксом r, чтобы не путать обратные слэши
# Проверяйте существование файлов перед операциями, чтобы избежать ошибок
# Модуль os универсален и кроссплатформен, помогает писать переносимый код

'''






































































































# задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи задачи

# Модуль 2.1
# 5
"""
def hide_card(card_number):
    card_number = card_number.replace(' ','')
    return '*'*12 + card_number[-4:]
"""
# 11
"""
def likes(names):
    if len(names) == 0:
        return f'Никто не оценил данную запись'
    elif len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} и {len(names)-2} других оценили данную запись'
    """
# 12
"""
def index_of_nearest(numbers,number):
    if not numbers:
        return -1
    return numbers.index(min(numbers, key=lambda x: abs(number-x)))
"""
# 13
"""
def spell(*args):
    res = {}
    for i in range(len(args)):
        res[args[i][0].lower()] = len(max(args, key=lambda x: len(x) if x[0].lower()==args[i][0].lower() else 0))
    return res

words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
"""
# 14
"""
def choose_plural(amount, declensions):
    if str(amount)[-1] in "056789" or str(amount)[-2:] in ['11','12','13','14']:
        return f"{amount} {declensions[2]}"
    elif str(amount)[-1] == "1":
        return f"{amount} {declensions[0]}"
    elif str(amount)[-1] in "234":
        return f"{amount} {declensions[1]}"

print(choose_plural(512312, ("цент", "цента", "центов")))
"""
# 15
"""
def get_biggest(numbers):
    if not numbers:
        return -1
    return int(''.join(sorted([str(x) for x in numbers], key=lambda x: x*len(str(max(numbers,key=lambda s: len(str(s))))), reverse=True)))


print(sorted([61, 228, 9, 3, 11]))
print(get_biggest([0, 0, 0, 0, 0, 0]))
"""

# Модуль 2.2
# 1
"""
d1, d2, d3 = int(input()), int(input()), int(input())
print(min(d1+d3+d2,min(d1,d2,d3)*2 + ((d1+d2+d3)-max(d1,d2,d3)-min(d1,d2,d3))*2))
"""
# 2
"""
#тупое решение
en, ru = False, False
for _ in range(3):
    if input() in "AaBCcEeHKMOoPpTXxy":
        en = True
    else:
        ru = True
if en and not ru:
    print('en')
elif ru and not en:
    print('ru')
else:
    print('mix')
"""
# 3
"""
n, x, y, A, B = (int(x) for x in input().split())
nums = [str(x) for x in range(1, n + 1)]
nums = nums[: x - 1] + nums[x - 1 : y][::-1] + nums[y:]
nums = nums[: A - 1] + nums[A - 1 : B][::-1] + nums[B:]
print(*nums)
"""
# 4
"""
S = [int(x) for x in input().split()]
res = []
for i in S:
    if S.count(i) > 1 and i not in res:
        res.append(i)
print(*sorted(res))
"""
# 5
"""
res = {}
for num in range(1,int(input())+1):
    key = sum([int(x) for x in str(num)])
    res[key] = res.get(key,0) + 1

print(max(res.values()))
"""
# 6
"""
res = {}
n = int(input())
for _ in range(n):
    languages = input().split(', ')
    for lang in languages:
        res[lang] = res.setdefault(lang,0) + 1
print([', '.join(sorted([k for k,v in res.items() if v==n])), 'Сериал снять не удастся'][len([k for k,v in res.items() if v==n])==0])
"""
# 7
"""
s = input()
indexes = [i for i in range(len(s)) if s[i] in 'ауоыиэяюёе']
for _ in range(int(input())):
    word = input()
    if [i for i in range(len(word)) if word[i] in 'ауоыиэяюёе'] == indexes:
        print(word)
"""
# 8
"""
#через while можно сделать попроще, чтобы обойти i == 0 
mas = [input().rstrip('@beegeek.bzz') for _ in range(int(input()))]

for _ in range(int(input())):
    mail = input()

    if f'{mail}' not in mas:
        print(f'{mail}{"@beegeek.bzz"}')
        mas.append(f'{mail}')
    else:
        for i in range(1,100):
            if f'{mail}{i}' not in mas:
                print(f'{mail}{i}{"@beegeek.bzz"}')
                mas.append(f'{mail}{i}')
                break
    """
# 9
"""
with open('files.txt', 'r', encoding='utf-8') as files:
    extensions = {}
    
    for s in [s.rstrip().split() for s in files.readlines()]:
        extensions[s[0].split('.')[1]] = extensions.setdefault(s[0].split('.')[1],list())
        extensions[s[0].split('.')[1]].append(s)
    
    for key,group in sorted(extensions.items()):
        weight = 0

        for file in sorted(group):
            if file[2]=='GB':
                weight += int(file[1])*1024*1024*1024
            elif file[2]=='MB':
                weight += int(file[1])*1024*1024
            elif file[2]=='KB':
                weight += int(file[1])*1024
            else:
                weight += int(file[1])
            print(file[0])
        print('----------')
        units = ['B','KB','MB','GB']
        k = 0
        while weight // 1024 >= 1:
            k+=1
            weight = round(weight/1024)

        print(f'Summary: {weight} {units[k]}')
        print()
"""
# Модуль 3.1
# 20
"""
from datetime import date

def get_min_max(dates):
    if not dates:
        return ()
    return (min(dates),max(dates))

dates = []

print(get_min_max(dates))
"""
# 21
"""
from datetime import date

def get_date_range(start,end):
    return [date.fromordinal(i) for i in range(date.toordinal(start),date.toordinal(end)+1)]


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
"""
# 22
"""
from datetime import date

def saturdays_between_two_dates(start,end):
    res = 0
    for date1 in range(date.toordinal(min(start,end)), date.toordinal(max(start,end))+1):
        if date.fromordinal(date1).weekday() == 5:
            res+=1
    return res

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))
"""
# Модуль 3.2
# 12
"""
from datetime import date

date1, date2 = date.fromisoformat(input()),date.fromisoformat(input())

print(min(date1,date2).strftime('%d-%m (%Y)'))
"""
# 13
"""
from datetime import date

[ print(s.strftime('%d/%m/%Y')) for s in sorted([date.fromisoformat(input()) for _ in range(int(input()))]) ]
"""
# 14
"""
from datetime import date

def print_good_dates(dates):
    res = sorted([date1 for date1 in dates if date1.year == 1992 and date1.month + date1.day == 29])
    [print(date1.strftime('%B %d, %Y')) for date1 in res]
"""
# 15
"""
from datetime import date

def is_correct(day,month,year):
    try:
        res = date(year,month,day)
        return True
    except:
        return False
"""
# 16
"""
from datetime import date

def is_correct(day,month,year):
    try:
        res = date(year,month,day)
        return True
    except:
        return False


k=0
date1 = input()
while date1 != 'end':
    day, month, year = date1.split('.')
    if is_correct(int(day),int(month),int(year)):
        print('Корректная')
        k+=1
    else:
        print('Некорректная')
    date1 = input()
    
print(k)
"""
# Модуль 3.3
# 17
"""
from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

print(min(data, key=lambda x: datetime.timestamp(datetime.strptime(data[x][1],'%d.%m.%Y %H:%M:%S')) - datetime.timestamp(datetime.strptime(data[x][0],'%d.%m.%Y %H:%M:%S')) ))
"""
# 18
"""
#мое решение
from datetime import datetime

with open('diary.txt','r',encoding='utf-8') as text:
    history = {}
    line = text.readline()
    while line != '':
        try:
            datetime.strptime(line.rstrip(), '%d.%m.%Y; %H:%M')
            keyDT = line.rstrip()
            txt = ''
            line = text.readline()
            while line != '\n' and line != '':
                txt += line.rstrip() + '\n'
                line = text.readline()
            history[keyDT] = txt
        except:
            line = text.readline()
    [print(key,value, sep='\n') if key != sorted(history.items(), key=lambda x: datetime.strptime(x[0], '%d.%m.%Y; %H:%M'))[-1] else print(key,value, sep='\n',end='') for key,value in sorted(history.items(), key=lambda x: datetime.strptime(x[0], '%d.%m.%Y; %H:%M'))]
"""
"""
#вдохновился в ответах
from datetime import datetime

with open('diary.txt','r',encoding='utf-8') as text:
    history = text.read().split('\n\n')
    history = sorted(history, key=lambda x: datetime.strptime(x[0:17],'%d.%m.%Y; %H:%M'))
    print(*history,sep='\n\n')
"""
# 19
"""
from datetime import date, datetime

def is_available_date(booked_dates, date_for_booking):
    res_booked_dates = []   # создаем новый список с забронированными датами 

    for day in booked_dates:   # проходимся по старому списку 
    
        if len(day) == 21:          # если это промежуток то выполняем следу.щий код
            start = date.toordinal(datetime.strptime(day.split('-')[0], '%d.%m.%Y'))   # находим первую дату в днях от эпохи UNIX
            end = date.toordinal(datetime.strptime(day.split('-')[1], '%d.%m.%Y'))     # находим вторую дату в днях от эпохи UNIX
            for iDATE in range(start,end+1):                                           # проходимся по этому промежутку между датами
                res_booked_dates.append(date.fromordinal(iDATE).strftime('%d.%m.%Y'))    # добавляем каждый день в этом промежутке в список, переделывая из "дней" в "дату"
    
        else:
            res_booked_dates.append(day)

    if len(date_for_booking) == 21:
        start = date.toordinal(datetime.strptime(date_for_booking.split('-')[0], '%d.%m.%Y'))
        end = date.toordinal(datetime.strptime(date_for_booking.split('-')[1], '%d.%m.%Y'))
        for iDATE in range(start,end+1):
            if date.fromordinal(iDATE).strftime('%d.%m.%Y') in res_booked_dates:
                return False
                break
        else:
            return True
    else:
        if date_for_booking in res_booked_dates:
            return False
        else:
            return True






dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
"""
# Модуль 3.4
# 18
"""
from datetime import timedelta, date


def num_of_sundays(year):
    first_day = date(year, 1, 1).toordinal()
    k = 0
    while date.fromordinal(first_day).weekday() != 6:
        first_day += 1
    while date.fromordinal(first_day).year == year:
        k += 1
        first_day += 7
    return k


print(num_of_sundays(768))
"""
# 19
"""
from datetime import timedelta, date

d,m,y = map(int, input().split('.'))
Date = date(y,m,d)
for i in range(2,12):
    print(Date.strftime('%d.%m.%Y'))
    Date += timedelta(days=i)
"""
# 20
"""
from datetime import datetime

mas = [datetime.strptime(x, '%d.%m.%Y') for x in input().split()]
res = [abs(mas[i] - mas[i+1]).days for i in range(len(mas)-1)]
    
print(res)

"""
# 21
"""
from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    dates  = [datetime.strptime(x, '%d.%m.%Y') for x in dates]
    start, end = min(dates), max(dates)
    days = (end-start).days
    return [(start+timedelta(days=i)).strftime('%d.%m.%Y') for i in range(days+1)]







dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))
"""
# 22
"""
from datetime import datetime, timedelta

start, end = input(), input()
start, end = datetime.strptime(start,'%H:%M'), datetime.strptime(end,'%H:%M')
for i in range((end-start+timedelta(minutes=10)).seconds//60//55):
    if end >= start + timedelta(minutes=45):
        end_moment = start + timedelta(minutes=45)
        print(f"{start.strftime('%H:%M')} - {end_moment.strftime('%H:%M')}")
        start = end_moment + timedelta(minutes=10)
"""
# Модуль 3.5
# 1
"""
from datetime import date, time, datetime, timedelta
from functools import reduce


data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

res = 0
for tupl in data:
    res += (datetime.strptime(tupl[1], '%H:%M') - datetime.strptime(tupl[0], '%H:%M')).seconds//60

print(res)
"""
# 2
"""
from datetime import datetime, timedelta

weekdays_dict = {}

y,m = 1, 1
while True:
    try:
        Date = datetime(y,m,13)
        weekdays_dict[Date.weekday()] = weekdays_dict.setdefault(Date.weekday(),0) + 1
        if m < 12:
            m += 1
        else:
            m = 1
            y += 1

    except:
        break

[print(value) for key, value in sorted(weekdays_dict.items())]
"""
# 3
"""
from datetime import datetime, timedelta

schedule = {
    0: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    5: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }

s = datetime.strptime(input(),'%d.%m.%Y %H:%M')
res = schedule[s.date().weekday()]['end'].seconds//60 - s.hour * 60 - s.minute
all_min_shop = schedule[s.date().weekday()]['end'].seconds//60 - schedule[s.date().weekday()]['start'].seconds//60
if res <= 0 or res > all_min_shop:
    print('Магазин не работает')
else:
    print(res)
"""
# 4
"""
from datetime import datetime, timedelta


start, end = datetime.strptime(input(),'%d.%m.%Y'), datetime.strptime(input(),'%d.%m.%Y')
while (start.month + start.day) % 2 == 0 :
    start += timedelta(days=1)

while start <= end:
    if start.weekday() != 0 and start.weekday() != 3:
        print(start.strftime('%d.%m.%Y'))
    start += timedelta(days=3)
"""
# 5
"""
#мой метод, почему-то светится ошибка, но делает всё норм
from datetime import datetime, timedelta

employee_mas = [input().split() for _ in range(int(input()))]    # считываем сотрудников в строки

for i in range(len(employee_mas)):
    employee_mas[i][2] = datetime.strptime(employee_mas[i][2], '%d.%m.%Y')   # переписываем дату из строки в datetime

employee_mas_max = list(filter( lambda x: x[2] == min( employee_mas, key=lambda x: x[2])[2], employee_mas ))  # ищем самого взрослого сотрудника/сотрудников

print([f"{datetime.strftime(employee_mas_max[0][2],'%d.%m.%Y')} {employee_mas_max[0][0]} {employee_mas_max[0][1]}", f"{datetime.strftime(employee_mas_max[0][2],'%d.%m.%Y')} {len(employee_mas_max)}"][len(employee_mas_max)!=1])
"""
"""
#списал понравившееся решение
from datetime import datetime

d = {}
for _ in range(int(input())):
    name, Date = input().rsplit(maxsplit=1)
    d.setdefault(datetime.strptime(Date, '%d.%m.%Y'), []).append(name)
print( min(d).strftime('%d.%m.%Y'), [''.join(d[min(d)]) , len(d[min(d)]) ][ len(d[min(d)]) > 1 ] )
"""
# 6
"""
from datetime import datetime

employee_dict = {}

for _ in range(int(input())):
    name, Date = input().rsplit(maxsplit=1)
    employee_dict.setdefault(Date, []).append(name)

res = sorted([datetime.strptime(k,'%d.%m.%Y') for k,v in employee_dict.items() if len(v) == len(employee_dict[max(employee_dict, key=lambda x: len(employee_dict[x]))])])

[print(x.strftime('%d.%m.%Y')) for x in res]
"""
# 7
"""
from datetime import datetime, timedelta

employee_dict = {}
D,M,Y = [int(x) for x in input().split('.')]

for _ in range(int(input())):
    name, Date = input().rsplit(maxsplit=1)
    employee_dict[Date] = name

employee_dict = dict(sorted(employee_dict.items(), key=lambda x: datetime.strptime(x[0],'%d.%m.%Y'), reverse=True))

for k,v in employee_dict.items():
    if datetime(Y,M,D) + timedelta(days=1) <= datetime(Y, int(k.split('.')[1]), int(k.split('.')[0])) <= datetime(Y,M,D) + timedelta(days=7) \
        or datetime(Y,M,D) + timedelta(days=1) <= datetime(Y+1, int(k.split('.')[1]), int(k.split('.')[0])) <= datetime(Y,M,D) + timedelta(days=7):
        print(v)
        break
else:
    print('Дни рождения не планируются')
"""
# 8
"""
from datetime import datetime


def choose_plural(amount, declensions):
    if str(amount)[-1] in "056789" or str(amount)[-2:] in ['11','12','13','14']:
        return f"{amount} {declensions[2]}"
    elif str(amount)[-1] == "1":
        return f"{amount} {declensions[0]}"
    elif str(amount)[-1] in "234":
        return f"{amount} {declensions[1]}"



relize = datetime(year=2022, month=11, day=8, hour=12)
Date = datetime.strptime(input(), '%d.%m.%Y %H:%M')

res = relize - Date
res = [res.days, res.seconds//60//60, res.seconds%3600//60]

if res[0]<0 or res[0]==0 and res[1]==0 and res[2]==0:
    print('Курс уже вышел!')
elif res[0] and res[1]:
    print(f"До выхода курса осталось: {choose_plural(res[0],("день", "дня", "дней"))} и {choose_plural(res[1],("час", "часа", "часов"))}")
elif res[0] and not res[1]:
    print(f"До выхода курса осталось: {choose_plural(res[0],("день", "дня", "дней"))}")
elif not res[0] and res[1] and res[2]:
    print(f"До выхода курса осталось: {choose_plural(res[1],("час", "часа", "часов"))} и {choose_plural(res[2],("минута", "минуты", "минут"))}")
elif not res[0] and res[1] and not res[2]:
    print(f"До выхода курса осталось: {choose_plural(res[1],("час", "часа", "часов"))}")
elif not res[0] and not res[1] and res[2]:
    print(f"До выхода курса осталось: {choose_plural(res[2],("минута", "минуты", "минут"))}")
"""
"""
import time

def get_the_fastest_func(func, *args, d={}):
    for i in func:
        start = time.perf_counter()
        i(*args)
        d[i.__name__] = time.perf_counter() - start
    # return min(d, key=lambda x: d[x])
    return d


def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable)   




print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))
"""
# Модуль 3.7
# 13
"""
import calendar
from datetime import date, timedelta

def get_all_mondays(year):
    res = []
    day = 1
    while date(year,1,day).weekday() != 0:
        day += 1
    while (date(year-1,12,31) + timedelta(days=day)).year == year:
        res.append( date(year-1,12,31) + timedelta(days=day) )
        day += 7
    return res

print(get_all_mondays(111))
"""
# 14
"""
import calendar
from datetime import date

year = int(input())
for month in range(1,12+1):
    for day in range(15,21+1):
        if date(year,month,day).weekday() == 3:
            print(date(year,month,day).strftime('%d.%m.%Y'))
            break
"""
# Модуль 4.1
# 10
"""
import sys

for line in sys.stdin:
    sys.stdout.write(line.rstrip()[::-1])
    print()
"""
# 11
"""
import sys
from datetime import date

dates = []
for Date in sys.stdin:
    y,m,d = map(int, Date.strip().split('-'))
    dates.append(date(y,m,d))
sys.stdout.write(str((max(dates)-min(dates)).days))
"""
# 12
"""
import sys

k, last_step = 0, 0
for i in sys.stdin:
    k+=1
    last_step = int(i.strip())

if last_step % 2 == 0:
    sys.stdout.write(['Анри','Дима'][k%2==0])
elif last_step % 2 != 0:
    sys.stdout.write(['Анри','Дима'][k%2!=0])
"""
# 13
"""
import sys

students_height = [int(x) for x in sys.stdin]
if len(students_height) == 0:
    sys.stdout.write('нет учеников')
else:
    sys.stdout.write(f"Рост самого низкого ученика: {min(students_height)}\n")
    sys.stdout.write(f"Рост самого высокого ученика: {max(students_height)}\n")
    sys.stdout.write(f"Средний рост: {sum(students_height)/len(students_height)}")
"""
# 14
"""
import sys

sys.stdout.write(str(sum([1 for s in sys.stdin if s.strip()[0]=='#'])))
"""
# 15
"""
import sys 

for line in sys.stdin:
    if len( line.strip() ) == 0 or line.strip()[0] != '#':
        sys.stdout.write(line)
"""
# 16
"""
import sys

res = []
condition = ''
for line in sys.stdin:
    if '/' in line:
        res.append(line.strip().split(' / '))
    else:
        condition = line.strip()

[sys.stdout.write(elem[0] + '\n') for elem in sorted(list(filter(lambda x: x[1]==condition, res)), key=lambda x: (x[2],x[0]))]
"""
# 17
"""
import sys
from datetime import datetime

res = []
for line in sys.stdin:
    res.append(datetime.strptime(line.strip(), '%d.%m.%Y'))

if res == sorted(list(set(res))):
    sys.stdout.write('ASC')
elif res == sorted(list(set(res)), reverse=True):
    sys.stdout.write('DESC')
else:
    sys.stdout.write('MIX')
"""
# 18
"""
import sys

numbers = []
for line in sys.stdin:
    numbers.append(int(line.strip()))

arif, geom = 0, 0
for i in range(1, len(numbers)-1):
    if 2*numbers[i] == numbers[i-1] + numbers[i+1]:
        arif += 1
    if numbers[i]**2 == numbers[i-1] * numbers[i+1]:
        geom += 1

if arif == len(numbers)-2:
    sys.stdout.write('Арифметическая прогрессия')
elif geom == len(numbers)-2:
    sys.stdout.write('Геометрическая прогрессия')
else:
    sys.stdout.write('Не прогрессия')
"""
# Модуль 4.2
# 12
"""
import csv

with open('sales.csv', 'r', encoding='utf-8') as file:
    File = list(csv.reader(file, delimiter=';'))
    del File[0]
    for product in File:
        if int(product[1]) > int(product[2]):
            print(product[0])
"""
# 13
"""
import csv 

with open('salary_data.csv','r',encoding='utf-8') as file:
    file = list(csv.reader(file,delimiter=';'))
    del file[0]
    average_salary = {}
    for row in file:
        average_salary[row[0]] = average_salary.get(row[0],[]) + [int(row[1])]
    for company in average_salary:
        average_salary[company] = sum(average_salary[company]) / len(average_salary[company])

    print(*sorted(sorted(average_salary), key=lambda x: int(average_salary[x])), sep='\n')
"""
# 14
"""
import csv

with open('deniro.csv','r',encoding='utf-8') as file:
    file = list(csv.reader(file))
    k = int(input())-1
    if file[0][k].isdigit():
        [print(*row, sep=',') for row in sorted(file, key=lambda x: int(x[k]))]
    else:
        [print(*row, sep=',') for row in sorted(file, key=lambda x: x[k])]
"""
# 15
"""
import csv

def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file = csv.DictReader(file,delimiter=',')
        res = {}
        for row in file:
            for key in row.keys():
                res.setdefault(key,[]).append(row[key])
        return res
        


csv_columns(input())
"""
# 16
"""
import csv

with open('data.csv', 'r', encoding='utf-8', newline='') as file, open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_write:
    file = list(csv.reader(file, delimiter=','))
    del file[0]

    file_write = csv.writer(file_write)
    file_write.writerow(['domain','count'])
    
    my_dict = {}

    for row in file:
        domain = row[2].split('@')[1]
        my_dict[domain] = my_dict.setdefault(domain,0) + 1

    file_write.writerows( sorted( my_dict.items(), key=lambda x: (x[1], x[0]) ) )
"""
# 17
"""
import csv

with open('wifi.csv', 'r', encoding='utf-8') as file:
    file = list(csv.reader(file, delimiter=';'))
    del file[0]
    districts = {}
    for row in file:
        districts[row[1]] = districts.setdefault(row[1],0)+int(row[3])
    [print(f'{key}: {value}') for key,value in sorted(districts.items(), key=lambda x: (-x[1],x[0]))]
"""
# 18
"""
import csv

with open('titanic.csv', 'r', encoding='utf-8') as file:
    file = list(csv.reader(file, delimiter=';'))
    res = []
    for row in file:
        if row[0] == '1' and float(row[3]) < 18:
            res.append(row)
    [print(row[1]) for row in sorted(res, key=lambda x: x[2], reverse=True)]
"""
# 19
"""
import csv
from datetime import datetime

with open('name_log.csv','r', encoding='utf-8') as old_file, open('new_name_log.csv','w',encoding='utf-8',newline='') as new_file:
    old_file = list(csv.reader(old_file))
    del old_file[0]
    new_log = {}
    for row in sorted(old_file, key=lambda x: datetime.strptime(x[2],'%d/%m/%Y %H:%M')):
        new_log[row[1]] = row
    
    new_file = csv.writer(new_file)
    new_file.writerow(['username','email','dtime'])
    new_file.writerows(sorted(new_log.values(), key=lambda x: x[1]))
"""
# 20
'''
import csv


def condense_csv(filename, id_name):
    with open(filename, "r", encoding="utf-8") as file_read, open("condensed.csv", "w", encoding="utf-8", newline="") as file_write:
        file_read = csv.reader(file_read)
        features = {}
        all_objects = []
        for row in file_read:
            features[row[1]] = features.setdefault(row[1], []) + [row]
            if row[0] not in all_objects:
                all_objects.append(row[0])

        file_write = csv.writer(file_write)
        first_line = [id_name] + [x for x in features.keys()]
        file_write.writerow(first_line)
        res = [[name] for name in all_objects]

        for value in features.values():
            for i in range(len(res)):
                res[i].append(value[i][2])

        file_write.writerows(res)




text = """ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none"""

with open("data.csv", "w", encoding="utf-8") as file:
    file.write(text)

condense_csv("data.csv", id_name="ID")

with open("condensed.csv", encoding="utf-8") as file:
    print(file.read().strip())
'''
# 21
"""
import csv

with open('student_counts.csv', 'r', encoding='utf-8') as file, open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_write:
    file = list(csv.reader(file))
    first_line = file[0]
    first_line_sorted = [file[0][0]] + sorted(file[0][1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    list_key = []
    for i in first_line_sorted:
        list_key.append(first_line.index(i))

    file_write = csv.writer(file_write)
    for row in file:
        line = []
        for i in list_key:
            line.append(row[i])
        file_write.writerow(line)
"""
# 22
"""
import csv

with open('prices.csv', 'r', encoding='utf-8') as file:
    file = csv.DictReader(file, delimiter=';')
    min_shop, min_product, min_price = 'XXX', 'XXX', 10**10

    for shop_dict in file:
        shop = shop_dict['Магазин']
        for key,value in shop_dict.items():
            if key == 'Магазин':
                continue

            if int(value) < min_price:
                min_shop, min_product, min_price = shop, key, int(value)
            elif int(value) == min_price and key < min_product:
                min_shop, min_product, min_price = shop, key, int(value)
            elif int(value) == min_price and key == min_product and shop < min_shop:
                min_shop, min_product, min_price = shop, key, int(value)
    
    print(f'{min_product}: {min_shop}')
"""
"""
import csv

prices = []
with open('prices.csv', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=";")
    products = reader.__next__()[1:]    # Отбрасываем строку "Магазин"
    
    for shop, *price_list in reader:
        prices.extend(map(lambda price, product: (int(price), product, shop), price_list, products))

print(f"{min(prices)[1]}: {min(prices)[2]}")
"""
# Модуль 4.4
# 6
"""
import json, sys

json_object = sys.stdin.read()
json_object = json.loads(json_object)
for key,value in json_object.items():
    if type(value) == list:
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')
"""
# 7
"""
import json

with open('data.json', 'r', encoding='utf-8') as file_r, open('updated_data.json', 'w', encoding='utf-8') as file_w:
    file_r = json.load(file_r)
    res = []
    for row in file_r:
        if type(row) == str:
            res.append(row+'!')
        elif type(row) == int:
            res.append(row+1)
        elif type(row) == int:
            res.append(row+1)
        elif type(row) == bool:
            res.append(not row)
        elif type(row) == list:
            res.append(row*2)
        elif type(row) == dict:
            row["newkey"] = None
            res.append(row)
    json.dump(res, file_w, indent=3)
"""
# 8
"""
import json

with open('data1.json','r',encoding='utf-8') as file:
    file1_dict = json.load(file)
with open('data2.json','r',encoding='utf-8') as file:
    file2_dict = json.load(file)

for key,value in file2_dict.items():
    file1_dict[key] = value

with open('data_merge.json', 'w', encoding='utf-8') as file:
    json.dump(file1_dict, file, indent=3)
"""
# 9
"""
import json

with open("people.json", "r", encoding="utf-8") as file, \
    open('updated_people.json', 'w', encoding='utf-8') as file_w:
    people_json = json.load(file)
    
    all_keys = set(max(people_json, key=len).keys())
    for obj in people_json:
        obj.update(dict.fromkeys(list(all_keys-set(obj.keys()))))
    
    json.dump(people_json, file_w, indent=3)
"""
# 10
"""
import json

with open('countries.json','r',encoding='utf-8') as file_r, \
    open('religion.json','w',encoding='utf-8') as file_w:
    res_religions = {}
    file_r = json.load(file_r)
    for row in file_r:
        res_religions.setdefault(row['religion'], []).append(row['country'])
    json.dump(res_religions, file_w, indent=3)
"""
# 11
"""
import json, csv

with open('playgrounds.csv','r',encoding='utf-8') as file_csv, \
    open('addresses.json', 'w', encoding='utf-8') as file_json:
    res_addresses = {}
    file_csv = list(csv.reader(file_csv, delimiter=';'))
    del file_csv[0]
    for row in file_csv:
        res_addresses.setdefault(row[1],{}).setdefault(row[2],[]).append(row[3])
        
    json.dump(res_addresses, file_json, indent=3, ensure_ascii=False)
"""
# 12
"""
import json, csv

with open('students.json', 'r', encoding='utf-8') as file_read, \
    open('data.csv', 'w', encoding='utf-8', newline='') as file_write:
    file_read = json.load(file_read)
    
    file_write = csv.writer(file_write, delimiter=',')
    file_write.writerow(['name','phone'])

    res = []

    for student in file_read:
        if student['age'] >= 18 and student['progress'] >= 75:
            res.append([student['name'], student['phone']])

    file_write.writerows(sorted(res))
"""
# 13
"""
import json
from datetime import timedelta

with open('pools.json', 'r', encoding='utf-8') as file:
    file = json.load(file)

xy_res, address = (0,0), 'aq'

for pool in file:
    t1,t2 = pool['WorkingHoursSummer']['Понедельник'].split('-')
    t1 = timedelta(hours=int(t1.split(':')[0]), minutes=int(t1.split(':')[1]))
    t2 = timedelta(hours=int(t2.split(':')[0]), minutes=int(t2.split(':')[1]))
    if t1<=timedelta(hours=10) and t2>=timedelta(hours=12):
        if xy_res < (pool['DimensionsSummer']['Length'], pool['DimensionsSummer']['Width']):
            xy_res = (pool['DimensionsSummer']['Length'], pool['DimensionsSummer']['Width'])
            address = pool['Address']

print(f'{xy_res[0]}x{xy_res[1]}', address, sep='\n')
"""
# 14
"""
import json, csv
from datetime import datetime

with open("exam_results.csv", "r", encoding="utf-8") as file_r:
    names = ["name", "surname", "best_score", "date_and_time", "email"]
    file_r = csv.DictReader(file_r.readlines()[1:], fieldnames=names)

    res = {}
    for row in file_r:
        if row["email"] in res and (row["best_score"] > res[row["email"]]["best_score"] or \
                                    row["best_score"] == res[row["email"]]["best_score"] and \
                                    datetime.strptime(row["date_and_time"], "%Y-%m-%d %H:%M:%S") > datetime.strptime(res[row["email"]]["date_and_time"], "%Y-%m-%d %H:%M:%S") ):
            res[row["email"]] = row

        elif row["email"] not in res:
            res[row["email"]] = row

with open("best_scores.json", "w", encoding="utf-8", newline="") as file_w:
    res = [value for value in dict(sorted(res.items())).values()]
    for row_dict in res:
        row_dict['best_score'] = int(row_dict['best_score'])
    file_w = json.dump(res, file_w, indent=4)
"""
# 15
'''
import json

with open("food_services.json", "r", encoding="utf-8") as file:
    file = json.load(file)

districts_count, company_count = {}, {}

for row_dict in file:
    districts_count[row_dict["District"]] = (
        districts_count.get(row_dict["District"], 0) + 1
    )
    company_count[row_dict["OperatingCompany"]] = (
        company_count.get(row_dict["OperatingCompany"], 0) + 1
    )

del company_count[""]

print(*max(districts_count.items(), key=lambda x: x[1]), sep=": ")
print(*max(company_count.items(), key=lambda x: x[1]), sep=': ')
'''
# 16
'''
import json

with open('food_services.json','r',encoding='utf-8') as file:
    file = json.load(file)

res = {}

for row_dict in file:
    if row_dict['TypeObject'] not in res or (row_dict['SeatsCount'] > res[row_dict['TypeObject']][0]):
        res[row_dict['TypeObject']] = (row_dict['SeatsCount'], row_dict['Name'])

[print(key,f'{value[1]}, {value[0]}', sep=': ') for key,value in sorted(res.items())]
'''
# Модуль 4.5
# 1
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    k = 0
    for file in zip_file.infolist():
        if not file.is_dir():
            k+=1
    print(k)
"""
# 2
"""
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    res1, res2 = 0, 0
    for file in zip_file.infolist():
        res1 += int(file.file_size)
        res2 += int(file.compress_size)

print(f'Объем исходных файлов: {res1} байт(а)')
print(f'Объем сжатых файлов: {res2} байт(а)')
"""
# 3
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    res = (0, 'xxx')
    for file in zip_file.infolist():
        if not file.is_dir() and res[0] < 100-(file.compress_size / file.file_size * 100):
            res = (100-(file.compress_size / file.file_size * 100), file.filename)
print(res[1].split('/')[1])
"""
# 4
'''
from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    res = []
    for file in zip_file.infolist():
        if not file.is_dir() and file.date_time > (2021, 11, 30, 14, 22, 0):
            res.append(file.filename)
    print(*sorted([s.split("/")[1] if "/" in s else s for s in res]), sep='\n')
'''
# 5
'''
from zipfile import ZipFile
from datetime import datetime

res = []
with ZipFile('workbook.zip') as zip_file:
    for file in zip_file.infolist():
        if not file.is_dir():
            if '/' in file.filename:
                res.append([file.filename.split('/')[-1], datetime(*file.date_time), file.file_size, file.compress_size])
            else:
                res.append([file.filename, datetime(*file.date_time), file.file_size, file.compress_size])

for s in sorted(res, key=lambda x: x[0]):
    print(f"""{s[0]}
  Дата модификации файла: {s[1]}
  Объем исходного файла: {s[2]} байт(а)
  Объем сжатого файла: {s[3]} байт(а)
""")
'''
# 6
'''
from zipfile import ZipFile

file_names = ['best_scores.json', 'exam_results.csv']

with ZipFile('files.zip','w') as file_zip:
    for name in file_names:
        file_zip.write(name)
'''
# 7
'''
from zipfile import ZipFile, ZipInfo

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip','w') as file_zip:
    for name in file_names:
        if 100 >= ZipInfo.from_file(name).file_size:
            file_zip.write(name)
'''
# 8
'''
from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as file_zip:
        file_zip.extractall(members=args or None)
'''
# 9
'''
from zipfile import ZipFile
import json


res = []

with ZipFile('data.zip') as file_zip:                           # открываем zip
    for file_info in file_zip.infolist():                       # проходимся по всему содержимому
        with file_zip.open(file_info) as file:                  # открываем файл
            try:                                                # проверяем json ли это
                file_json = json.load(file)                     # если ДА, то сразу читаем его
            except:
                continue
            
            if file_json['team'] == 'Arsenal':
                res.append((file_json['first_name'], file_json['last_name']))

[print(*player) for player in sorted(res)]
'''
# 10
'''
from zipfile import ZipFile


def file_rounded_weight(weight):
    for i in range(3):
        if weight // 1024 >= 1:
            weight = round(weight/1024)
        else:
            return f"{weight} {['B','KB','MB'][i]}"
    return f"{weight} GB"


with ZipFile('test.zip') as file_zip:
    for file in file_zip.infolist():
        if file.is_dir():
            print(f"{'  ' * (file.filename.count('/')-1)}{file.filename.split('/')[-2]}")
        else:
            rounded_weight = file_rounded_weight(file.file_size)
            print(f"{'  ' * (file.filename.count('/'))}{file.filename.split('/')[-1]} {rounded_weight}")
            '''
# 4.6
# 2
'''
import pickle, sys

with open(input(),'rb') as file:
    my_func = pickle.load(file)

args = [line.strip() for line in sys.stdin]
print(my_func(*args))
'''
# 3
'''
import pickle

def filter_dump(filename, objects, typename):
    filtered = [i for i in objects if type(i) == typename]
    with open(filename, 'wb') as file_w:
        pickle.dump(filtered, file_w)


filter_dump('numbers.pkl', [1, '2', '3', '3', '3', 4, '5'], int)

with open('numbers.pkl','rb') as file:
    print(pickle.load(file))
'''
# 4
'''
import pickle

with open(input(),'rb') as file_r:
    file_r = pickle.load(file_r)
    
file_r_int = [i for i in file_r if isinstance(i,int)]

if type(file_r) is list and file_r_int:
    checksum = min(file_r_int) * max(file_r_int)
elif type(file_r) is dict and file_r_int:
    checksum = sum(file_r_int)
else:
    checksum = 0
    
checksum_orig = int(input())
if checksum == checksum_orig:
    print('Контрольные суммы совпадают')
else:
    print('Контрольные суммы не совпадают')
'''
# 4.7 Модуль os
# === Практика ===
'''
import os
#print(os.name)

#print(os.environ)

#print(os.getenv('TMP'))

#print(os.getcwd()) 

#os.chdir(r"C:/Users/user/Desktop/testtt")

#print(os.path.exists("C:/Users/user/Desktop/coding/test_os/test.pkl"))
#print(os.path.exists("test.pkl"))

#print(os.path.isfile("folder_test"))
#print(os.path.isfile("C:/Users/user/Desktop/coding/test_os/test.pkl"))
#print(os.path.isfile("test.pkl"))

#print(os.path.isdir("folder_test"))
#print(os.path.isdir("C:/Users/user/Desktop/coding/test_os/test.pkl"))
#print(os.path.isdir("test.pkl"))

#os.mkdir("C:/Users/user/Desktop/coding/test_os/test_mkdir")
#os.mkdir("test_mkdir_2")

#os.makedirs("C:/Users/user/Desktop/coding/test_os/test_makedirs/test2_makedirs/test3_makedirs")
#os.makedirs("test_makedirs_2/test2_makedirs_2/test3_makedirs_2")

#os.remove("C:/Users/user/Desktop/coding/test_os/test_for_remove_2.txt")
#os.remove('test_for_remove.txt')

#os.rmdir('folder_for_remove')

#os.removedirs("for_test_makedirs_2/for_test2_makedirs_2/for_test3_makedirs_2")

#os.startfile("test_startfile.docx")
#os.startfile("C:/Program Files (x86)/GamersFirst/APB Reloaded/Launcher/APBLauncher.exe")

#print(os.path.basename("C:/Users/user/Desktop/coding/test_os/test_startfile.docx"))

#print(os.path.dirname("C:/Users/user/Desktop/coding/test_os/test.pkl"))

#print(os.path.getsize("C:/Users/user/Desktop/coding/test_os"))
#print(os.path.getsize("test.pkl"))

#os.rename("C:/Users/user/Desktop/coding/test_os/folder_test", "C:/Users/user/Desktop/coding/test_os/folder_test_rename")

#os.renames("test_makedirs_2_rename/test2_makedirs_2_rename/test3_makedirs_2_rename", "test_makedirs_2/test2_makedirs_2/test3_makedirs_2")

#print(os.listdir())
#print(os.listdir("C:/Users/user/Desktop/coding/git-lessons"))


#for root, directories, files in os.walk("C:/Users/user/Desktop/coding/git-lessons/python/test_os"):
#    print(root)
#    [print(directory) for directory in directories]
#    [print(file) for file in files]


#print(os.stat("C:/Usersuser/Desktop/coding/test_os"))

#print(os.path.split("C:/Users/user/Desktop/coding/test_os"))

#print(os.path.join("C:/Users/user/Desktop/coding", "test_os"))
'''
# A (задания с сайта - https://ejudge.179.ru/tasks/python/2027b/27-os.html)
'''
import os

os.chdir("C:/Users/user/Desktop/coding/git-lessons/Primates/Haplorrhini/Simiiformes/Platyrrhini/Callitrichinae")
res_files = [file for file in os.listdir() if os.path.isfile(file)]
print(*sorted(res_files), sep='\n')
'''
# B 
'''
import os

os.chdir('Primates')

while len([name for name in os.listdir() if os.path.isdir(name)]) > 0:
    os.chdir(min([name for name in os.listdir() if os.path.isdir(name)]))

print( os.path.dirname(os.path.join(os.getcwd(), min([name for name in os.listdir() if os.path.isfile(name)]))))
'''
# C
'''
import os

def find_file(file_name):
    for root, dirs, files in os.walk('C:/Users/user/Desktop/coding/git-lessons/Primates'):
        if file_name in files:
            with open(os.path.join(root,file_name)) as file:
                print(file.read().strip())
            break

find_file('Homo_sapiens.txt')
'''
# D
'''
import os

def find_file(file_name):
    for root, dirs, files in os.walk('C:/Users/user/Desktop/coding/git-lessons/Primates'):
        if file_name in files:
            print('Primates' + os.path.join(root,file_name).split('Primates')[1].replace('\\','/'))
            break
        

find_file('Homo_sapiens.txt')
'''
# E
'''
import os

res_files = []
for root, dirs, files in os.walk('Primates'):
    [res_files.append(file) for file in files]

print(*sorted(res_files), sep='\n')
'''
# F
'''
import os

for root, dirs, files in os.walk('Primates'):
    dirs.sort()
    print(root.replace('\\', '/'))
'''
# G
'''
import os


def find_path_max_dir(path_file):
    path_res_file = ('All dirs have 0 files', 0)
    for root, dirs, files in os.walk(path_file):
        if len(files) > path_res_file[1]:
            path_res_file = (root, len(files))
    relative_path = os.path.relpath(path_res_file[0], path_file)
    
    if relative_path == '.':
        print(os.path.basename(path_file))
    else:
        print(os.path.join(os.path.basename(path_file), relative_path).replace('\\','/'))

    
find_path_max_dir(input())
'''
# H
'''
import os

res = []
for root, dirs, files in os.walk('Primates/Strepsirrhini/Lorisiformes/Lorisidae'):
    for file in files:
        with open(os.path.join(root,file)) as file_r:
            res.append(file_r.read().strip()) 

print(*sorted(res), sep='\n')
'''
# 4.7 Модуль shutil
# === Практика ===
# rmtree(path) — рекурсивное удаление директории
'''
# Удаляет всю директорию path со всем её содержимым (поддиректориями и файлами).
# Параметр ignore_errors позволяет игнорировать ошибки удаления.
# Параметры onerror (устаревший) и onexc — обработчики ошибок, которые вызываются при неудаче удаления.
# Не удаляет символические ссылки на каталоги, а удаляет сами каталоги.
# На платформах с поддержкой файловых дескрипторов защищает от атак с символическими ссылками.
# Игнорирует исключения FileNotFoundError для вложенных путей, кроме корня.
# Вызывает событие аудита с аргументом path.


import shutil, os

# создаем директорию с вложенными файлами для примера
os.makedirs('example1/example2/example3/example4')

# удаляем директорию
shutil.rmtree('example1')
'''
# copyfile(src, dst) - копирование содержимое одного файла в другой наиболее эффективным способом без переноса метаданных
'''
# Копирует только содержимое файла, без метаданных.
# Перезаписывает dst, если такой файл существует.
# Вызывает исключение SameFileError, если src и dst — один файл.
# Не копирует специальные файлы (например, символические ссылки).
# Параметр follow_symlinks определяет, копировать ли содержимое ссылки или саму ссылку.

import shutil, os

# создание файла и директории для тестов + просмотр содержимого
os.mkdir('example')
open('example/test_file.txt', 'w').close()
print(os.listdir('example'))

# копируем
shutil.copyfile('example/test_file.txt', 'example/test_file.txt.copy')

# смотрим содержимое директории + удаление после тестов
print(os.listdir('example'))
shutil.rmtree('example')
'''
# copy(src, dst) — копирование файла с правами доступа
'''
# Копирует содержимое файла и его права доступа (mode), но не другие метаданные.
# Если dst — каталог, копирует файл в эту папку с тем же именем.
# Поддерживает работу с символическими ссылками через параметр follow_symlinks.
# Если follow_symlinks=False и src — символическая ссылка, копирует именно ссылку.
# Возвращает путь к созданному файлу.

import shutil, os

# создание файла и директории для тестов + просмотр содержимого и прав доступа
open('file_test.txt','w').close()
os.mkdir('example')
print(os.listdir('example'))
print(os.stat('file_test.txt').st_mode)


# копирование
dests = shutil.copy('file_test.txt', 'example')


# просмотр содержимого, прав доступа, пути + удаление после тестов
print(os.listdir('example'))
print(os.stat('file_test.txt').st_mode)
print(dests)
os.remove('file_test.txt')
shutil.rmtree('example')
'''
# copy2(src, dst) — копирование файла с всеми метаданными 
'''
# Работает как copy(), но дополнительно сохраняет метаданные файла.
# При follow_symlinks=False и если src — символическая ссылка, пытается скопировать все метаданные символической ссылки в новую ссылку.
# Поддержка полного копирования метаданных зависит от платформы.
# Никогда не вызывает ошибку, если не может сохранить все метаданные — сохраняет максимум доступного.
# Использует copystat() для копирования метаданных.


import os
import shutil

def show_file_info(filename):
    stat_info = os.stat(filename)
    print('Mode:', stat_info.st_mode)
    print('Created:', stat_info.st_ctime)
    print('Accessed:', stat_info.st_atime)
    print('Modified:', stat_info.st_mtime)


# создание файла и директории для тестов + просмотр метаданных
open('shutil_copy2.py','w').close()
os.mkdir('example')
print('SOURCE:')
show_file_info('shutil_copy2.py')
print()


# копирование
shutil.copy2('shutil_copy2.py', 'example')


# просмотр метаданных + удаление после тестов
print('DESTINATION:')
show_file_info('example/shutil_copy2.py')
os.remove('shutil_copy2.py')
shutil.rmtree('example')
'''
# copytree(src, dst) — рекурсивное копирование директории
'''
# Копирует весь каталог src (с поддиректориями и файлами) в каталог dst.
# По умолчанию копирует все метаданные файлов и папок.
# Можно указать функцию для пропуска некоторых файлов/папок (ignore).
# Можно выбрать способ обработки символических ссылок (symlinks, follow_symlinks).
# Можно разрешить существование целевой папки (dirs_exist_ok=True).


import os
import shutil

# создание директории и файла в ней + просмотр содержимого
os.mkdir('example_tree')
open('example_tree/shutil_copytree.py','w').close()
print('Содержимое example_tree:', os.listdir('example_tree'))


# копирование
shutil.copytree('example_tree', 'example_tree_copy')


# просмотр содержимого + удаление после тестов
print('Содержимое example_tree_copy:', os.listdir('example_tree_copy'))
shutil.rmtree('example_tree')
shutil.rmtree('example_tree_copy')
'''
# which(cmd) — поиск пути к исполняемому файлу
'''
# Ищет исполняемый файл cmd в системной переменной PATH.
# Возвращает полный путь к найденному файлу или None, если файл не найден.
# По умолчанию ищет только существующие и исполняемые файлы (mode=os.F_OK | os.X_OK).
# Учитывает расширения из PATHEXT на Windows.
# Можно явно задать переменную среды поиска (path).


import shutil

print(shutil.which('python'))
print(shutil.which('git'))
print(shutil.which('aaaaaaaa'))
'''
# disk_usage(path) — статистика использования диска
'''
# Возвращает общий, используемый и свободный объем дискового пространства по указанному пути.
# Путь может быть файлом или каталогом.
# Результат представлен в виде именованного кортежа с атрибутами total, used и free (в байтах).
# Поддерживается на Unix и Windows системах.


import shutil

print(shutil.disk_usage('.'))
'''
# move(src, dst) — перемещение файла или каталога
'''
# Рекурсивно перемещает файл или каталог из src в dst.
# Если dst — существующий каталог, перемещает внутрь него.
# Если src и dst в одной файловой системе, используется os.rename().
# Если в разных файловых системах, копирует с помощью copy_function (по умолчанию copy2) и удаляет src.
# При работе с символическими ссылками создает новую ссылку на цель src и удаляет старую.
# Возвращает путь к целевому местоположению dst.

import shutil, os

# Создали файл и изменили формат
open('test_file.txt','w').close()
os.rename('test_file.txt','test_file.mp3')

# Создание файла и директории для теста
open('test_file2.txt','w').close()
os.mkdir('test_dir')

# Смотрим содержание директории
print(os.listdir('test_dir'))

# Переносим файл в директорию
shutil.move('test_file2.txt', 'test_dir')

# Смотрим содержание директории + удаляем
print(os.listdir('test_dir'))
shutil.rmtree('test_dir')
os.remove('test_file.mp3')
'''
# make_archive() — создание архива
'''
# make_archive(base_name, format, root_dir=None, base_dir=None, dry_run=False, owner=None, group=None, logger=None
# Создает архив с именем base_name в формате format (zip, tar, gztar, bztar, xztar).
# Архивирует содержимое каталога root_dir, начиная с base_dir (по умолчанию текущий каталог).
# Возвращает имя созданного архива.
# Параметр dry_run позволяет симулировать создание без записи архива.
# owner и group используются при создании tar-архивов.
# logger — объект для ведения журналов.


import shutil, os


result = shutil.make_archive('test_archive', 'zip', 'C:/Users/user/Desktop/testtt')
print(result)
'''
# get_archive_formats() / get_unpack_formats() — получение форматов архивов
'''
# get_archive_formats() возвращает список поддерживаемых форматов для создания архивов.
# Каждый элемент — кортеж (name, description) с именем формата и описанием.
# get_unpack_formats() возвращает список форматов для распаковки архивов.
# Каждый элемент — кортеж (name, extensions, description), где extensions — список расширений файлов.
# По умолчанию доступны форматы: zip, tar, gztar, bztar, xztar.
# Позволяет узнать, какие форматы поддерживает ваш текущий Python и платформа.

import shutil

print(*shutil.get_archive_formats(), sep='\n')
print(*shutil.get_unpack_formats(), sep='\n')
'''




































































































































































































































































































































































































































































































































































































































































































































































