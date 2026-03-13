students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 92},
]

# Sort by grade
sorted_students = sorted(students, key=lambda student: student["grade"])

print(sorted_students)