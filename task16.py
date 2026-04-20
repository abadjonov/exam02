def count_by_grade(grades: dict, target_grade: int) -> dict:
    matched_students = [name for name, grade in grades.items() 
                        if grade == target_grade]
    
    return {
        "count": len(matched_students),
        "students": matched_students
    }

print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))
print(count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4))