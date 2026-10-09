
# Student Records Program

names = []
marks = []

# Add student records
n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"\nEnter student {i + 1} name: ")
    mark = float(input(f"Enter marks for {name}: "))

    names.append(name)
    marks.append(mark)

# Display student records
print("\n--- Student Records ---")
for i in range(len(names)):
    print(names[i], ":", marks[i], "marks")

# Search for a student
search_name = input("\nEnter student name to search: ")

if search_name in names:
    index = names.index(search_name)
    print(search_name, "scored", marks[index], "marks.")
else:
    print("Student not found.")

# Sort records by marks
sorted_records = sorted(zip(names, marks), key=lambda x: x[1])

print("\n--- Students Sorted by Marks ---")
for name, mark in sorted_records:
    print(name, ":", mark, "marks")

# Find highest and lowest scores
if marks:
    highest = max(marks)
    lowest = min(marks)

    print("\nHighest Score:", highest)
    print("Top Student(s):")
    for i in range(len(marks)):
        if marks[i] == highest:
            print(names[i])

    print("\nLowest Score:", lowest)
    print("Student(s) with Lowest Score:")
    for i in range(len(marks)):
        if marks[i] == lowest:
            print(names[i])
