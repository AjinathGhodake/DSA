# 1.	Create a dictionary with student names as keys and their grades as values:
# •	Input: {'Alice': 90, 'Bob': 85, 'Charlie': 92}
# •	Print the grade for "Charlie".
student = {"Alice": 90, "Bob": 85, "Charlie": 92}
print("Students names>>>", student["Charlie"])

# 2.	Add a new student to the dictionary and update an existing student’s grade:
# •	Add "David" with a grade of 88.
# •	Update "Bob"’s grade to 89.
student["David"] = 88
student["Bob"] = 89
print("Update and add student>>>", student)

# 3.	Remove a student from the dictionary and return their grade:
# •	Remove "Alice" and print her grade.

del student["Alice"]
print("Delete Alice student>>>", student)

# 4.	Create a dictionary comprehension:
# •	Create a dictionary where keys are numbers from 1 to 4, and values are their cubes.
# •	Expected output: {1: 1, 2: 8, 3: 27, 4: 64}

print("Expected output: {1: 1, 2: 8, 3: 27, 4: 64}>>>", {i: i**3 for i in range(1, 5)})
