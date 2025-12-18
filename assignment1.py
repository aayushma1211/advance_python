## Question 1: Data Types and Input Handling
Take student name, roll number, age, and marks as input.  
Display each value with its data type.  
Convert age to float and marks to int before displaying.

#Code:
# Write your answer here
name = input("Enter name:")
roll_number = input("Enter a roll number:")
age = input ("Enter age:")
marks = input("Enter a marks:")

# conversion
age1 = float(age)
marks1 = int(marks)

# print
print("Name:",name ,"Type:",type(name))
print("Roll_number:",roll_number,"Type:",type(roll_number))
print("Age:",age1,"Type:",type(age1))
print("Marks:",marks1,"Type:",type(marks1))

# output is:
# Enter name: aayushma
# Enter a roll number: 1
# Enter age: 21
# Enter a marks: 100
# Name: aayushma Type: <class 'str'>
# Roll_number: 1 Type: <class 'str'>
# Age: 21.0 Type: <class 'float'>
# Marks: 100 Type: <class 'int'>

## Question 2: Conditional Logic
Accept marks (0–100) and display:
- Excellent (≥80)
- Good (≥60)
- Pass (≥40)
- Fail (<40)

#Code:
# Accept marks from the user
marks = int(input("Enter marks (0-100): "))

# Check conditions and display result
if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
    
#output is
# Enter marks (0-100):  80
# Excellent


## Question 3: Looping with Conditions
Print numbers between 1 and 100 that are divisible by 4 but not divisible by 8.

#Code:
# Loop through numbers from 1 to 100
for i in range(1, 101):
    # Check if number is divisible by 4 but not divisible by 8
    if i % 4 == 0 and i % 8 != 0:
        print(i)
        
#output is
# 4
# 12
# 20
# 28
# 36
# 44
# 52
# 60
# 68
# 76
# 84
# 92
# 100

## Question 4: List Operations
Given:
marks = [55, 72, 48, 90, 67, 72, 90]
Find max, min, count of 72, and marks ≥ 60.

#Code:
#list
marks = [55, 72, 48, 90, 67, 72, 90]
print( "count of 72:",marks.count(72))

print( "Maximum:",max(marks))
print("Minimum:",min(marks))
#using if inside for loop
for i in marks:
    if i>=60:
        print(i)
        
# output is:
# count of 72: 2
# Maximum: 90
# Minimum: 48
# 72
# 90
# 67
# 72
# 90

## Question 5: Tuple and Immutability
Create a tuple of 5 subjects and attempt modification.  
Explain result using comments.

#Code:
tuple = ("math","phy","chem","bio","nep")
print("Subject:",tuple)
#modify:
tuple[1] ="eng" # here type error occur because tuple is immutable in python so it doesnot support item assignment


## Question 6: List Sanitization and Metrics
Given:
marks = [45, -3, 88, "NA", 102, None, 67]
Write a function that:
1. Removes invalid entries  
2. Returns:
   - Cleaned list  
   - Number of invalid entries  
   - Percentage of valid marks  

Return values using a tuple.

#Code:
# marks
marks = [45, -3, 88, "NA", 102, None, 67]

def sanitize_marks(marks):
    valid_marks = []        # list to store valid marks
    invalid_count = 0       # counter for invalid entries

    for m in marks:
        # Check if mark is an integer and between 0 and 100
        if isinstance(m, int) and 0 <= m <= 100:
    # in isinstance m is value you want to check and int is The type or class you want to check against (can also be a tuple of types).
            valid_marks.append(m) #this line takes the value m and adds it to the list valid_marks
        else:
            invalid_count += 1

    # Calculate percentage of valid marks
    total = len(marks) # 7
    valid_percentage = (len(valid_marks) / total) * 100 ## Output: 42.857142857142854

    # Return results as a tuple
    return valid_marks, invalid_count, valid_percentage


# Function call
result = sanitize_marks(marks)
# result[0] → The first item of the tuple, which is valid_marks (the cleaned list).

# result[1] → The second item (invalid_count).

# result[2] → The third item (valid_percentage).

# In Python, when a function returns multiple values using a tuple, you can access each value by its index, starting from 0.
# Display results
print("Cleaned list:", result[0])
print("Number of invalid entries:", result[1])
print("Percentage of valid marks:", result[2])

# output is:
# Cleaned list: [45, 88, 67]
# Number of invalid entries: 4
# Percentage of valid marks: 42.857142857142854

