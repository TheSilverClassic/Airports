from src.fetch_sorter import fetch_a_sorter
from src.airport_input import airports_list

def main():
    print("Select the sorting criteria:")
    print("0: No sorting")
    print("1: IATA code")
    print("2: Name")
    print("3: City")
    print("4: State")
    print("5: Delay")
    print("6: Temperature")
    print("7: City and Name")
    print("Enter any other key to quit.")
    choice = input("Enter your choice: ")

    criteria_map = {
        "0": None,
        "1": "iata",
        "2": "name",
        "3": "city",
        "4": "state",
        "5": "delay",
        "6": "temperature",
        "7": "city_name"
    }

    sorter = fetch_a_sorter(criteria_map.get(choice))

    sorted_airports = sorter(airports_list) if sorter else airports_list

    display_airports(sorted_airports)

def display_airports(airports):
    print("\nSorted Airports:")
    for airport in airports:
        name_upper = airport.name.upper()
        print(f"{name_upper} ({airport.iata}) - {airport.city}, {airport.state}, Temp: {airport.temperature}, Delay: {'Yes' if airport.delay else 'No'}")

if __name__ == '__main__':
    main()
