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
"""
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
"""
# ===== Работа с модулем pickle =====
"""
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
"""
# ===== Самостоятельное изучение Модуля OS (примеры в папке test_os) =====
"""
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

"""
# ===== Самостоятельное изучение Модуля shutil =====
"""
# теория сразу на примерах внизу
# название - 4.7 Модуль shutil
"""
# ===== Самостоятельное изучение Модуля shelve =====
"""
# очень грубо - словарь в виде файла, а не переменной

import shelve

# Создаем или открываем хранилище
with shelve.open('mydata') as db:
    db['key1'] = [1, 2, 3]      # сохраняем список под ключом 'key1'
    db['key2'] = {'a': 10}       # сохраняем словарь

# Открываем и читаем данные
with shelve.open('mydata') as db:
    print(db['key1'])  # [1, 2, 3]
    print(db.get('key2'))  # {'a': 10}
"""
# ===== Модуль collections - namedtuple =====
"""
from collections import namedtuple

# Создаем тип именованного кортежа с обязательными параметрами:
# typename - имя создаваемого типа (строка)
# field_names - имена полей (список/кортеж/строка с пробелами)
Point = namedtuple(typename='Point', field_names=['x', 'y'])

# Дополнительные необязательные параметры функции namedtuple():
# rename=False — автоматически переименовывает поля с недопустимыми именами (по умолчанию False)
# defaults=None — кортеж с значениями по умолчанию для последних N полей
# module=None — имя модуля, которое добавится в атрибут __module__ созданного типа (для отладки и сериализации)

# Пример создания:
Rectangle = namedtuple('Rectangle', 'width height color', rename=True, defaults=(0, 'black'))

# Создаем экземпляр
rect1 = Rectangle(10, 20, 'red')
rect2 = Rectangle(5)  # height=0, color='black' - значения по умолчанию

# Доступ к полям именованного кортежа осуществляется по имени и индексу
print(rect1.width)   # 10
print(rect1[1])      # 20

# Атрибуты именованных кортежей:
# _fields - кортеж с именами полей
print(Rectangle._fields)  # ('width', 'height', 'color')

# _field_defaults - словарь: поле -> значение по умолчанию (если определены)
print(Rectangle._field_defaults)  # {'height': 0, 'color': 'black'}

# Методы:
# _make(iterable) - создает namedtuple из итерируемого объекта
points = Point._make([1, 2])

# _replace(**kwargs) - вернет новый namedtuple с заменой указанных полей
new_rect = rect1._replace(color='blue')

# _asdict() - возвращает OrderedDict с именами и значениями полей
d = rect1._asdict()

# namedtuple — потомок tuple, наследует все методы кортежа и добавляет новые

# Сравнение namedtuple с dict:
# - Читаемость: ✔ у обеих структур
# - Изменяемость: ✘ у namedtuple (immutable), ✔ у dict
# - Память: ✔ у namedtuple (эффективнее), ✘ у dict (больше расход памяти)
# - Производительность: ✔ у namedtuple

# Пример полного использования namedtuple
Car = namedtuple('Car', 'make model year', defaults=['Unknown', 2020])

my_car = Car('Toyota', 'Corolla', 2022)
print(my_car.model)       # Corolla

my_new_car = my_car._replace(year=2025)
print(my_new_car)         # Car(make='Toyota', model='Corolla', year=2025)

# Преобразование в словарь
print(my_car._asdict())   # OrderedDict([('make', 'Toyota'), ('model', 'Corolla'), ('year', 2022)])

# Создание из списка
data = ['Ford', 'Mustang', 1969]
car_from_list = Car._make(data)
print(car_from_list)
"""
# ===== Модуль collections - defaultdict =====
"""
# defaultdict — это подкласс dict из модуля collections.
# Позволяет задавать значение по умолчанию для несуществующего ключа.
# При попытке обращения к отсутствующему ключу вызывается функция, переданная при создании.

from collections import defaultdict

# --- Основной синтаксис ---

# defaultdict(func)
# func — функция без аргументов, возвращающая значение по умолчанию

# для int – число 0
# для float – число 0.0
# для bool – значение False
# для str – пустая строка ''
# для list – пустой список []
# для tuple – пустой кортеж ()
# для set – пустое множество set()
# для dict – пустой словарь {}



# --- Примеры ---

# defaultdict(int) — словарь с целым значением по умолчанию (0)
d = defaultdict(int)
d['a'] += 1       # d['a'] становится 1, не вызывает KeyError

# defaultdict(list) — словарь со списком по умолчанию ([])
d = defaultdict(list)
d['letters'].append('a')
d['letters'].append('b')
# d == {'letters': ['a', 'b']}

# defaultdict(str) — словарь со строкой по умолчанию ('')
d = defaultdict(str)
d['word'] += 'cat'  # d['word'] == 'cat'

# --- Типовые сценарии использования ---

# Подсчет элементов
words = ['a', 'b', 'a']
counter = defaultdict(int)
for w in words:
    counter[w] += 1
# counter == {'a': 2, 'b': 1}

# Группировка по ключу
pairs = [('x', 1), ('y', 2), ('x', 3)]
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
# d == {'x': [1, 3], 'y': [2]}

# Сравнение с обычным dict:
# - не вызывает KeyError при чтении/модификации нового ключа
# - значение для нового ключа сразу создается вызовом функции

# --- Важно помнить ---
# При создании defaultdict обязательно передается функция (например, int, list, set, lambda: значение).
# Если ключ ещё не существует, он автоматически создается при чтении/модификации.
# Значение по умолчанию для нового ключа не копируется, а создается новым вызовом функции.

# --- Практика ---

d = defaultdict(lambda: 'default value')
print(d['abc'])  # 'default value'
d['abc'] = '100'
print(d['abc'])  # 100
"""
# ===== Модуль collections - OrderedDict =====
"""
from collections import OrderedDict # импорт класса OrderedDict
'----------------------'
OrderedDict()
# создание пустого упорядоченного словаря
# сохраняет порядок вставки элементов
'----------------------'
OrderedDict({'a': 1, 'b': 2, 'c': 3})
# создание из обычного словаря
'----------------------'
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# создание из списка пар ключ-значение
'----------------------'
OrderedDict(a=1, b=2, c=3)
# создание с именованными аргументами
'----------------------'
OrderedDict.fromkeys(['a', 'b', 'c'], 0)
# создание из ключей с одинаковым значением по умолчанию
# результат: OrderedDict([('a', 0), ('b', 0), ('c', 0)])
'----------------------'
ordered_dict['new_key'] = value
# добавление нового элемента → помещается в конец
'----------------------'
ordered_dict['existing_key'] = new_value
# изменение существующего ключа → позиция не меняется
'----------------------'
del ordered_dict['key']
ordered_dict['key'] = value
# удаление и повторная вставка → элемент перемещается в конец
'----------------------'
ordered_dict.move_to_end(key, last=True)
# перемещение элемента в конец (last=True) или начало (last=False)
# key — ключ перемещаемого элемента (обязательный)
# last — направление перемещения: True=конец, False=начало
'----------------------'
ordered_dict.move_to_end('first_key', last=False)
# перемещение элемента в начало словаря
'----------------------'
ordered_dict.popitem(last=True)
# удаление и возврат последнего элемента (LIFO - Last In First Out)
# возвращает кортеж (key, value)
'----------------------'
ordered_dict.popitem(last=False)
# удаление и возврат первого элемента (FIFO - First In First Out)
'----------------------'
# ИТЕРИРОВАНИЕ В ПРЯМОМ ПОРЯДКЕ:
for key in ordered_dict:           # перебор ключей
for key, value in ordered_dict.items():  # перебор пар
for key in ordered_dict.keys():    # перебор ключей через метод
for value in ordered_dict.values(): # перебор значений
'----------------------'
# ИТЕРИРОВАНИЕ В ОБРАТНОМ ПОРЯДКЕ:
for key in reversed(ordered_dict):
for key, value in reversed(ordered_dict.items()):
for key in reversed(ordered_dict.keys()):
for value in reversed(ordered_dict.values()):
# функция reversed() поддерживается начиная с Python 3.5 для OrderedDict
'----------------------'
# СОРТИРОВКА ПО КЛЮЧАМ:
for key in sorted(ordered_dict):
    ordered_dict.move_to_end(key)
# перемещение ключей в алфавитном порядке в конец словаря
'----------------------'
# СРАВНЕНИЕ СЛОВАРЕЙ:
OrderedDict([('a', 1), ('b', 2)]) == OrderedDict([('a', 1), ('b', 2)])  # True
OrderedDict([('a', 1), ('b', 2)]) == OrderedDict([('b', 2), ('a', 1)])  # False
# для OrderedDict порядок важен при сравнении!
'----------------------'
OrderedDict([('a', 1), ('b', 2)]) == {'a': 1, 'b': 2}  # True
OrderedDict([('a', 1), ('b', 2)]) == {'b': 2, 'a': 1}  # True  
# при сравнении OrderedDict с dict порядок НЕ важен
'----------------------'
# ОПЕРАТОРЫ ОБЪЕДИНЕНИЯ (Python 3.9+):
dict1 | dict2        # объединение словарей (создание нового)
dict1 |= dict2       # добавление элементов dict2 в dict1
# работает как для dict, так и для OrderedDict
'----------------------'
# НАСЛЕДОВАНИЕ ОТ DICT:
isinstance(OrderedDict(), dict)    # True
issubclass(OrderedDict, dict)     # True
# OrderedDict — подкласс dict, наследует все методы
'----------------------'
# ВСЕ МЕТОДЫ DICT ДОСТУПНЫ:
ordered_dict.get(key, default)    # получение с значением по умолчанию
ordered_dict.setdefault(key, default)  # установка если ключа нет
ordered_dict.pop(key)              # удаление с возвратом значения
ordered_dict.clear()               # очистка словаря
ordered_dict.update(other)         # обновление из другого словаря
ordered_dict.keys()                # представление ключей
ordered_dict.values()              # представление значений
ordered_dict.items()               # представление пар
'----------------------'
# ДОПОЛНИТЕЛЬНЫЙ АТРИБУТ __dict__:
ordered_dict.__dict__['custom_attr'] = value
# или
ordered_dict.custom_attr = value
# добавление пользовательских атрибутов/методов во время выполнения
'----------------------'
# ИСТОРИЧЕСКАЯ СПРАВКА:
# Python 3.6 — dict случайно стал упорядоченным (деталь реализации)
# Python 3.7 — порядок в dict официально гарантирован
# Сейчас OrderedDict в основном нужен для явной сигнализации намерений
'----------------------'
# ПРОИЗВОДИТЕЛЬНОСТЬ OrderedDict vs dict:
# dict быстрее на ~40% 
# dict использует на ~50% меньше памяти
# OrderedDict реализован как двусвязный список в C
'----------------------'
# КОГДА ИСПОЛЬЗОВАТЬ OrderedDict:
# ✔️ Нужно явно показать важность порядка элементов
# ✔️ Требуется изменение порядка элементов (move_to_end)
# ✔️ Нужны LIFO/FIFO операции с popitem()
# ✔️ Важен порядок при сравнении словарей на равенство
# ✔️ Нужно добавить пользовательские атрибуты
# ✔️ Работа с API, где порядок ключей критичен
'----------------------'
# КОГДА НЕ ИСПОЛЬЗОВАТЬ OrderedDict:
# ❌ Просто нужен словарь с сохранением порядка → используйте dict
# ❌ Критична производительность → dict быстрее
# ❌ Ограниченная память → dict экономнее
# ❌ Порядок не важен → обычный dict проще
'----------------------'
# ВАЖНЫЕ ОСОБЕННОСТИ:
# Удаление и повторная вставка перемещает элемент в конец
# reversed() работает с Python 3.5+ для OrderedDict, с Python 3.8+ для dict
# При сравнении OrderedDict учитывает порядок, dict — нет
# Можно добавлять пользовательские методы через __dict__
# Операторы | и |= доступны с Python 3.9
"""
# ===== Модуль collections - Counter =====
'''
# --- Основное ---

# Counter — это подтип dict для подсчета хешируемых объектов.
# В Counter ключ — объект, значение — его количество.

from collections import Counter

# --- Как создать Counter ---

# Передать коллекцию (строку, список, множество...)
c = Counter('abcaabbc')
# Counter({'a': 3, 'b': 3, 'c': 2})

c2 = Counter([1, 2, 2, 3])
# Counter({2: 2, 1: 1, 3: 1})

# Передать dict или именованные аргументы
c3 = Counter({'x': 10, 'y': 5})
c4 = Counter(x=3, y=7)

# --- Преобразование Counter в обычный словарь ---
d = dict(c)
# Counter наследует методы dict (кроме fromkeys, вызовет ошибку)

# --- Методы Counter ---

# update(iterable/словарь) — суммирует значения с существующими (не заменяет)
c.update('abc')        # Counter({'a': 4, 'b': 4, 'c': 3})

# subtract(iterable/словарь) — вычитает значение, не удаляет элементы, даже если < 0
c.subtract({'a': 2, 'b': 2})  # Counter({'a': 2, 'b': 2, 'c': 3})

# most_common([n]) — возвращает n самых частых элементов в виде списка кортежей
print(c.most_common(2))  # [('a', 2), ('b', 2)]

# elements() — итератор по всем элементам (повторяются по их количеству)
print(list(c.elements()))

# total() — сумма всех значений (с Python 3.10)
print(c.total())

# --- Операции между Counter ---

# + и - заменяют update() и subtract()
c1 = Counter(a=2, b=3)
c2 = Counter(a=5, b=1)
print(c1 + c2)  # Counter({'a': 7, 'b': 4})
print(c1 - c2)  # Counter({'b': 2})

# & — пересечение (минимум по каждому ключу)
print(c1 & c2)  # Counter({'a': 2, 'b': 1})

# | — объединение (максимум по каждому ключу)
print(c1 | c2)  # Counter({'a': 5, 'b': 3})

# --- Особенности Counter ---

# Если значение <= 0, оно хранится внутри, но при итерациях и выводе элементов не показывается
c = Counter(a=2, b=-1)
print(c)  # Counter({'a': 2, 'b': -1})

# Counter поддерживает __dict__ — можно динамически добавлять атрибуты

# --- Примеры из практики ---

# Подсчет слов в тексте
sentence = 'apple orange apple banana orange apple'
c = Counter(sentence.split())
print(c.most_common())          # [('apple', 3), ('orange', 2), ('banana', 1)]
print(list(c.elements()))       # ['apple', 'apple', 'apple', 'orange', 'orange', 'banana']
print(c.total())                # 6 (сумма всех слов)

# --- Итог ---

# Counter — мощный инструмент для задач, связанных со статистикой, текстом и повторяющимися объектами.
# Удобнее и короче, чем defaultdict(int) — простота создания, методы для анализа.
# Совместим с dict, но обладает расширенными возможностями для подсчета.
'''
# ===== Модуль collections - ChainMap =====
'''
# --- Основная идея ---

# ChainMap объединяет несколько словарей в один логический словарь.
# Позволяет обращаться к нескольким словарям как к одному, последовательно ищет ключи.

from collections import ChainMap

# --- Создание ---

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)

# --- Особенности доступа ---

print(cm['a'])  # 1, из первого словаря, в котором найден ключ
print(cm['b'])  # 2, значение из первого словаря, даже если в других также есть ключ
print(cm['c'])  # 4, из второго словаря

# Если ключа нет ни в одном из словарей, возникает KeyError

# Безопасный доступ с get()
print(cm.get('d'))       # None, ключ отсутствует
print(cm.get('d', 0))    # 0, значение по умолчанию

# --- Атрибут maps ---

# Внутренний список объединяемых словарей (в порядке поиска)
print(cm.maps)  # [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]

# Можно изменить порядок или добавить словарь, изменяя список maps напрямую


# --- Методы управления цепочкой ---

# new_child(m=None) — возвращает новый ChainMap с добавленным словарем m в начало цепочки
cm2 = cm.new_child({'a': 42, 'd': 10})
print(cm2['a'])  # 42 (из добавленного словаря)

# Если m не передан, новый пустой словарь добавится в начало
cm3 = cm.new_child()
print(cm3.maps[0])  # {}

# parents — новый ChainMap, без первого словаря из текущего
print(cm2.parents)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# --- Изменение значений ---

# Изменения (добавление, обновление, удаление) влияют только на первый словарь в цепочке
cm['a'] = 100
print(dict1['a'])  # 100

# --- Итерация и поведение ключей ---

# Итерирование по ChainMap идет с последнего словаря к первому, 
# при этом при повторяющихся ключах берется первое встреченное значение.

# --- Вывод ---

# ChainMap — удобный способ работать с несколькими словарями как с одним целым,
# полезен для управления конфигурациями, объединения параметров из разных источников,
# реализации стеков областей видимости и т.п.

# Рекомендуется использовать get() для безопасного доступа к ключам,
# так как прямое обращение к отсутствующему ключу вызывает KeyError.
'''
# ===== Модуль array  (массивы) =====
'''
import array as arr

# --- Основное о методах ---

# Методы массива практически такие же, как у списков:
# append(), extend(), insert(), remove(), pop(), index(), count(), reverse(), sort() и т.д.
# Поэтому не описываем их подробно — работают так же, как для list.

# --- Отличия и важные моменты ---

# Все элементы массива должны быть одного типа, заданного параметром typecode.
# При добавлении элемента несовместимого типа возникает ошибка TypeError.
# Массивы эффективнее по памяти и скорости, чем списки с одинаковыми типами элементов.

# --- Полный список typecode, поддерживаемых в модуле array ---

# 'b' — signed char (int), 1 байт
# 'B' — unsigned char (int), 1 байт
# 'u' — wchar_t (символ Unicode), 2 байта (размер зависит от платформы)
# 'h' — signed short (int), 2 байта
# 'H' — unsigned short (int), 2 байта
# 'i' — signed int (int), 2 или 4 байта (зависит от платформы)
# 'I' — unsigned int (int), 2 или 4 байта
# 'l' — signed long (int), 4 байта
# 'L' — unsigned long (int), 4 байта
# 'q' — signed long long (int), 8 байт
# 'Q' — unsigned long long (int), 8 байт
# 'f' — float (float), 4 байта
# 'd' — double (float), 8 байт

# --- Создание массива с typecode ---

numbers = arr.array('i', [1, 2, 3])  # массив целых чисел
floats = arr.array('d', [1.0, 2.0, 3.5])  # массив чисел с плавающей точкой

# --- Пример ошибки при несоответствии ---

try:
    numbers.append(4.5)  # Ошибка, т.к. float нельзя добавить в int-массив
except TypeError as e:
    print(e)

# --- Краткое напоминание ---

# Используйте массивы, когда важна оптимизация по памяти и производительности для однородных данных.
# Методы похожи на списковые, но обязательно соблюдайте ограничение на тип элементов.
'''
# ===== Обработка исключений =====
'''


# модуль 7.1 Категории ошибок
# - Синтаксические — нарушение правил синтаксиса; ловит интерпретатор на этапе парсинга.
# - Логические — программа выполняется, но результат неверный; интерпретатор их не показывает автоматически.
# - Ошибки времени выполнения (исключения) — возникают во время исполнения при некорректных данных/ресурсах.



# модуль 7.2 Конструкция try-except (базовый шаблон)
try:
    # контролируемый код
    ...
except ExceptionType:
    # обработка ошибки
    ...

# Несколько обработчиков:
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
# Можно один except для нескольких типов:
try:
    ...
except (KeyError, IndexError):
    ...

# Частые встроенные исключения (примеры возникновения):
# IndexError        — выход за границы последовательности
# KeyError          — нет ключа в словаре
# NameError         — имя не определено
# SyntaxError       — синтаксическая ошибка (ловится не в рантайме блока try)
# TypeError         — операция с несовместимым типом
# FileNotFoundError — файл не найден
# ValueError        — аргумент некорректного значения
# ZeroDivisionError — деление на ноль



# модуль 7.3 Блоки else и finally

# else выполняется ТОЛЬКО если в try не было исключения:
try:
    x = int("42")
except ValueError:
    print("bad int")
else:
    print("ok:", x)

# finally выполняется ВСЕГДА (был исключение или нет):
try:
    f = open("data.txt", "w", encoding="utf-8")
    f.write("hello")
except OSError:
    print("io error")
finally:
    # гарантированное освобождение ресурсов
    try:
        f.close()
    except Exception:
        pass

# Общий полный шаблон:
try:
    ...
except TypeA:
    ...
except TypeB:
    ...
else:
    ...
finally:
    ...

    

# модуль 7.4 Иерархия и работа с объектом исключения


BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning


# Базовые классы:
# BaseException — корень дерева исключений.
# Exception     — базовый класс для пользовательских исключений; от него наследоваться.


# Проверка наследования:
issubclass(ZeroDivisionError, Exception)  # True


# Получение сгенерированного объекта исключения:
try:
    1 / 0
except ZeroDivisionError as exc:
    # exc — объект исключения; у него есть атрибуты/методы, см. dir(exc)
    msg = str(exc)

# Генерация исключений: raise
# Формы:

#1 raise <КлассИсключения>()
#  raise ValueError('Oпиcaниe исключения')

#2 raise <ЭкземплярИсключения>
#  raise ValueError                       # эквивалентно: raise ValueError()

#3 raise <НовыйКласс> from <исходная_ошибка>   # связывание причин
#  try:
#      х = 1 / 0
#  except Exception as err:
#     raise ZeroDivisionError('Описание исключения') from err

#4 просто 'raise' внутри except — проброс текущего исключения
#  try:
#      х = 1 / 0
#  except Exception as err:
#      print(err)                  # каким-то образом обработали перехваченное исключение
#      raise                       # пробрасываем исключение выше


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("b must be non-zero")
    return a / b

# Конструкторы исключений принимают аргументы через *args:
try:
    raise ValueError("bad value", 123)
except ValueError as e:
    args = e.args  # ('bad value', 123)



# модуль 7.5 — Методики LBYL и EAFP + свои исключения и assert

# Свои исключения (всегда наследуемся от Exception)
class ConfigError(Exception):
    pass


# LBYL — Look Before You Leap («посмотри перед прыжком»)
# Сначала проверяем, потом делаем действие.
data = {'Timur': 29, 'Ivan': 54}

# Хотим увеличить счётчик для ключа 'Anri'
# Прямой код вызовет KeyError:
# data['Anri'] += 1

# LBYL-способ:
if 'Anri' in data:
    data['Anri'] += 1
else:
    print('Ключ Anri отсутствует в словаре.')

# Аналогия: посмотрели на светофор — только потом идём.


# EAFP — Easier to Ask Forgiveness than Permission («проще извиниться, чем спрашивать разрешение»)
# Сразу выполняем, ошибки ловим по факту.
data = {'Timur': 29, 'Ivan': 54}

try:
    data['Anri'] += 1
except KeyError:
    print('Ключ Anri отсутствует в словаре.')

# В Python чаще используют именно EAFP: код короче, читается лучше,
# и обработка выполняется только при реальной ошибке.


# Третий удобный вариант — метод get() без исключений:
data = {'Timur': 29, 'Ivan': 54}
data['Anri'] = data.get('Anri', 0) + 1  # если ключа нет, берём 0 и инкрементим


# Где годится LBYL, а где EAFP?
# - LBYL: проверки дешёвые и помогают явно документировать условия (валидация ввода, наличие ключа, формат).
# - EAFP: «счастливый путь» — просто делаем; исключения редки и должны обрабатываться точечно.


# Пример с собственным исключением (делаем понятное сообщение домена)
def load_required(cfg):
    if 'HOST' not in cfg:
        raise ConfigError('HOST отсутствует в конфиге')
    try:
        port = int(cfg['PORT'])
    except (KeyError, ValueError) as err:
        # сохраняем первопричину
        raise ConfigError('Некорректный PORT') from err
    return cfg['HOST'], port


# assert — быстрые проверки во время разработки
# Если условие ложно, поднимается AssertionError с сообщением.
def normalize_prob(p):
    assert 0.0 <= p <= 1.0, 'p должен быть в диапазоне [0, 1]'
    return p


# Короткие памятки:
# - Свои исключения: наследуй от Exception и давай понятные сообщения.
# - Для отсутствующих ключей удобно: d.get(k, default) или EAFP с try/except.
# - LBYL делает код многословнее, но прозрачнее по условиям.
# - EAFP делает код компактным; не злоупотребляй пустыми except.
# - assert оставляй для инвариантов и отладки (в продакшене может быть выключен).




Общее:
# Практические заметки
# - В блоках except перехватывайте только те типы, которые действительно ожидаете.
# - Сначала более узкие исключения, затем более общие (Exception/ BaseException — крайний случай).
# - Используйте else для кода, который должен выполняться только при отсутствии ошибок.
# - Используйте finally для освобождения ресурсов (файлы, соединения, блокировки).
# - Для многоуровневых обработок применяйте 'raise from', чтобы не терять первопричину.
# - Пользовательские исключения помогают сделать ошибки домена явно различимыми.

# Контекстный менеджер лучше finally, но знание finally обязательно:
# with open(path) as f: ...   # под капотом тот же принцип освобождения ресурсов


'''
# ===== Рекурсия =====
'''
# 8.1 Базовые понятия

# Рекурсивная функция — функция, которая вызывает саму себя.
# Идея решения:
# 1) Если задачу можно решить сразу — решаем (базовый случай).
# 2) Иначе сводим задачу к такой же, но меньшего размера (рекурсивный случай) и вызываем функцию снова.
# С каждым вызовом размер задачи уменьшается — в итоге достигаем базового случая.

# Базовый случай и рекурсивный случай — два обязательных элемента корректной рекурсии.
# Глубина рекурсии — сколько раз функция вызвала сама себя до возврата.
# Хвостовая рекурсия — частный случай, когда рекурсивный вызов стоит последним действием функции.

# Пример: факториал n! = 1 * 2 * ... * n
def fact(n):
    if n <= 1:          # базовый случай
        return 1
    return n * fact(n-1)  # рекурсивный случай

# Пример: сумма цифр
def sum_digits(x):
    if x < 10:
        return x
    return x % 10 + sum_digits(x // 10)

# 8.2 Практика оформления рекурсии

# Важно:
# - Всегда иметь корректный базовый случай (или несколько).
# - На каждом шаге приближаться к базе (уменьшать размер задачи).
# - Не дублировать тяжёлые вычисления без необходимости (см. мемоизация ниже).

# Пример: двоичное представление числа
def to_binary(n):
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)

# 8.3 Мемоизация

# Мемоизация — сохранение результатов вызовов функции для повторного использования.
# В Python удобно применять декоратор lru_cache из functools.
from functools import lru_cache

@lru_cache(maxsize=None)   # кэш не ограничен, хранит все рассчитанные аргументы
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Польза:
# - Резко ускоряет рекурсивные алгоритмы с перекрывающимися подзадачами (Фибоначчи, пути в сетке и т.п.).
# Замечание:
# - Кэш работает по аргументам функции; аргументы должны быть хешируемыми.
# - Кэширует только результаты чистой функции (без побочных эффектов).

# Рекурсия допустима и в лямбда-функциях, но читаемость обычно хуже.
# При необходимости используйте именованную функцию или технику присваивания имени лямбде.

# 8.4 Лимит рекурсии

# sys.getrecursionlimit() — узнать текущий лимит глубины рекурсии.
# sys.setrecursionlimit(n) — установить новый лимит (делайте это осознанно).
import sys

cur = sys.getrecursionlimit()
# print(cur)

# Повышать лимит стоит только при реальной необходимости и понимании рисков:
# - Чрезмерный лимит может привести к переполнению стека и крашу процесса.
# - Если можно — перепишите алгоритм итеративно или примените мемоизацию/динамику.

# Пример аккуратного увеличения:
def safe_set_limit(target):
    # Мягкая проверка, чтобы не поднимать слишком высоко
    if target < 1000 or target > 100000:
        return
    sys.setrecursionlimit(target)

# Практические советы

# - Начинайте с формулировки базы и уменьшения задачи.
# - Проверяйте граничные случаи (n = 0, пустые структуры, единичные элементы).
# - Для задач с повторными подвычислениями используйте lru_cache.
# - Если получаете RecursionError — проверьте, действительно ли на каждом шаге приближаетесь к базе.
# - При больших глубинах предпочитайте итерации или стек вручную.

# Мини-шаблон рекурсивной функции
def solve(task):
    if is_base(task):
        return base_result(task)
    sub = shrink(task)         # уменьшили задачу
    partial = solve(sub)       # рекурсивный вызов
    return combine(task, partial)
'''
# ===== Функция format() и мини-язык спецификаций =====
'''

# Сигнатура: format(value, format_spec='')
# Возвращает строку — отформатированное представление value по правилам format_spec.
# Эквивалентно вызовам f-строк: f'{value:format_spec}'.

# Общий шаблон format_spec (порядок важен):
# [[fill]align][sign][z][#][0][width][grouping][.precision][type]
# где:
#   fill         — символ заполнения (любой, по умолчанию пробел)
#   align        — выравнивание: < (влево) | > (вправо) | ^ (по центру) | = (знак/префикс слева, цифры выравниваются нулями)
#   sign         — знак для чисел: + | - | пробел
#   z            — для float (Py 3.11+): превращает -0.0 в +0.0 после округления
#   #            — альтернативная форма (для int/float/complex)
#   0            — нулевое заполнение; эквивалентно fill='0' при align='='
#   width        — минимальная ширина поля (целое)
#   grouping     — разделители групп: ',' (запятая) или '_' (подчёркивание)
#   .precision   — точность: для float — количество знаков; для строк — максимум символов
#   type         — тип представления (см. ниже)

# Типы представления (type):
#   s  — строка (по умолчанию для str)
#   d  — десятичное целое
#   b  — двоичное целое
#   o  — восьмеричное целое
#   x  — шестнадцатеричное нижним регистром
#   X  — шестнадцатеричное верхним регистром
#   c  — символ по коду Unicode из int
#   n  — как d/f/g, но учитывает локаль при выводе числа
#   e/E — экспоненциальная форма (нижний/верхний регистр)
#   f/F — фиксированная форма (нижний/верхний регистры обозначения NaN/Inf)
#   g/G — «общая» форма (короче из f/e), обрезает/оставляет нули; с альтернативной формой # не обрезает
#   %  — умножает на 100 и добавляет знак процента; точность как у f

# Альтернативная форма (#):
#   Для целых: добавляет префиксы систем счисления (0b, 0o, 0x/0X).
#   Для float/complex: гарантирует наличие десятичной точки; для g/G не обрезает конечные нули.

# Выравнивание и заполнение:
#   '{v:>10}'  — вправо в поле ширины 10
#   '{v:<10}'  — влево; '{v:^10}' — по центру
#   '{v:=+010}' — знак/префикс слева, остальное нулями (полезно для чисел)
#   Символ заполнения указывается перед align: '{v:_>10}' заполняет слева '_'

# Знаки для чисел:
#   '+' — всегда показывать; '-' — только отрицательные (по умолчанию); ' ' — пробел для положительных
#   Примеры: '{x:+d}', '{x: d}', '{x:-d}'

# Группировка разрядов:
#   '{n:,}'  — 1,234,567
#   '{n:_}'  — 1_234_567
#   В f-строках и str.format работает одинаково.

# Точность:
#   Для float: количество знаков (для f — после точки; для g — значащих)
#   '{pi:.2f}' → '3.14', '{pi:.6g}' → '3.14159'
#   Для строк: максимум символов '{s:.3}' → берёт первые 3

# Важные замечания:
# - Нулевое заполнение '0' действует как fill='0' и align='=' для чисел.
# - Фигурные скобки как литералы в f-строках/str.format нужно экранировать удвоением: '{{' или '}}'.
# - В самой функции format() ограничение на fill='{'/'}' не действует (но это редко нужно).
# - Типы e/E/f/F/g/G применимы к числам с плавающей точкой и complex (для complex форматируется каждая часть).

# Быстрые эквиваленты:
#   f'{v:spec}'  <=>  format(v, 'spec')
#   '{:spec}'.format(v)  <=>  format(v, 'spec')

# Примеры (копируй, запускай):
n = 1000
pi = 1000.5368
s  = 'Привет'

# Системы счисления и префиксы
print(format(26, 'b'))     # 11010
print(format(26, '#b'))    # 0b11010
print(format(26, 'X'))     # 1A
print(format(26, '#06x'))  # 0x001a  (ширина 6, нули)

# Ширина/выравнивание/заполнение
print(format(42, '*>8d'))   # ******42 (вправо, заполнитель '*')
print(format(42, '*<8d'))   # 42****** (влево)
print(format(3.14, '^10.1f'))  #   3.1    

# Знаки
print(format(42, '+d'))     # +42
print(format(-42, ' d'))    # -42  (пробел влияет только на положительные)

# Группировка разрядов
print(format(n, '10,d'))    # '     1,000'
print(format(n, '10,_'))    # '     1_000'

# Точность и тип
print(format(pi, '.2f'))     # 1000.54 (округление)
print(format(pi, '.6g'))     # 1000.54 (значащих цифр)
print(format(0.125, '.2%'))  # 12.50%

# Строки: усечение и выравнивание
print(format(s, '>10.3'))    # '       При'
print(format('ok', '*^8'))   # '**ok****'

# Специальный флаг z (Py 3.11+)
neg_zero = -0.0
print(format(neg_zero, 'z'))      # '0.0' (отрицательный ноль стал положительным)
print(format(neg_zero, 'zf'))     # '0.000000'

# Практические паттерны
# - Деньги/комма: '{:,.2f}'.format(amount)
# - Проценты: '{:.1%}'.format(ratio)
# - Hex dump: '{:02X}'.format(byte)
# - Выравнивание колонок: f'{name:<20}{value:>10,.2f}'

# Частые ошибки
# - Неправильный порядок компонентов спецификатора — соблюдай шаблон.
# - Путаница 0 и =: для «нулями внутри, знак слева» используй '=' (например, '0=+10d').
# - Попытка применить точность к целым: .precision для int не используется (исключение — %).

# Справка под рукой (мини-напоминалка):
#   '{val:[fill][align][sign][z][#][0][width][,/_][.prec][type]}'
#   align: < > ^ =
#   type:  s d b o x X c n e E f F g G %
#   grouping: ',' или '_'
#   примеры: '{n:#010X}', '{x:>8}', '{pi:,.2f}', '{rate:.1%}', '{txt:.5}'
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
"""
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
"""
# 16
"""
import json

with open('food_services.json','r',encoding='utf-8') as file:
    file = json.load(file)

res = {}

for row_dict in file:
    if row_dict['TypeObject'] not in res or (row_dict['SeatsCount'] > res[row_dict['TypeObject']][0]):
        res[row_dict['TypeObject']] = (row_dict['SeatsCount'], row_dict['Name'])

[print(key,f'{value[1]}, {value[0]}', sep=': ') for key,value in sorted(res.items())]
"""
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
"""
from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    res = []
    for file in zip_file.infolist():
        if not file.is_dir() and file.date_time > (2021, 11, 30, 14, 22, 0):
            res.append(file.filename)
    print(*sorted([s.split("/")[1] if "/" in s else s for s in res]), sep='\n')
"""
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
"""
from zipfile import ZipFile

file_names = ['best_scores.json', 'exam_results.csv']

with ZipFile('files.zip','w') as file_zip:
    for name in file_names:
        file_zip.write(name)
"""
# 7
"""
from zipfile import ZipFile, ZipInfo

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip','w') as file_zip:
    for name in file_names:
        if 100 >= ZipInfo.from_file(name).file_size:
            file_zip.write(name)
"""
# 8
"""
from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as file_zip:
        file_zip.extractall(members=args or None)
"""
# 9
"""
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
"""
# 10
"""
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
            """
# 4.6
# 2
"""
import pickle, sys

with open(input(),'rb') as file:
    my_func = pickle.load(file)

args = [line.strip() for line in sys.stdin]
print(my_func(*args))
"""
# 3
"""
import pickle

def filter_dump(filename, objects, typename):
    filtered = [i for i in objects if type(i) == typename]
    with open(filename, 'wb') as file_w:
        pickle.dump(filtered, file_w)


filter_dump('numbers.pkl', [1, '2', '3', '3', '3', 4, '5'], int)

with open('numbers.pkl','rb') as file:
    print(pickle.load(file))
"""
# 4
"""
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
"""
# 4.7 Модуль os
# === Практика ===
"""
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
"""
# A (задания с сайта - https://ejudge.179.ru/tasks/python/2027b/27-os.html)
"""
import os

os.chdir("C:/Users/user/Desktop/coding/git-lessons/Primates/Haplorrhini/Simiiformes/Platyrrhini/Callitrichinae")
res_files = [file for file in os.listdir() if os.path.isfile(file)]
print(*sorted(res_files), sep='\n')
"""
# B
"""
import os

os.chdir('Primates')

while len([name for name in os.listdir() if os.path.isdir(name)]) > 0:
    os.chdir(min([name for name in os.listdir() if os.path.isdir(name)]))

print( os.path.dirname(os.path.join(os.getcwd(), min([name for name in os.listdir() if os.path.isfile(name)]))))
"""
# C
"""
import os

def find_file(file_name):
    for root, dirs, files in os.walk('C:/Users/user/Desktop/coding/git-lessons/Primates'):
        if file_name in files:
            with open(os.path.join(root,file_name)) as file:
                print(file.read().strip())
            break

find_file('Homo_sapiens.txt')
"""
# D
"""
import os

def find_file(file_name):
    for root, dirs, files in os.walk('C:/Users/user/Desktop/coding/git-lessons/Primates'):
        if file_name in files:
            print('Primates' + os.path.join(root,file_name).split('Primates')[1].replace('\\','/'))
            break
        

find_file('Homo_sapiens.txt')
"""
# E
"""
import os

res_files = []
for root, dirs, files in os.walk('Primates'):
    [res_files.append(file) for file in files]

print(*sorted(res_files), sep='\n')
"""
# F
"""
import os

for root, dirs, files in os.walk('Primates'):
    dirs.sort()
    print(root.replace('\\', '/'))
"""
# G
"""
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
"""
# H
"""
import os

res = []
for root, dirs, files in os.walk('Primates/Strepsirrhini/Lorisiformes/Lorisidae'):
    for file in files:
        with open(os.path.join(root,file)) as file_r:
            res.append(file_r.read().strip()) 

print(*sorted(res), sep='\n')
"""
# 4.7 Модуль shutil
# rmtree(path) — рекурсивное удаление директории
"""
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
"""
# copyfile(src, dst) - копирование содержимое одного файла в другой наиболее эффективным способом без переноса метаданных
"""
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
"""
# copy(src, dst) — копирование файла с правами доступа
"""
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
"""
# copy2(src, dst) — копирование файла с всеми метаданными
"""
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
"""
# copytree(src, dst) — рекурсивное копирование директории
"""
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
"""
# which(cmd) — поиск пути к исполняемому файлу
"""
# Ищет исполняемый файл cmd в системной переменной PATH.
# Возвращает полный путь к найденному файлу или None, если файл не найден.
# По умолчанию ищет только существующие и исполняемые файлы (mode=os.F_OK | os.X_OK).
# Учитывает расширения из PATHEXT на Windows.
# Можно явно задать переменную среды поиска (path).


import shutil

print(shutil.which('python'))
print(shutil.which('git'))
print(shutil.which('aaaaaaaa'))
"""
# disk_usage(path) — статистика использования диска
"""
# Возвращает общий, используемый и свободный объем дискового пространства по указанному пути.
# Путь может быть файлом или каталогом.
# Результат представлен в виде именованного кортежа с атрибутами total, used и free (в байтах).
# Поддерживается на Unix и Windows системах.


import shutil

print(shutil.disk_usage('.'))
"""
# move(src, dst) — перемещение файла или каталога
"""
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
"""
# make_archive() — создание архива
"""
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
"""
# get_archive_formats() / get_unpack_formats() — получение форматов архивов
"""
# get_archive_formats() возвращает список поддерживаемых форматов для создания архивов.
# Каждый элемент — кортеж (name, description) с именем формата и описанием.
# get_unpack_formats() возвращает список форматов для распаковки архивов.
# Каждый элемент — кортеж (name, extensions, description), где extensions — список расширений файлов.
# По умолчанию доступны форматы: zip, tar, gztar, bztar, xztar.
# Позволяет узнать, какие форматы поддерживает ваш текущий Python и платформа.

import shutil

print(*shutil.get_archive_formats(), sep='\n')
print(*shutil.get_unpack_formats(), sep='\n')
"""

# Модуль 6.2
# 17
"""
from string import ascii_letters

en_translator = str.maketrans(ascii_letters, input()*2)

print(input().translate(en_translator))
"""
# Модуль 6.4
# 10
"""
import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ('name,family,sex,color'))

with open('data.pkl', 'rb') as file_pkl:
    for animal in pickle.load(file_pkl):
        print(f"name: {animal.name}\nfamily: {animal.family}\nsex: {animal.sex}\ncolor: {animal.color}\n")
"""
# 11
"""
from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]


users = sorted(users, key=lambda x: (['Gold','Silver','Bronze','Basic'].index(x.plan), x.email))
for user in users:
    print(f"{user.name} {user.surname}\n  Email: {user.email}\n  Plan: {user.plan}\n")
"""
# 12
"""
import csv
from datetime import datetime

with open('meetings.csv', 'r', encoding='UTF-8') as file_csv:
    file_csv = list(csv.reader(file_csv, delimiter=','))
    del file_csv[0]

file_csv = sorted(file_csv, key=lambda x: (datetime.strptime((x[2]+'.'+x[3]),'%d.%m.%Y.%H:%M')))
[print(x[0], x[1]) for x in file_csv]
"""
# Модуль 6.5
# 17
"""
from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

data_new = defaultdict(int)

for key,value in data:
    data_new[key] += value

[print(f"{key}: ${value}") for key,value in sorted(data_new.items())]
"""
# 18
"""
from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

staff_new = defaultdict(int)

for key,value in staff:
    staff_new[key] += 1

[print(f"{key}: {value}") for key,value in sorted(staff_new.items())]
"""
# 19
"""
from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]

staff = defaultdict(set)

for key,value in staff_broken:
    staff[key].add(value)

[print(f"{key}: {', '.join(sorted(value))}") for key,value in sorted(staff.items())]
"""
# 20
"""
from collections import defaultdict

def wins(pairs):
    winners = defaultdict(set)
    for key,value in pairs:
        winners[key].add(value)
    return winners
"""
# 21
"""
from collections import defaultdict

def flip_dict(dict_of_lists):
    res = defaultdict(list)
    for key,values in dict_of_lists.items():
        for value in values:
            res[value].append(key)
    return res
"""
# 22
"""
from collections import defaultdict

def best_sender(messages, senders):
    res = defaultdict(int)
    for i in range(len(messages)):
        res[senders[i]] += len(messages[i].split())
    return max(res, key=lambda x: (res[x],x))
"""
# Модуль 6.6
# 16
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

[data.move_to_end(key, last=False) for key in list(data.keys())]

print(data)
"""
# 17
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()

rule = False
for _ in range(len(data)):
    key,value = data.popitem(last=rule)
    new_data[key] = value
    rule = not rule

print(new_data)
"""
# 18
"""
from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    for key,value in sorted(ordered_dict.items(), key=lambda x: x[by_values]):
        ordered_dict.move_to_end(key)
"""
# Модуль 6.7
# 14
"""
from collections import Counter

files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

for i in range(len(files)):
    files[i] = files[i].split('.')[1]

counter = Counter(files)

[print(f"{key}: {value}") for key,value in sorted(counter.items())]
"""
# 15
'''
from collections import Counter