## Question 7: Dictionary Usage
Create a dictionary of roll number and name.  
Implement add, update, and display operations using functions.

#Code:
# Function to add a student
def add_student(students, roll, name):
    students[roll] = name   # add roll and name to dictionary

# Function to update a student name
def update_student(students, roll, name):
    students[roll] = name   # update name for given roll number

# Function to display all students
def display_students(students):
    for roll, name in students.items():
        print("Roll:", roll, "Name:", name)

# Create empty dictionary
students = {}

# Add students
add_student(students, 1, "Aayushma")
add_student(students, 2, "Sita")

# Update student name
update_student(students, 1, "Gita")

# Display all students
display_students(students)

#output
# Roll: 1 Name: Gita
# Roll: 2 Name: Sita

## Question 8: Prime Number Function
Write is_prime(n) and display prime numbers between 1 and 50.

#Code:
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Display prime numbers between 1 and 50
print("Prime numbers:")
for num in range(1, 51):
    if is_prime(num):
        print(num)
        
#output is
# Prime numbers:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47

## Question 9: Function Composition
Write functions to:
1. Calculate total marks  
2. Calculate average  
3. Classify result (Distinction / Pass / Fail)

Then write a function that combines them and returns:
(name, total, average, result)
Explain why modular design is beneficial.

#Code:
# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average(total, count):
    return total / count

# Function to classify result
def classify_result(average):
    if average >= 75:
        return "Distinction"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

# Function that combines all the above functions
def student_result(name, marks):
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = classify_result(average)

    # Return combined result as a tuple
    return name, total, average, result


# Example usage
name = "Aayushma"
marks = [70, 80, 65, 90]

output = student_result(name, marks)
print(output)

#output is
#('Aayushma', 305, 76.25, 'Distinction')
#  Why modular design is beneficial (simple explanation):
# Each function does one small task
# Code becomes easy to read and understand
# Easy to test and debug
# Functions can be reused in other programs
# Changes in one function don’t affect the whole program

## Question 10: Defensive Input Parsing
Write a function that accepts a raw input string in the format:
"Ram|101|22|78, 88, 91"
Hint: Parse student data from string format: "Name|Roll|Age|Mark1, Mark2, Mark3"

Tasks:
1. Extract name, roll number, age, and marks  
2. Convert them into appropriate data types  
3. Validate age (≥16) and marks (0–100)  
4. Return the result as a dictionary using roll number as the key  

The function must not crash for malformed input.

#Code:
# Function to safely parse student data from a raw input string
def parse_student_data(raw_input):

    try:
        # Split the input string using | as separator
        parts = raw_input.split("|")

        # Check if input has exactly 4 parts
        if len(parts) != 4:
            return "Invalid format"

        # Extract and clean student name
        name = parts[0].strip()

        # Convert roll number from string to integer
        roll = int(parts[1].strip())

        # Convert age from string to integer
        age = int(parts[2].strip())

        # Split marks string using comma
        marks_str = parts[3].split(",")

        # Convert each mark from string to integer
        marks = [int(m.strip()) for m in marks_str]

        # Validate age (must be 16 or above)
        if age < 16:
            return "Invalid age"

        # Validate each mark (must be between 0 and 100)
        for m in marks:
            if m < 0 or m > 100:
                return "Invalid marks"

        # Create and return dictionary using roll number as key
        return {
            roll: {
                "name": name,
                "age": age,
                "marks": marks
            }
        }

    except:
        # This block runs if any error occurs (wrong format, letters instead of numbers, etc.)
        return "Malformed input"


# Example raw input string
data = "Ram|101|22|78, 88, 91"

# Call the function and store the result
result = parse_student_data(data)

# Print the returned result
print(result)

# output is:
# {101: {'name': 'Ram', 'age': 22, 'marks': [78, 88, 91]}}

## Question 11: Type Stability and Conversion
Given the list:
python
data = [10, "20", 30.5, "abc", None, True]
Write a function that:
1. Separates numeric and non-numeric values  
2. Converts numeric values to float  
3. Returns both lists  
Explain in comments why `True` behaves as a numeric value.

#Code:
# Given list containing mixed data types
data = [10, "20", 30.5, "abc", None, True]

