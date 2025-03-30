import json
import math
from pathlib import Path

# Создание графа
filename = Path("algorithms", "dijkstra.json")
with open(file=filename) as my_json:
    graph = json.load(my_json)

# Создание множества уже проверенных узлов
processed = set()


# Создние хэш-таблицы для стоимостей
# (рассматриваем относительно старта)
infinity = math.inf
costs = {}
costs["a"] = 2
costs["b"] = 5
costs["fin"] = infinity
costs["c"] = infinity
costs["d"] = infinity

# Создание хэш-таблицы для родителей
# (рассматриваем относительно старта)
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None


# Найти кратчайший узел
def find_lowest_node(costs: dict):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_node(costs)

while node:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    print(node)
    node = find_lowest_node(costs)

print(costs["fin"])
print(parents)
