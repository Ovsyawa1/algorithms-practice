N = input("Длина массива: ")
my_list = [int(element) for element in input("Элементы массива: ").split()]
x = int(input("Загадать число: "))

def solution(x: int, some_list: list):
    k = 0
    for i in some_list:
        if i == x:
            k += 1
            
    return k

print(solution(x, my_list))