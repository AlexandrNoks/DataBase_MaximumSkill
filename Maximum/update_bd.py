import pandas as pd
from data import data

i = 1
while i < 2:
    name_pupils = str(input("Enter name: "))
    age_pupils = int(input("Enter age: "))
    phone_pupils = int(input("Enter phone: "))
    data_piples = [name_pupils,age_pupils,phone_pupils]
    i += 1
    data_piples.insert(0,len(data) + 2)
    data.append(data_piples)
    keys = ["id",'Name', 'Age','Phone']
    younger_group = [dict(zip(keys,data[i])) for i in range(len(data)) if data[i][2] <= 8]
    middle_group = [dict(zip(keys,data[i])) for i in range(len(data)) if data[i][2] > 8 and data[i][2] <= 16]
    senior_group = [dict(zip(keys,data[i])) for i in range(len(data)) if data[i][2] > 16]
    table_younger = pd.DataFrame(younger_group,columns=['Name', 'Age','Phone'])
    table_middle = pd.DataFrame(middle_group,columns=['Name', 'Age','Phone'])
    table_senior = pd.DataFrame(senior_group,columns=['Name', 'Age','Phone'])
    if age_pupils <= 8:
        print(table_younger.to_string())
    elif age_pupils > 8 and age_pupils <= 16:
        print(table_middle.to_string())
    else:
        print(table_senior.to_string())
# print(len(younger_group))
# print(len(middle_group))
# print(len(senior_group))
