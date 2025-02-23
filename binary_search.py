import random


def binary_search(arr: list, item): # объявление функции
    low = 0
    high = len(arr)
    
    while low <= high:
        mid = (high + low) // 2 # центр промежутка от low до high
        guess = arr[mid] # предполагаемое число
        if guess < item: # предполагаемое число меньше -> берем больше ->
            low = mid + 1 # -> смещаем нижнюю границу
        elif guess > item: # предполагаемое число больше -> берем меньше ->
            high = mid - 1 # -> смещаем верхнюю границу
        else:
            return mid  
    return None

# объявление переменных #

my_arr = [] # объявление массива
n = 10 # длина массива
req_numb = 10 # нужное для поиска число
  
for _ in range(n): # создание массива из n символов рандомными int'ами
    my_arr.append(random.randint(1, 100))

my_arr.sort() # отсортировать массив

print(my_arr)
print(binary_search(my_arr, req_numb))
