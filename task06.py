def analyze_grades(students: dict) -> dict:
        
    grades = list(students.values())
    average = sum(grades) / len(grades)
    
    above_avg_students = [name for name, grade in students.items() if grade > average]
    
    return {
        "average": average,
        "above_average": above_avg_students
    }

print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))
print(analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5}))
