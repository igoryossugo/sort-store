from main import get_distance, sort_stores


class TestSortStore:

    def test_should_return_sorted_store_list(self):
        customer_location = [20, 32]
        stores = [[40, 88], [18, 56], [99, 2], [99, 2], [72, 1]]
        expected_sorted_stores = [
            [18, 56],
            [40, 88],
            [72, 1],
            [99, 2],
            [99, 2],
        ]
        sorted_stores = sort_stores(
            customer_location=customer_location,
            stores=stores
        )
        assert sorted_stores == expected_sorted_stores


class TestGetDistance:

    def test_should_return_distance_of_store_and_location(self):
        shortest_distance = get_distance(
            store=[30, 23],
            customer_location=[41, 32]
        )
        median_distance = get_distance(
            store=[15, 11],
            customer_location=[41, 32]
        )
        greater_distance = get_distance(
            store=[98, 10],
            customer_location=[41, 32]
        )
        assert shortest_distance < median_distance < greater_distance
