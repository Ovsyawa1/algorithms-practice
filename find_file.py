from os import listdir
from os.path import isfile, join
from collections import deque

## Применение поиска в ширину при помощи очереди (FIFO - первый вошел, первым вышел) ##

def printnames(start_dir):
    # Инициализация переменных #
    search_queue = deque() # создание очереди 
    search_queue.append(start_dir) # добавление первого элемента в очередь
    
    # Начало логики #
    while search_queue: # пока существует очередь
        dir = search_queue.popleft() # достань элемент с индексом 0
        for file in sorted(listdir(dir)): #
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)
  
## Применение поиска в глубину при помощи рекурсии, которая создает стэк вызовов (LIFO - последним пришел, первым вышел) ## 
                
def printnames_v2(current_dir):
    for file in sorted(listdir(current_dir)):
        fullpath = join(current_dir, file)
        if isfile(fullpath):
            print(file)
        else:
            printnames_v2(fullpath)
                