def count_occurences(word, words):
    return Counter(words.lower().split())[word.lower()]


word = "python"
words = "Python Conferences python training python events"

print(count_occurences(word, words))
'''
# 16
'''
from collections import Counter

counter = Counter(input().split(','))
[print(f"{key}: {value}") for key,value in sorted(counter.items())]
'''
# 17
'''
from collections import Counter

counter = Counter(input().split(','))

for key,value in sorted(counter.items()):
    cost = sum([ord(i) for i in key.replace(' ','')])
    whitespaces = len(max(counter, key=len))-len(key)
    print(f"{key}{' ' * whitespaces}: {cost} UC x {value} = {cost*value} UC")
'''
# 18
'''
from collections import Counter

counter = Counter()
with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        counter.update(filter(str.isalpha, line.strip().lower()))

[print(f"{key}: {value}") for key,value in sorted(counter.items())]
'''
# Модуль 6.8
# 11
'''
from collections import Counter

print(Counter(input().lower().split()).most_common()[0][0])
'''
# 12
'''
from collections import Counter

counter = Counter(input().lower().split())
min_k = counter.most_common()[-1][1]
res = [word for word in filter(lambda x: counter[x]==min_k, counter)]
print(*sorted(res), sep=', ')
'''
# 13
'''
from collections import Counter

