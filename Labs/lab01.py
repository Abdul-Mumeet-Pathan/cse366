# -*- coding: utf-8 -*-
"""366_Lab01_AMP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CMC-PbqjNEoWYNWl_wgglqjrCznlo_Jb

**Name: Abdul Mumeet Pathan**

**ID: 2022-1-60-267**

Instructions:
1. Read the student IDs from a text file (e.g., student_ids.txt) containing
multiple student IDs, one per line, in the format YYYY-N-MM-xxx (e.g., 2024-1-05-
123).
2. Maintain a list of students who haven’t been selected yet.
3. Randomly select a student for viva from the list.
4. Remove the selected student from the list.
5. Repeat steps 3 and 4 until all students have been picked.
6. When all students have been selected, reset the list to include all students
again.

Additional Considerations:
1. There should be error handling (e.g., for file not found).
2. The format of the output (e.g., add a "Viva #" counter) should be understandable.
"""

import random
import re
import os

# Parameters for ID generation
num_ids = 100
year_range = (2018, 2024)
id_pattern = re.compile(r"^\d{4}-[1-3]-\d{2}-\d{3}$")

# Function to validate the format of the student ID
def is_valid_id(student_id):
    return bool(id_pattern.match(student_id))

# Generate unique student IDs with validation and additional constraints
student_ids = []  # List to store all unique IDs
attempts = 0      # Counter to avoid infinite loops in case of constraint issues
max_attempts = 100  # Max attempts to generate valid IDs

while len(student_ids) < num_ids and attempts < max_attempts:
    # Generate random components for the student ID
    year = random.randint(*year_range)
    n = random.randint(1, 3)  # Valid range for "n" is 1 to 3
    month = f"{random.randint(1, 12):02}"  # Ensures two digits for the month, range 01-12
    last_digits = f"{random.randint(0, 999):03}"  # Ensures three digits for the last part, range 000-999
    student_id = f"{year}-{n}-{month}-{last_digits}"

    # Check if the generated ID is valid, unique, and matches the required format
    if is_valid_id(student_id) and student_id not in student_ids:
        student_ids.append(student_id)  # Add ID to list if it passes all checks
        print(f"Generated ID: {student_id}")  # Print each valid, unique ID as it is generated
    else:
        print(f"Skipped duplicate or invalid ID: {student_id}")

    attempts += 1

# Alert if unable to generate enough unique IDs
if len(student_ids) < num_ids:
    print(f"Warning: Only {len(student_ids)} unique IDs were generated after {attempts} attempts.")

# Write the full list of unique, validated IDs to a file, with error handling
try:
    with open("student_ids.txt", "w") as file:
        for student_id in student_ids:
            file.write(student_id + "\n")
    print("\nAll generated student IDs have been validated and saved to 'student_ids.txt'.")
except IOError:
    print("Error: Unable to write to 'student_ids.txt'. Please check file permissions.")

import random

# Define the parameters for ID generation
num_ids = 5 # Number of IDs to generate
year = 2018  # Fixed year for the generated IDs
student_ids = []  # List to store the generated IDs

# Function to generate a new student ID in the required format
def generate_student_id():
    n = random.randint(1, 3)  # Random number between 1 and 3
    month = f"{random.randint(1, 12):02}"  # Random month between 01 and 12
    last_digits = f"{random.randint(0, 999):03}"  # Random last three digits
    return f"{year}-{n}-{month}-{last_digits}"

while len(student_ids) < num_ids:
    new_id = generate_student_id()
    if new_id not in student_ids:  # Ensure uniqueness
        student_ids.append(new_id)

# Display the newly generated IDs (for reference)
print("Generated student IDs for 2024:")
for student_id in student_ids:
    print(student_id)


not_selected_students = [student_id for student_id in student_ids if student_id.startswith("2024")]

# Randomly select a student for viva, remove them from the list, and repeat until all are picked
while not_selected_students:  # Continue until all students have been selected
    selected_student = random.choice(not_selected_students)  # Randomly select a student
    print(f"\nSelected student for viva (from year 2024): {selected_student}")

    # Remove the selected student from the list
    not_selected_students.remove(selected_student)

# Read existing student IDs from 'student_ids.txt' if the file exists
try:
    with open("student_ids.txt", "r") as file:
        existing_ids = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    existing_ids = []  # If the file doesn't exist, start with an empty list

while len(student_ids) < num_ids:
    new_id = generate_student_id()
    if new_id not in existing_ids and new_id not in student_ids:  # Ensure uniqueness
        student_ids.append(new_id)

# Write both old and new student IDs to 'student.txt'
with open("student.txt", "w") as file:
    # Write existing IDs from 'student_ids.txt' first
    for student_id in existing_ids:
        file.write(student_id + "\n")

    # Write newly generated IDs
    for student_id in student_ids:
        file.write(student_id + "\n")

# Print all student IDs from 'student.txt'
with open("student.txt", "r") as file:
    print("All student IDs (existing and new) from 'student.txt':")
    all_student_ids = file.readlines()
    for student_id in all_student_ids:
        print(student_id.strip())  # Remove the trailing newline and print