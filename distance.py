import itertools

cities = ['Чернівці', 'Хмельницький', "Кам'янець", 'Дунаївці', 'Вінниця']

distance_matrix = [
    [0, 110, 35, 85, 200],
    [110, 0, 100, 50, 120],
    [35, 100, 0, 45, 170],
    [85, 50, 45, 0, 130],
    [200, 120, 170, 130, 0]
]
def calculate_distance(path, matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += matrix[path[i]][path[i + 1]]
    distance += matrix[path[-1]][path[0]]
    return distance

min_distance = float('inf')
best_path = []

print("Всі маршрути")
for perm in itertools.permutations(range(len(cities))):
    dist = calculate_distance(perm, distance_matrix)
    city_path = [cities[i] for i in perm]
    print(f"Маршрут: {' - '.join(city_path)} - {cities[perm[0]]} = відстань: {dist}")

    if dist < min_distance:
        min_distance = dist
        best_path = perm

best_city_path = [cities[i] for i in best_path]
print("\nНайкращий маршрут:")
print(f"{' - '.join(best_city_path)} - {best_city_path[0]} = відстань: {min_distance} км")
