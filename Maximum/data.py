import pandas as pd

data = [
    [1,"Корсан Лиза",7,"+7 922 874 873"],
    [2,"Корнилов Андрей",4,"+7 922 874 873"],
    [3,"Полушин Миша",12,"+7 922 874 873"],
    [4,"Карпов Дима",11,"+7 922 874 873"],
    [5,"Чирков Тихон",6,"+7 922 874 873"],
    [6,"Виценко Оля",6,"+7 922 874 873"],
    [8,"Минеева Настя",11,"+7 922 874 873"],
    [9,"Унинбаева Азалия",12,"+7 922 874 873"],
    [10,"Пархомцев Даниил",16,"+7 922 874 873"],
    [11,"Тюрина Анастасия",25,"+7 922 874 873"],
    [12,"Власенко Валерия",42,"+7 922 874 873"],
    [13,"Макаров Юра",30,"+7 922 874 873"],
    [14,"Семаева София",6,"+7 922 874 873"],
    [15,"Минзафарова Оксана",40,"+7 922 874 873"],
    [16,"Суслова Лиза",6,"+7 922 874 873"],
    [17,"Суслова Настя",6,"+7 922 874 873"],
    [18,"Хисангулова Елена",33,"+7 922 874 873"],
    [19,"Хисангулова Ирада",7,"+7 922 874 873"],
    [20,"Черкова Василиса",8,"+7 922 874 873"]
]
table_data = pd.DataFrame(data,columns=["id",'Name', 'Age','Phone'])