# Function to separate numeric and non-numeric values
def separate_and_convert(data):

    numeric_values = []      # list to store numeric values as float
    non_numeric_values = []  # list to store non-numeric values

    # Loop through each item in the list
    for item in data:

        # Check if item is int or float
        # NOTE: True is treated as a number because in Python
        # True = 1 and False = 0 (bool is a subclass of int)
        if isinstance(item, (int, float)):

            # Convert numeric value to float and store it
            numeric_values.append(float(item))

        # Check if item is a numeric string (e.g. "20")
        elif isinstance(item, str) and item.isdigit():

            # Convert string number to float and store it
            numeric_values.append(float(item))

        else:
            # If item is not numeric, store it in non-numeric list
            non_numeric_values.append(item)

    # Return both lists as a tuple
    return numeric_values, non_numeric_values


# Call the function
numbers, others = separate_and_convert(data)

# Print numeric values
print("Numeric values (as float):", numbers)

# Print non-numeric values
print("Non-numeric values:", others)

# output is :
# Numeric values (as float): [10.0, 20.0, 30.5, 1.0]
# Non-numeric values: ['abc', None]
# Why True behaves as a numeric value (simple explanation):
# True  == 1
# In Python, bool is a subclass of int

## Question 12: Pattern-Based Looping
Generate the sequence:
2, 6, 12, 20, 30, 42, 56
Rules:
- Do not hardcode the list  
- Use loops and conditionals only  
- Explain the pattern in comments

#Code:
# This program generates the sequence:
# 2, 6, 12, 20, 30, 42, 56

# Explanation of the pattern:
# Each number is formed by multiplying two consecutive numbers:
# 1×2 = 2
# 2×3 = 6
# 3×4 = 12
# 4×5 = 20
# 5×6 = 30
# 6×7 = 42
# 7×8 = 56

# Loop to generate the pattern
for i in range(1, 8):          # Loop from 1 to 7
    value = i * (i + 1)        # Multiply current number with the next number
    print(value, end=", ")     # Print the value in sequence format
    
# output is:
# 2, 6, 12, 20, 30, 42, 56, 

## Question 13: Set-Based Enrollment Analysis
Given:
python
python = {"Amit", "Sita", "Hari", "Nita"}
sql = {"Hari", "Ram", "Nita"}
statistics = {"Amit", "Hari", "Gita"}
Find:
1. Students enrolled in exactly two subjects  
2. Students enrolled in only one subject  
3. Students enrolled in all subjects

#Code:
# Given sets of students enrolled in different subjects
python = {"Amit", "Sita", "Hari", "Nita"}
sql = {"Hari", "Ram", "Nita"}
statistics = {"Amit", "Hari", "Gita"}


# Students enrolled in ALL subjects
# Use intersection (&) to find common students
all_subjects = python & sql & statistics # output is hari

# Students enrolled in EXACTLY TWO subjects
# Find students common in each pair of subjects
python_sql = python & sql # output is{"Hari","Nita"}
python_statistics = python & statistics#amit,hari
sql_statistics = sql & statistics#hari

# Combine all pair-wise intersections
two_subjects = (python_sql | python_statistics | sql_statistics) - all_subjects
# So "|" this sign represent union like combine the output from intersection{hari,nita,amit}


# Students enrolled in ONLY ONE subject
# Combine all students using union (|)
all_students = python | sql | statistics

# Remove students who are in two or more subjects
one_subject = all_students - two_subjects - all_subjects

# Print results
print("Students enrolled in all subjects:", all_subjects)
print("Students enrolled in exactly two subjects:", two_subjects)
print("Students enrolled in only one subject:", one_subject)

# output is:
# Students enrolled in all subjects: {'Hari'}
# Students enrolled in exactly two subjects: {'Amit', 'Nita'}
# Students enrolled in only one subject: {'Sita', 'Ram', 'Gita'}

## Question 14: Dictionary Aggregation Logic
Given:
python
records = {
    "Amit": [78, 82, 91],
    "Sita": [88, 79, 85],
    "Hari": [45, 52, 60]
}

Write a function that:
1. Computes average per student  
2. Identifies top and bottom performers  
3. Returns results using a single dictionary

#Code:
# Given dictionary of student records
records = {
    "Amit": [78, 82, 91],
    "Sita": [88, 79, 85],
    "Hari": [45, 52, 60]
}

# Function to compute averages, top and bottom performers
def analyze_records(records):
    # Dictionary to store averages
    averages = {}
    
    # Loop through each student in records
    for student, marks in records.items(): # here student is key and marks is value of records(dictionary)
        # Calculate average marks for each student
        avg = sum(marks) / len(marks)
        # Store the average in the dictionary
        averages[student] = avg
    
    # Identify the student with maximum average (top performer)
    top_performer = max(averages, key=averages.get)
