from datetime import datetime
import calendar

# Рассписание занятий
time_lesson = ['11:00','11:50','12:40','13:30','14:20','15:10','16:00','16:50','17:40','18:30','19:20','20:10','21:00']
week_day_abbr = list(calendar.day_abbr) # дни недели сокращенно
num_week_day = datetime.today().isoweekday()
time_busy = (time_lesson[2:7],time_lesson[6:],time_lesson[6:10],time_lesson[11:],time_lesson[5:12])
free_time = (time_lesson[:3]+time_lesson[7:],time_lesson[:6],time_lesson[:6]+time_lesson[10:],time_lesson[:11],time_lesson[:5]+time_lesson[12:])
# Рассписание свободных часов
dict_free_time = dict(zip(week_day_abbr,free_time))
# Рассписание занятые часы
dict_time_busy = dict(zip(week_day_abbr,time_busy))

# Узнать свободные часы занятий
# for i in range(1,len(week_day_abbr)):
#     int_num_week_day = input("Enter week day: ")
#     if int_num_week_day == '' or int_num_week_day == 'stop':
#         break
#     try:
#         int_num_week_day = int(int_num_week_day)
#         i = int_num_week_day
#         print("\n".join(free_time[i]))
#     except ValueError:
#         print('Please, enter for number 1 to 5')
#         continue
#     except TypeError:
#         print('Sorry, school in now day do not work.')
#         continue
#     except IndexError:
#         print('Sorry, school in now day do not work.Try it again.')
#         continue


# print(num_week_day)
# Функция генератор указываем время в часах с которого выводится
inp_hours = str(input("Enter time: ")) + ':00'
def generator_schedule(inp_hours,time_lesson):
    res = datetime.strptime(inp_hours,'%H:%M')
    for n in time_lesson:
        date_time_obj = datetime.strptime(n, '%H:%M')
        if date_time_obj > res:
            yield date_time_obj.time().strftime('%H:%M')
        else:
            pass
schedule = list(generator_schedule(inp_hours,time_lesson))
print(schedule)







