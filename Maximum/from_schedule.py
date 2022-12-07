import pandas as pd
import calendar
# 21:00,16:50,12:40,19:20,14:20


# Рассписания
# Составления рассписания через ввод: день недели и время (колличества уроков зависит от введенного колличества времени)
week_day = list(calendar.day_abbr)[:5]
def gen_lessons():
    times = str(input(f"Select the lesson from the list (max 8).Please enter values without spaces,separated by commas: "))
    time_lesson = ['11:00','11:50','12:40','13:30','14:20','15:10','16:00','16:50','17:40','18:30','19:20','20:10','21:00']
    list_times = times.split(",")
    for i in list_times:
        if i in time_lesson:
            yield i
        else:
            pass

def func_err():
    try:
        gen_lessons()
    except ValueError:
        print("Please check enter the value")
    except TypeError:
        print("Please check enter the value")
    except NameError:
        print("Please check enter the value")


i = 1
my_list = []
while i <= 5:
    num_week_day = input("Enter number week day from 1 to 5: ")
    if num_week_day == "stop":
        break
    elif num_week_day.isdigit() is False:
        continue
    elif int(num_week_day) > 5:
        print("The maximum count working days 5")
        continue

    n = list(gen_lessons())
    if len(n) > 8:
        print("The maximum of count of lesson 8 in day")
        continue
    else:
        try:
            num_week_day = int(num_week_day)
        except int(num_week_day) == 0 or int(num_week_day) > 5:
            print("Please enter number week day from 1 to 5")
            continue
        except ValueError:
            func_err()
            continue
        my_list.append(n)
    i += 1
    if i > 6:
        break

dict_result = dict(zip(week_day,my_list))
free_time = [elem for elem in dict_result.values()]
# Составления рассписания на неделю
# time_lesson = ['11:00','11:50','12:40','13:30','14:20','15:10','16:00','16:50','17:40','18:30','19:20','20:10','21:00']
# res_list = ['11:00','11:50','12:40','13:30','14:20','15:10','16:00','16:50','17:40','18:30','19:20','20:10','21:00']
# дни недели сокращенно

# print(week_day)
# Рассписание свободных часов
dict_schedule = {}

# Функция генератор для составления единого списка свободных и занятых часов на каждый день в течении недели.
time_lesson_every = ['11:00','11:50','12:40','13:30','14:20','15:10','16:00','16:50','17:40','18:30','19:20','20:10','21:00']
def gen_time_lesson(week_day,time_lesson):
    free = "free"
    busy = "busy"
    res_dict = {}
    for values in week_day:
        res_dict[values] = time_lesson

    for i in range(len(week_day)):
        for elem in res_dict[week_day[i]]:
            if elem in free_time[i]:
                elem = elem.replace(elem,free)
            else:
                elem = elem.replace(elem,busy)
            yield elem
result = list(gen_time_lesson(week_day,time_lesson_every))
# print(len(result))
# count_lesson_in_day = int(input("Please enter count lesson: "))

# Функция генератор составления рассписания на равное колличество уроков в день вывод свободно/занято
# разбить список values_free_busy на несколько списков в зависимости от колличества уроков в день (n)
# def gen_schedule_lesson(result,n):
#     for i in range(0,len(result),n):
#         yield result[i:i + n]
#

schedule = dict(zip(week_day,result))
# print(schedule)
# Таблица pandas равномерного распределения часов
table_pd = pd.DataFrame(schedule,columns=week_day)
table_pd.insert(0,'time',time_lesson_every, True)
table_pd.assign(profit='Free',include='all')
print(table_pd)