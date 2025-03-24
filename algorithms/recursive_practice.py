my_arr = [1, 3, 9, 10, 20]
max_element = my_arr[0]
high_edge = len(my_arr) - 1

## Нахождение суммы ##
def arr_sum(arr, i=0, result=0):
    if i < len(arr):
        result += arr[i]
        i += 1
        return arr_sum(arr, i, result)
    
    return result

print(f"Сумма элементов массива равна: {arr_sum(my_arr)}")

## Нахождение числа элементов в массиве ##
def arr_numb(arr, i=0):
    i += 1
    if i < len(arr):
        return arr_numb(my_arr, i)
    
    return i

print(f"Число элементов в массиве равно: {arr_numb(my_arr)}")

## Нахождение наибольшего элемента в массиве ##
def arr_max(arr, max, i=1):
    if i < len(arr):
        if arr[i] > max:
            max = arr[i]
        i += 1
        return arr_max(arr, max, i)
    
    return max

print(f"Максимальный элемент в списке: {arr_max(my_arr, max_element)}")

## Бинарный поиск, но как рекурсия ##
def binary_search(sorted_arr, expected_number, low=0, high=high_edge):
    if low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] > expected_number:
            high = mid - 1
            return binary_search(sorted_arr, expected_number, low, high)
        
        elif sorted_arr[mid] < expected_number:
            low = mid + 1
            return binary_search(sorted_arr, expected_number, low, high)
        
        return True
    
    return False

expected_number = 100
print(f"Бинарный поиск числа {expected_number} дал результат: {binary_search(my_arr, expected_number)}")