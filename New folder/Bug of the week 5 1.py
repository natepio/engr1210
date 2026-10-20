grade_book = {
    "alice": 95,
    "bob": 82,
    "carlos": 90,
    "diana": 78,
    "eve": 93,
}
# --- Grade Lookup ---
student = "alice"
print(f"{student.capitalize()}'s grade: {grade_book[student]}")
print()
# --- All Grades ---
print("--- All Grades ---")
for name, grade in grade_book.items():
    print(f"{name}: {grade}")
print()
# --- Honor Roll (grade >= 90) ---
print("--- Honor Roll (grade >= 90) ---")
for name, grade in grade_book.items():
    if grade >= 90:
        print(f"{name.capitalize()} made the honor roll!")
print()
# --- Top Student ---
print("--- Top Student ---")
top_grade = 0
top_student = ""
for name, grade in grade_book.items():
    if grade > top_grade:
        top_grade = grade
        top_student = name
if top_student:
    print(f"Top student: {top_student.capitalize()} with a {top_grade}")
else:
    print("No top student found")