#  This line do Checks all keys ("Amit", "Sita", "Hari")
# Compares their average values (83.67, 84.0, 52.33)
# Returns the key with the highest value, which is "Sita".
    
    # Identify the student with minimum average (bottom performer)
    bottom_performer = min(averages, key=averages.get)
    
   # Combine all results in a single dictionary
    result = {
        "averages": averages,  # Store all student averages
        "top_performer": {top_performer: averages[top_performer]},  # Store top performer as a dictionary
        "bottom_performer": {bottom_performer: averages[bottom_performer]}  # Store bottom performer as a dictionary
    }

    return result

# Call the function and store the result
result = analyze_records(records)

# Display the results
print("Analysis Result:", result)

# output is:
# Analysis Result: {
#     'averages': {'Amit': 83.66666666666667, 'Sita': 84.0,
#                  'Hari': 52.333333333333336},
#     'top_performer': {'Sita': 84.0},
#     'bottom_performer': {'Hari': 52.333333333333336}
# }

## Question 15: Nested Data Structure Analysis
Given a nested dictionary representing a school's grade book:
python
school_data = {
    "Class A": {
        "Amit": [78, 82, 91],
        "Sita": [88, 79, 85]
    },
    "Class B": {
        "Hari": [45, 52, 60],
        "Ram": [92, 88, 95]
    }
}

Write a function that:
1. Calculates the average marks for each student
2. Finds the top performer in each class
3. Calculates the overall school average
4. Returns a dictionary with:
   - `class_toppers`: {class_name: (student_name, average)}
   - `school_average`: float
   - `student_averages`: {student_name: average}

Explain in comments why nested dictionaries are useful for hierarchical data.

#Code:
# Given nested dictionary representing a school's grade book
school_data = {
    "Class A": {
        "Amit": [78, 82, 91],
        "Sita": [88, 79, 85]
    },
    "Class B": {
        "Hari": [45, 52, 60],
        "Ram": [92, 88, 95]
    }
}

# Function to analyze nested school data
def analyze_school(school_data):
    # Dictionary to store the topper of each class
    class_toppers = {}
    
    # Dictionary to store average marks of all students
    student_averages = {}
    
    # List to store all marks for calculating school average
    all_marks = []
    
    # Loop through each class
    for class_name, students in school_data.items():
        # Initialize variables to track class topper
        topper_name = None
        # Using 0 wouldn’t make sense here because 0 is a number, not a string or “empty name.”
        # None is Python’s standard way to represent “no data” or “unknown.”
        topper_avg = 0
        # Using None here would complicate comparisons because None > some_number raises an error.
        
        # Loop through each student in the class
        for student_name, marks in students.items():
            # Calculate average marks for the student
            avg = sum(marks) / len(marks)
            
            # Store in student_averages dictionary
            student_averages[student_name] = avg
            
            # Add student's marks to all_marks list for school average calculation
            all_marks.extend(marks)
            
            # Update class topper if this student has higher average
            if avg > topper_avg:
                topper_avg = avg
                topper_name = student_name
        
        # Store class topper in class_toppers dictionary
        class_toppers[class_name] = (topper_name, topper_avg)# output example {'Class B': ('ram, 92)}
    
    # Calculate overall school average
    school_average = sum(all_marks) / len(all_marks)
    
    # Return all results in a dictionary
    result = {
        "class_toppers": class_toppers,
        "school_average": school_average,
        "student_averages": student_averages
    }
    
    return result

# Call the function and store the result
result = analyze_school(school_data)

# Display the results
print("School Analysis Result:", result)

# Explain in comments why nested dictionaries are useful for hierarchical data.
# Nested dictionaries are useful for hierarchical data because:
# 1. They organize data in multiple levels (e.g., class → student → marks).
# 2. Easy to access and loop through different levels using keys.
# 3. Improve readability and maintainability for complex data.

# Nested dictionaries are useful here because they allow storing hierarchical data:
# Class → Student → Marks
# Easy to loop through classes and students.

# output is:
# School Analysis Result: {'class_toppers': 
#                          {'Class A': ('Sita', 84.0), 'Class B': ('Ram', 91.66666666666667)},
#                          'school_average': 77.91666666666667, 'student_averages': {'Amit': 83.66666666666667, 
#                         'Sita': 84.0, 'Hari': 52.333333333333336, 'Ram': 91.66666666666667}
#                         }

