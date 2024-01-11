def sort_by_criteria(airports):
    return sorted(airports, key=lambda airport: (airport.city, airport.name))