counter = Counter(input().lower().split())
max_k = max(counter.values())
res = [word for word in filter(lambda x: counter[x]==max_k, counter)]
print(sorted(res)[-1])
'''
# 14
'''
from collections import Counter

s = [len(word) for word in input().split()]
counter = Counter(s)
[print(f"Слов длины {key}: {value}") for key,value in sorted(counter.items(), key=lambda x: x[1])]
'''
# 15
'''
import sys
from collections import Counter

counter = Counter()
for s in sys.stdin:
    s = s.split()
    counter.update({s[0]: int(s[1])})

print(counter.most_common()[-2][0])
'''
# 16
'''
from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: list(filter(lambda x: x[1] == min(data.values()), data.items()))
data.__dict__['max_values'] = lambda: list(filter(lambda x: x[1] == max(data.values()), data.items()))

print(data.max_values())
'''
# 17
'''
from collections import Counter
import csv

with open('name_log.csv','r',encoding='utf-8') as file:
    file = list(csv.reader(file, delimiter=','))
    del file[0]

counter = Counter([x[1] for x in file])
[print(f"{key}: {value}") for key,value in sorted(counter.items())]
'''
# 18
'''
from collections import Counter

def scrabble(symbols, word):
    return Counter(symbols.lower()) >= Counter(word.lower())
