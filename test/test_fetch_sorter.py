import unittest
from src.airport import Airport
from src.fetch_sorter import fetch_a_sorter
from src.sort_by_iata import sort_by_criteria as sort_by_iata
from src.sort_by_name import sort_by_criteria as sort_by_name
from src.sort_by_city import sort_by_criteria as sort_by_city
from src.sort_by_state import sort_by_criteria as sort_by_state
from src.sort_by_delay import sort_by_criteria as sort_by_delay
from src.sort_by_city_name import sort_by_criteria as sort_by_city_name
from src.sort_by_temperature import sort_by_criteria as sort_by_temperature

class TestSorterFetch(unittest.TestCase):
    def test_fetch_sorter_import_error(self):
        self.assertIsNone(fetch_a_sorter("non_existent"))

    def test_fetch_sorter_attribute_error(self):
        self.assertIsNone(fetch_a_sorter("incomplete"))

    def test_fetch_iata_sorter(self):
        self.assertEqual(fetch_a_sorter("iata"), sort_by_iata)

    def test_fetch_name_sorter(self):
        self.assertEqual(fetch_a_sorter("name"), sort_by_name)

    def test_fetch_city_sorter(self):
        self.assertEqual(fetch_a_sorter("city"), sort_by_city)

    def test_fetch_state_sorter(self):
        self.assertEqual(fetch_a_sorter("state"), sort_by_state)

    def test_fetch_temperature_sorter(self):
        self.assertEqual(fetch_a_sorter("temperature"), sort_by_temperature)

    def test_fetch_delay_sorter(self):
        self.assertEqual(fetch_a_sorter("delay"), sort_by_delay)

    def test_fetch_city_name_sorter(self):
        self.assertEqual(fetch_a_sorter("city_name"), sort_by_city_name)

    def setUp(self):
        self.iad = Airport("IAD", "Dulles Intl", "Washington", "DC", 71, True)
        self.ord = Airport("ORD", "O'Hare International", "Chicago", "IL", 62, True)
        self.mdw = Airport("MDW", "Midway International", "Chicago", "IL", 60, False)

    def test_fetch_iata_sorter_and_sort(self):
        iata_sorter = fetch_a_sorter("iata")
        sorted_airports = iata_sorter([self.mdw, self.ord, self.iad])
        self.assertEqual(sorted_airports, [self.iad, self.mdw, self.ord])

    def test_fetch_name_sorter_and_sort(self):
        name_sorter = fetch_a_sorter("name")
        sorted_airports = name_sorter([self.mdw, self.ord, self.iad])
        self.assertEqual(sorted_airports, [self.iad, self.mdw, self.ord])

    def test_fetch_city_sorter_and_sort(self):
        city_sorter = fetch_a_sorter("city")
        sorted_airports = city_sorter([self.iad, self.ord, self.mdw])
        self.assertEqual(sorted_airports, [self.ord, self.mdw, self.iad])

    def test_fetch_state_sorter_and_sort(self):
        state_sorter = fetch_a_sorter("state")
        sorted_airports = state_sorter([self.mdw, self.ord, self.iad])
        self.assertEqual(sorted_airports, [self.iad, self.mdw, self.ord])

    def test_fetch_temperature_sorter_and_sort(self):
        temperature_sorter = fetch_a_sorter("temperature")
        sorted_airports = temperature_sorter([self.mdw, self.ord, self.iad])
        self.assertEqual(sorted_airports, [self.mdw, self.ord, self.iad])

    def test_fetch_delay_sorter_and_sort(self):
        delay_sorter = fetch_a_sorter("delay")
        sorted_airports = delay_sorter([self.iad, self.ord, self.mdw])
        self.assertEqual(sorted_airports, [self.iad, self.ord, self.mdw])

    def test_fetch_city_name_sorter_and_sort(self):
        city_name_sorter = fetch_a_sorter("city_name")
        sorted_airports = city_name_sorter([self.iad, self.ord, self.mdw])
        self.assertEqual(sorted_airports, [self.mdw, self.ord, self.iad])
