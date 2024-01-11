import importlib

def fetch_a_sorter(property_name):
    try:
        sort_module = importlib.import_module(f"src.sort_by_{property_name}")
        return getattr(sort_module, "sort_by_criteria")
    except ImportError:
        print(f"No sorting module found for: {property_name}")
        return None
    except AttributeError:
        print(f"Module 'src.sort_by_{property_name}' does not have 'sort_by_criteria'")
        return None