'''
# 19
'''
from collections import Counter

def print_bar_chart(data, mark):
    counter = Counter(data)
    whitespaces = len(max(counter.keys(), key=len))

    [print(f"{key}{' '*(whitespaces-len(key))} |{value*mark}") for key,value in counter.most_common()]
'''
# 20
'''
from collections import Counter
import csv, json

counter = Counter()

for i in range(1,4+1):
    with open(f"quarter{i}.csv",'r',encoding='utf-8') as file:
        file = list(csv.reader(file,delimiter=','))
        del file[0]
        for s in file:
            for i in range(1,3+1):
                counter.update({s[0]: int(s[i])})

with open('prices.json','r',encoding='utf-8') as file_json:
    file_json = json.load(file_json)

print(sum([counter[key]*file_json[key] for key in counter.keys()]))
'''
# 21
'''
from collections import Counter

have_books = Counter(input().split())
earned_money = 0

for _ in range(int(input())):
    book_number, cost = input().split()
    if have_books[book_number] >= 1:
        have_books[book_number] -= 1
        earned_money += int(cost)

print(earned_money)
'''
# Модуль 6.9
# 21
'''
from collections import ChainMap
import json

with open('zoo.json','r',encoding='utf-8') as file:
    file = json.load(file)

animals = ChainMap(*file)

