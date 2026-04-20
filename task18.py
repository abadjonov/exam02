def square_values(numbers: list) -> list:
    return [{'value': item['value'] ** 2}
             for item in numbers]

print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))
print(square_values([{'value': -2}, {'value': 5}]))
