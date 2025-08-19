# "Поколение Python": курс для профессионалов

# конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект конспект

# ------------------ Модуль datetime ------------------
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
# Модуль calendar
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
'''
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
'''
# 19
'''
from datetime import timedelta, date

d,m,y = map(int, input().split('.'))
Date = date(y,m,d)
for i in range(2,12):
    print(Date.strftime('%d.%m.%Y'))
    Date += timedelta(days=i)
'''
# 20
'''
from datetime import datetime

mas = [datetime.strptime(x, '%d.%m.%Y') for x in input().split()]
res = [abs(mas[i] - mas[i+1]).days for i in range(len(mas)-1)]
    
print(res)

'''
# 21
'''
from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    dates  = [datetime.strptime(x, '%d.%m.%Y') for x in dates]
    start, end = min(dates), max(dates)
    days = (end-start).days
    return [(start+timedelta(days=i)).strftime('%d.%m.%Y') for i in range(days+1)]







dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))
'''
# 22
'''
from datetime import datetime, timedelta

start, end = input(), input()
start, end = datetime.strptime(start,'%H:%M'), datetime.strptime(end,'%H:%M')
for i in range((end-start+timedelta(minutes=10)).seconds//60//55):
    if end >= start + timedelta(minutes=45):
        end_moment = start + timedelta(minutes=45)
        print(f"{start.strftime('%H:%M')} - {end_moment.strftime('%H:%M')}")
        start = end_moment + timedelta(minutes=10)
'''
# Модуль 3.5
# 1
'''
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
'''
# 2
'''
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
'''
# 3
'''
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
'''
# 4
'''
from datetime import datetime, timedelta


start, end = datetime.strptime(input(),'%d.%m.%Y'), datetime.strptime(input(),'%d.%m.%Y')
while (start.month + start.day) % 2 == 0 :
    start += timedelta(days=1)

while start <= end:
    if start.weekday() != 0 and start.weekday() != 3:
        print(start.strftime('%d.%m.%Y'))
    start += timedelta(days=3)
'''
# 5
'''
#мой метод, почему-то светится ошибка, но делает всё норм
from datetime import datetime, timedelta

employee_mas = [input().split() for _ in range(int(input()))]    # считываем сотрудников в строки

for i in range(len(employee_mas)):
    employee_mas[i][2] = datetime.strptime(employee_mas[i][2], '%d.%m.%Y')   # переписываем дату из строки в datetime

employee_mas_max = list(filter( lambda x: x[2] == min( employee_mas, key=lambda x: x[2])[2], employee_mas ))  # ищем самого взрослого сотрудника/сотрудников

print([f"{datetime.strftime(employee_mas_max[0][2],'%d.%m.%Y')} {employee_mas_max[0][0]} {employee_mas_max[0][1]}", f"{datetime.strftime(employee_mas_max[0][2],'%d.%m.%Y')} {len(employee_mas_max)}"][len(employee_mas_max)!=1])
'''
'''
#списал понравившееся решение
from datetime import datetime

d = {}
for _ in range(int(input())):
    name, Date = input().rsplit(maxsplit=1)
    d.setdefault(datetime.strptime(Date, '%d.%m.%Y'), []).append(name)
print( min(d).strftime('%d.%m.%Y'), [''.join(d[min(d)]) , len(d[min(d)]) ][ len(d[min(d)]) > 1 ] )
'''
# 6 
'''
from datetime import datetime

employee_dict = {}

for _ in range(int(input())):
    name, Date = input().rsplit(maxsplit=1)
    employee_dict.setdefault(Date, []).append(name)

res = sorted([datetime.strptime(k,'%d.%m.%Y') for k,v in employee_dict.items() if len(v) == len(employee_dict[max(employee_dict, key=lambda x: len(employee_dict[x]))])])

[print(x.strftime('%d.%m.%Y')) for x in res]
'''
# 7
'''
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
'''
# 8
'''
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
'''    
'''
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
'''
# Модуль 3.7
# 13
'''
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
'''
# 14
'''
import calendar
from datetime import date

year = int(input())
for month in range(1,12+1):
    for day in range(15,21+1):
        if date(year,month,day).weekday() == 3:
            print(date(year,month,day).strftime('%d.%m.%Y'))
            break
'''
# Модуль 4.1
# 10
'''
import sys

for line in sys.stdin:
    sys.stdout.write(line.rstrip()[::-1])
    print()
'''
# 11
'''
import sys
from datetime import date

dates = []
for Date in sys.stdin:
    y,m,d = map(int, Date.strip().split('-'))
    dates.append(date(y,m,d))
sys.stdout.write(str((max(dates)-min(dates)).days))
'''
# 12
'''
import sys

k, last_step = 0, 0
for i in sys.stdin:
    k+=1
    last_step = int(i.strip())

if last_step % 2 == 0:
    sys.stdout.write(['Анри','Дима'][k%2==0])
elif last_step % 2 != 0:
    sys.stdout.write(['Анри','Дима'][k%2!=0])
'''
# 13
'''
import sys

students_height = [int(x) for x in sys.stdin]
if len(students_height) == 0:
    sys.stdout.write('нет учеников')
else:
    sys.stdout.write(f"Рост самого низкого ученика: {min(students_height)}\n")
    sys.stdout.write(f"Рост самого высокого ученика: {max(students_height)}\n")
    sys.stdout.write(f"Средний рост: {sum(students_height)/len(students_height)}")
'''
# 14
'''
import sys

sys.stdout.write(str(sum([1 for s in sys.stdin if s.strip()[0]=='#'])))
'''
# 15
'''
import sys 

for line in sys.stdin:
    if len( line.strip() ) == 0 or line.strip()[0] != '#':
        sys.stdout.write(line)
'''
# 16 
'''
import sys

res = []
condition = ''
for line in sys.stdin:
    if '/' in line:
        res.append(line.strip().split(' / '))
    else:
        condition = line.strip()

[sys.stdout.write(elem[0] + '\n') for elem in sorted(list(filter(lambda x: x[1]==condition, res)), key=lambda x: (x[2],x[0]))]
'''
# 17
'''
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
'''
# 18
'''
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
'''
# Модуль 




















































































































































































































































































































































































































































































































































































