print(sum(animals.values()))
'''
# 22
'''
from collections import ChainMap, Counter    

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread,meat,sauce,vegetables,toppings)

s = Counter(input().split(','))
whitespaces = len(max(s, key=len))
total_price = 0
len_dash = 0

for ingredient in sorted(s):
    line_for_print = f"{ingredient:{whitespaces}} x {s[ingredient]}"
    len_dash = max(len_dash, len(line_for_print))
    print(line_for_print)
    total_price += ingredients[ingredient] * s[ingredient]

len_dash = max(len_dash, len(f"ИТОГ: {total_price}р"))
print('-'*len_dash)
print(f"ИТОГ: {total_price}р")
'''
# Модуль 6.10
# 12
'''
from collections import ChainMap

def get_all_values(chainmap, key):
    res = set()
    for d in chainmap.maps:
        try:
            res.add(d[key])
        except:
            continue
    return res

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)
'''
# 13
'''
from collections import ChainMap

def deep_update(chainmap, key, value):
    if key in chainmap:
        for d in chainmap.maps:
            if key in d:
                d[key]=value
    else:
        chainmap[key] = value
'''
# 14
'''
from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()
    return chainmap.get(key)
    '''
# Модуль 7.2
# 23
'''
import sys

res, k = 0, 0

for line in sys.stdin:
    try:
        if float(line)%1==0:
            res += int(line)
        else:
            res += float(line)
    except:
        k += 1

