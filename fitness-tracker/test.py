import datetime

my_time = "12:43:1111"

try:
    time_fromat = datetime.datetime.strptime(my_time, '%H:%M:%S')
    print(time_fromat.time())
except ValueError:
    print("Govnj")
my_list = []

print(my_list[-1])
