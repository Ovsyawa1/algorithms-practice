'''
    Импортирую библиотеки datetime и json
'''
import datetime
import json

# Число элементов в json
n = 5

# Формат представления времени в json
TIME_FORMAT = "%H:%M:%S"

# Длина шага
STEP_M = 0.65

# Хранение
storage_data = {}

# Массивы времени и шагов
time_list = []
steps_list = []


def check_correct_data(data: dict):
    if not data:
        return False
    elif not all(x in data.keys() for x in ["time", "steps"]):
        return False
    elif any(x == '' for x in data.values()):
        return False
    return True


# Проверка корректности времени
def check_correct_time(time: str, time_list: list):
    try:
        time_format = datetime.datetime.strptime(time, TIME_FORMAT)
    except ValueError:
        print("Пришли некорректные значения")
        return False
    try:
        if time_format < time_list[-1]:
            return False
    except IndexError:
        return True
    return True


# Суммарный подсчет шагов
def get_step_day(steps: list):
    steps_sum = 0
    for element in steps:
        steps_sum += element
    return steps_sum


# Подсчет пройденной дистанции
def get_distance(steps_sum):
    return steps_sum * STEP_M


with open('data.json', encoding='utf-8') as my_json:
    all_data = json.load(my_json)

for i in range(n):
    data_package = f"data_package_{i+1}"
    if (
        check_correct_data(all_data[data_package]) and
        check_correct_time(
            time=all_data[data_package]["time"],
            time_list=time_list
        )
    ):
        time_format = datetime.datetime.strptime(
            all_data[data_package]["time"], TIME_FORMAT
        )
        time_list.append(time_format)
        steps_list.append(all_data[data_package]["steps"])
        current_dict = {data_package: all_data[data_package]}
        storage_data.update(current_dict)
steps_sum = get_step_day(steps_list)
distance = get_distance(steps_sum)


print(time_list)
print(steps_list)
print(storage_data)