print(res)
print(k)
'''
# Модуль 7.3
# 19
'''
import calendar

try:
    months = dict(zip(range(1,13), calendar.month_name[1:]))
    print(months[int(input())])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
'''
# Модуль 7.4 
# 17
'''
def get_weekday(number):
    if type(number) is not int:
        raise TypeError('Аргумент не является целым числом')
    if not 1<=number<=7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    
    week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }
    return week[number]
'''
# 18
'''
def get_id(names, name):
    if type(name) is not str:
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    
    return len(names)+1
'''
# 19
'''
import json

try:
    with open(input(), 'r', encoding='utf-8') as file_json:
        file_json = json.load(file_json)
        print(file_json)
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')
'''
# Модуль 7.5 
# 6
'''
def is_good_password(string):
    if len(string) >= 9 and string != string.lower() and string != string.upper() and any(i.isdigit() for i in string):
        return True
    else:
        return False
'''
# 7
'''
class LengthError(Exception):
    pass
class LetterError(Exception):
    pass
class DigitError(Exception):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if string == string.lower() or string == string.upper():
        raise LetterError
    if not any(i.isdigit() for i in string):
        raise DigitError
    return True
'''
# 8
'''
class LengthError(Exception):
    pass
class LetterError(Exception):
    pass
class DigitError(Exception):
    pass

