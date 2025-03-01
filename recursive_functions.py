## Функция, которая берет факториал от числа ##
def fact(x):
    if x == 1:
        return 1
    else:
        print(x)
        return (x * fact(x-1))
    
print(fact(5))

## Функция, которая находит сумму массива ##
def sum(my_list):
    if my_list == []:
        return 0
    return my_list[0] + sum(my_list[1:])

# list[start:stop:step] - вот так работает срез