from src.airport import Airport
from dataclasses import replace

def process_airports(airports, sort_by_criteria=lambda airports: airports):
    return sort_by_criteria([convert_name_case(airport) for airport in airports])

def convert_name_case(airport):
    return replace(airport, name=airport.name.upper())
