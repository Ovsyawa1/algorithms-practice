import random


def binary_search(arr: list, item): # объявление функции
    low = 0
    high = len(arr)
    
    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
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
