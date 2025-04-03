# Штаты, которые нужно покрыть связью
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Станции, которые покрывают определенные штаты
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Для хранения итогового набора станций
final_stations = set()

# Станция с самым большим числом штатов
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # & - это пересечение множеств
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    states_needed -= states_covered

print(final_stations)