def is_good_password(string):
    if len(string) < 9:
        return 'LengthError'
    if string == string.lower() or string == string.upper():
        return 'LetterError'
    if not any(i.isdigit() for i in string):
        return 'DigitError'
    return 'Success!'


flag = True
while flag:
    res = is_good_password(input())
    print(res)
    if res == 'Success!':
        flag = False
'''
# Модуль 8.2
# 6
'''
numbers = [243, -279, 395, 130, 89]

def print_numbers(numbers):
    end = len(numbers)
    def res(step):
        if step < end:
            print(f"Элемент {step}: {numbers[step]}")
            res(step+1)
    res(0)

print_numbers(numbers)
'''
# 7
'''
def rec(num):
    if num != 0:
        rec(int(input()))
    print(num)
rec(int(input()))
'''
# 8
'''
def triangle(h):
    if h > 0:
        print('*' * h)
        triangle(h-1)
'''
# 9
'''
def triangle(h):
    def rec(step):
        if step <= h:
            print('*' * step)
            rec(step+1)
    rec(1)
'''
# 10
'''
def sand_timer(max_num):
    def rec(step):
        if step < max_num:
            print(f"{str(step) * (max_num*4-4*(step-1))}".center(max_num*4))
            rec(step+1)
        print(f"{str(step) * (max_num*4-4*(step-1))}".center(max_num*4))
    rec(1)

