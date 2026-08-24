students = [
    {'name': 'Thato', 'maths': 78, 'english': 65, 'science': 82},
    {'name': 'Palesa', 'maths': 55, 'english': 48, 'science': 60},
    {'name': 'Neo', 'maths': 90, 'english': 88, 'science': 95},
    {'name': 'Kat', 'maths': 42, 'english': 38, 'science': 45},
    {'name': 'Lionel', 'maths': 70, 'english': 72, 'science': 68},
]

results = []
all_marks = []

# Loop through every student and calculate their average
for student in students:
    maths = student['maths']
    english = student['english']
    science = student['science']

    average = (maths + english + science) / 3

    if average >= 80:
        grade = "A"
        status = "Pass"
    elif average >= 70 and average <= 79:
        grade = "B"
        status = "Pass"
    elif average >= 60 and average <= 69:
        grade = "C"
        status = "Pass"
    elif average >= 50 and average <= 59:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    results.append({
        'name': student['name'],
        'average': round(average, 2),
        'grade': grade,
        'status': status
    })

    all_marks.extend([maths, english, science])

class_average = sum(r['average'] for r in results) / len(results)
highest_mark = max(all_marks)
lowest_mark = min(all_marks)

print("\n===================================")
print("        CLASS GRADE REPORT")
print("===================================")

for r in results:
    print(f"\nName: {r['name']}")
    print(f"Average: {r['average']}")
    print(f"Grade: {r['grade']}")
    print(f"Status: {r['status']}")

print("\n===================================")
print("        CLASS STATISTICS")
print("===================================")
print(f"Class Average: {round(class_average, 2)}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print("===================================\n")

# Let the user search for a student by name after the report is shown
while True:
    search_name = input("Enter a student's name to search (or type 'exit' to quit): ").strip()

    if search_name.lower() == "exit":
        print("Goodbye!")
        break

    found = False
    for r in results:
        if r['name'].lower() == search_name.lower():
            print(f"\nName: {r['name']}")
            print(f"Average: {r['average']}")
            print(f"Grade: {r['grade']}")
            print(f"Status: {r['status']}\n")
            found = True
            break

    if not found:
        print(f"No student found with the name '{search_name}'.\n")