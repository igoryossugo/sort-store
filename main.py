import math
from collections import defaultdict


customer_location = [20, 32]
stores = [[40, 88], [18, 56], [99, 2]]
plan = None


def sort_stores(customer_location, stores, plan=None):
    stores_by_distance = defaultdict(list)
    for store in stores:
        distance = get_distance(
            store=store,
            customer_location=customer_location
        )
        stores_by_distance[distance].append(store)

    sorted_distances = sorted(stores_by_distance.keys())
    sorted_stores = []
    for distance in sorted_distances:
        sorted_stores += stores_by_distance[distance]

    return sorted_stores


def get_distance(store, customer_location):
    x_a, y_a = store[0], store[1]
    x_b, y_b = customer_location[0], customer_location[1]
    distance_x = (x_b - x_a) * (x_b - x_a)
    distance_y = (y_b - y_a) * (y_b - y_a)
    return math.sqrt(distance_x + distance_y)


sorted_stores = sort_stores(
    customer_location=customer_location,
    stores=stores,
    plan=plan
)
print(sorted_stores)