sand_timer(4)
'''
# 11
'''
def print_digits(number):
    if number:
        print(number%10)
        print_digits(number//10)



print_digits(12345)
'''
# 12
'''
def print_digits(number):
    def rec(step):
        if step >= 0:
            print(number // int('1'+'0'*step) % 10 )
            rec(step-1)
    rec(len(str(number))-1)


print_digits(12345)
'''
# Модуль 8.3
# 5
'''
def len_for_gay(number):
    if number < 10:
        return 1
    return 1 + len_for_gay(number//10)

print(len_for_gay(123456))
'''
# 6
'''
def sum_for_gay(number):
    if number < 10:
        return number
    return number%10 + sum_for_gay(number//10)

print(sum_for_gay(int(input())))
'''
# 7
'''
def number_of_frogs(year):
    if year == 1:
        return 77
    return 3*(number_of_frogs(year-1)-30)
'''
# 8
'''
def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    return numbers[start] + range_sum(numbers, start+1, end)
'''
# 9
'''
def get_pow(a, n):
    if n == 0:
        return 1
    return a*get_pow(a, n-1)
'''
# 10
'''
def get_fast_pow(a, n):
    if n == 0:
        return 1
    elif n%2==0:
        return get_fast_pow(a*a, n//2)
    else:
        return a*get_fast_pow(a, n-1)

print(get_fast_pow(2, 10))
'''
# 11
'''
def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a+1, b-1)
'''
# 12
'''
def is_power(number):
    print(number)
    if number <= 2:
        return True
    elif number > 2 and number%1!=0:
        return False
    return is_power(number/2)


print(is_power(512))
'''
# 13
'''
def tribonacci(n):
    cache = {1:1, 2:1, 3:1}
    def rec(step):
        if step in cache:
            return cache[step]
        cache[step] = rec(step-3) + rec(step-2) + rec(step-1)
        return cache[step]
    return rec(n)

print(tribonacci(4))
'''
# 14
'''
def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])

print(is_palindrome('levelll'))
'''
# 15
'''
def to_binary(number):
    if number < 2:
        return str(number)
    return to_binary(number//2) + str(number%2)

print(to_binary(16))
'''
# 16
'''
def accordion(n):
    if n > 0:
        print(n)
        accordion(n-5)
    print(n)

accordion(int(input()))
'''
# Модуль 8.4
# 3
'''
def recursive_sum(nested_lists):
    sum_mas = 0
    for elem in nested_lists:
        if type(elem) is int:
            sum_mas += elem
        elif type(elem) is list:
            sum_mas += recursive_sum(elem)
    return sum_mas 
'''
# 4
'''
def linear(nested_lists):
    res_mas = []
    for elem in nested_lists:
        if type(elem) is int:
            res_mas.append(elem)
        else:
            res_mas.extend(linear(elem))
    return res_mas
'''
# 5
'''
def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for elem in nested_dicts.values():
        if type(elem) is dict:
            value = get_value(elem, key)
            if value is not None:
                return value
'''
# 6
'''
def get_all_values(nested_dicts, key):
    res = set()
    if key in nested_dicts and type(key) is not dict:
        res = res | {nested_dicts[key]}
    
    for elem in nested_dicts.values():
        if type(elem) is dict:
            res = res | get_all_values(elem, key)

    return res

        



my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
'''
# 7 (моё решение)
'''
def dict_travel(nested_dicts):
    res = []
    def rec(nested_dict, way):
        for key, elem in nested_dict.items():
            if type(elem) is str or type(elem) is int:
                res.append( f"{way+key}: {elem}" )
            else:
                rec(elem, way+key+'.')

    rec(nested_dicts, '')
    print(*sorted(res), sep='\n')


print(dict_travel({'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}))
'''
# 7 (решение создателей)
'''
def dict_travel(nested_dicts, prefix=''):
    for key,value in sorted(nested_dicts.items()):
        way = f"{prefix}.{key}" if prefix else key
        if isinstance(value, (str, int)):
            print(f"{way}: {value}")
        else:
            dict_travel(value, way)



data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)
'''
# Модуль 9.1
# 4
'''
for i in range(ord('a'), ord('z')+1):
    print(chr(i))
'''
# 5
'''
def convert(number):
    return (str(bin(number)).replace('0b',''), str(oct(number)).replace('0o',''), str(hex(number)).replace('0x',''))

print(convert(-24))
'''
'''
def convert(n):
    return (f"{n:b}", f"{n:o}", f"{n:X}")
'''
# 7
'''
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

print(min(films, key=lambda x: sum(films[x].values())/2))
'''
# 8
'''
def non_negative_even(numbers):
    return all([i>=0 and i%2==0 for i in numbers])
'''
# 9
'''
def is_greater(lists, number):
    return any([sum(list)>number for list in lists])
'''
# 10
'''
def custom_isinstance(objects, typeinfo):
    return sum([1 if isinstance(object, typeinfo) else 0 for object in objects])
'''
# 11
'''
numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]

print(numbers.index(max(numbers)))
'''
# 12
'''
def my_pow(number):
    res = 0
    for i, num in enumerate(str(number), 1):
        res += int(num)**i
    return res
'''
# 13
'''
names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

for name, budget, profit in sorted(zip(names, budgets, box_offices)):
    print(f"{name}: {profit-budget}$")
'''
# 14
'''
def zip_longest(*args, fill=None):
    res = []
    for i in range(len(max(args, key=len))):
        row = list()
        for list_ in args:
            try:
                row.append(list_[i])
            except:
                row.append(fill)
        res.append(tuple(row))
    return res
'''
# 15
# моё решение
'''
list_sort = ['', '', '', '']

for elem in sorted(input()):
    if elem.islower():
        list_sort[0] += elem
    elif elem.isupper():
        list_sort[1] += elem
    elif elem.isdigit() and int(elem)%2==1:
        list_sort[2] += elem
    else:
        list_sort[3] += elem

print(''.join(list_sort))
'''
# понравилось чужое решение
'''
from string import ascii_lowercase, ascii_uppercase

key_sort = ascii_lowercase + ascii_uppercase + '13579' + '02468'
print(''.join(sorted(input(), key=key_sort.index)))
'''























































































































































































































































































































































































































































































































































































































































































































































































































