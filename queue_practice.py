from collections import deque
import json
    
def person_is_seller(name):
    return name[-1] == 'm'

def find_mango_trader(search_queue: deque, json_name: "str" = "sample.json"):
    with open(json_name, "r") as my_json:
        json_file = json.load(my_json) # открыть созданный json
        
    search_queue += json_file["You"] # добавить первый элемент в очередь 
    searched = set() # создание множества для уже проверенных продавцов
        
    while search_queue: # пока существует очередь
        person = search_queue.popleft() # вытащить элемент с индексом 0
            
        if not (person in searched): # проверка, что пользователь ещё не был проверен
            searched.add(person)
            print(person)
                            
            if person_is_seller(person): # проверка на продовца манго
                print(person + " - это продавец манго!!!")
                return True
            
            else: 
                if person in json_file: # поиск человека по ключу в json
                    search_queue += json_file[person] # добавить в очередь всех связанных с этим человеком
        
    return False # если ничего не было найдено, то вернуть False
    
search_queue = deque()

find_mango_trader(
    search_queue=search_queue,
    json_name="queue.json",
)