def analyze_list(items: list) -> dict:
    total = len(items)
    unique_items = set(items)
    unique_count = len(unique_items)
    
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            


print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))