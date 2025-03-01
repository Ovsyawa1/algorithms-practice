
## Сортировка выбором ##
def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr: list):
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest_index = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest_index))
    return new_arr

my_arr = [1, 8, -10, 26, 15, 100, -1000, 90, 66, 125]

sorted_arr = selection_sort(my_arr)

print(sorted_arr)

## Алгоритм быстрой сортировки
def quick_sort(my_array: list):
    if len(my_array) < 2:
        return my_array
    else:
        pivot = my_array[0]
        less = [i for i in my_array[1:] if i <= pivot]
        greater = [i for i in my_array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 7, 24, 89, 32, 7]))
