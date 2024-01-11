import unittest
from src.airport import Airport
from src.airports_info_processor import process_airports
from src.sort_by_iata import sort_by_criteria as sort_by_iata
from src.sort_by_name import sort_by_criteria as sort_by_name
from src.sort_by_city import sort_by_criteria as sort_by_city
from src.sort_by_state import sort_by_criteria as sort_by_state
from src.sort_by_delay import sort_by_criteria as sort_by_delay
from src.sort_by_city_name import sort_by_criteria as sort_by_city_name
from src.sort_by_temperature import sort_by_criteria as sort_by_temperature

class AirportInfoProcessTests(unittest.TestCase):

    def setUp(self):
        self.iad = Airport("IAD", "Dulles Intl", "Washington", "DC", 71, True)
        self.ord = Airport("ORD", "O'Hare International", "Chicago", "IL", 62, True)
        self.mdw = Airport("MDW", "Midway International", "Chicago", "IL", 60, False)
        
        self.expected_iad = Airport("IAD", "DULLES INTL", "Washington", "DC", 71, True)
        self.expected_ord = Airport("ORD", "O'HARE INTERNATIONAL", "Chicago", "IL", 62, True)
        self.expected_mdw = Airport("MDW", "MIDWAY INTERNATIONAL", "Chicago", "IL", 60, False)

    def test_canary(self):
        self.assertTrue(True)

    def test_empty_list(self):
        airports = []

        result = process_airports(airports)

        self.assertEqual(airports, result)

    def test_one_airport(self):
        result = process_airports([self.iad])

        self.assertEqual([self.expected_iad], result)

    def test_two_airport(self):
        result = process_airports([self.iad, self.ord])

        self.assertEqual([self.expected_iad, self.expected_ord], result)

    def test_three_airport(self):
        result = process_airports([self.iad, self.ord, self.mdw])

        self.assertEqual([self.expected_iad, self.expected_ord, self.expected_mdw], result)

    def test_sort_two_airports_by_iata_code(self):
        result = process_airports([self.ord, self.iad], sort_by_criteria=sort_by_iata)

        self.assertEqual([self.expected_iad, self.expected_ord], result)

    def test_sort_two_airports_by_name(self):
        result = process_airports([self.ord, self.iad], sort_by_criteria=sort_by_name)

        self.assertEqual([self.expected_iad, self.expected_ord], result)

    def test_sort_two_airports_by_city(self):
        result = process_airports([self.ord, self.iad], sort_by_criteria=sort_by_city)

        self.assertEqual([self.expected_ord, self.expected_iad], result)

    def test_sort_two_airports_by_state(self):
        result = process_airports([self.ord, self.iad], sort_by_criteria=sort_by_state)

        self.assertEqual([self.expected_iad, self.expected_ord], result)

    def test_sort_three_airports_by_delay(self):
        airports = [self.iad, self.ord, self.mdw]
        expected_order = [self.expected_iad, self.expected_ord, self.expected_mdw]

        result = process_airports(airports, sort_by_criteria=sort_by_delay)

        self.assertEqual(expected_order, result)

    def test_sort_three_airports_by_temperature(self):
        airports = [self.ord, self.iad, self.mdw]
        expected_order = [self.expected_mdw, self.expected_ord, self.expected_iad]

        result = process_airports(airports, sort_by_criteria=sort_by_temperature)

        self.assertEqual(expected_order, result)

    def test_sort_three_airports_by_city_and_name(self):
        airports = [self.mdw, self.ord, self.iad]
        expected_order = [self.expected_mdw, self.expected_ord, self.expected_iad]

        result = process_airports(airports, sort_by_criteria=sort_by_city_name)

        self.assertEqual(expected_order, result)
