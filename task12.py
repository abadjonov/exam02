def sort_names(students: list) -> list:
    return sorted(students, key=lambda x: x.lower())

print(sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"]))
print(sort_names(["Zara", "Bobur", "Anvar"]))
