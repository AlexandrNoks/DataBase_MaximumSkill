week_day = "Mon   Tue   Wed   Thu   Fri".split("   ")
print(week_day)
# 21:00,16:50,12:40,19:20,14:20
# str max 47 symbol
dict_schedule = {}


def gen_func():
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
        gen_func()
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

    n = list(gen_func())
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





