import pandas as pd
from datetime import datetime
import calendar

# Создания таблицы с данными об учениках
data = [
    [1,"Корсан Лиза",7,"+7 922 874 873"],
    [2,"Корнилов Андрей",4,"+7 922 874 873"],
    [3,"Полушин Миша",12,"+7 922 874 873"],
    [4,"Карпов Дима",11,"+7 922 874 873"],
    [5,"Чирков Тихон",6,"+7 922 874 873"],
    [6,"Виценко Оля",6,"+7 922 874 873"],
    [7,"Минеева Настя",11,"+7 922 874 873"],
    [8,"Унинбаева Азалия",12,"+7 922 874 873"],
    [9,"Пархомцев Даниил",16,"+7 922 874 873"],
    [10,"Тюрина Анастасия",25,"+7 922 874 873"],
    [11,"Власенко Валерия",42,"+7 922 874 873"],
    [12,"Макаров Юра",30,"+7 922 874 873"],
    [13,"Семаева София",6,"+7 922 874 873"],
    [14,"Минзафарова Оксана",40,"+7 922 874 873"],
    [15,"Суслова Лиза",6,"+7 922 874 873"],
    [16,"Суслова Настя",6,"+7 922 874 873"],
    [17,"Хисангулова Елена",33,"+7 922 874 873"],
    [18,"Хисангулова Ирада",7,"+7 922 874 873"],
    [19,"Черкова Василиса",8,"+7 922 874 873"]
]
data_table = pd.DataFrame(data,columns=["id",'Name', 'Age','Phone'])

# Создания таблиц данных учеников с разделением их на группы
# data_table["visits"] = None
# print(data_table.to_string(index=False))
name_data = data_table["Name"].index.tolist()
# print(name_data)
younger = []
dict_table = {}
data_age = data_table[data_table["Age"] <= 8]
data_name = data_age["Name"]
hour_time = list(range(14,22))
hours = [f"{hour}:50" for hour in hour_time]
# print(len(hours))
titles = list(calendar.day_abbr)[:-2]
names = list(map(lambda x: "".join(x[1:2]),data))

# Создание таблицы посещения занятий
titles.insert(0,"time")
for i in titles:
    dict_table["time"] = hours
    names = list(map(lambda x: "".join(x[1:2]),data))
    if i == "Mon":
        dict_table["Mon"] = list(names[4:9])
    elif i == "Tue":
        dict_table["Tue"] = list(names[9:15])
    elif i == "Wed":
        dict_table["Wed"] = list(names[3:7])
    elif i == "Thu":
        dict_table["Thu"] = list(names[2:5])
    elif i == "Fri":
        dict_table["Fri"] = list(names[1:3])
# print(dict_table)
for elem in dict_table:
    if len(dict_table[elem]) < 8:
        x = 8 - len(dict_table[elem])
        y = ["free"] * x
        dict_table[elem] = dict_table[elem] + y
    else:
        pass
    # print(elem,":",dict_table[elem])
# print(titles)


# print(titles)
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
timetable = pd.DataFrame(dict_table,columns=titles)
print(timetable.to_string())

