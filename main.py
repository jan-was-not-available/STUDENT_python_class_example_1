import os
os.system("clear") # 
# Do not modify code above his line.

from module import Student
# Run this code. There are several mistakes that must be fixed before the module can be shipped to use in schools.
# Bugs that need to be fixed are listed below.
 
# TODO 1: Student names are not being printed properly in Section 1.
# TODO 2: Student greetings are missing in Section 2.
# TODO 3: Letter grade are printed as 'D' when the student has a higher letter grade in Sections 1 & 3.


# Create student instances
s1 = Student("Ava", 10, [88, 92, 89])
s2 = Student("Liam", 11, [60, 70, 50])

# Print-out Student Properties
print("SECTION 1\n")
print("Student 1:", s1.name)
print("Grade Level:", s1.grade_level)
print("Scores:", s1.scores)
print("Average:", int(s1.average))
print("Letter Grade:", s1.get_letter_grade())

print("\n") # Blank line

print("Student 2:", s2.name)
print("Grade Level:", s2.grade_level)
print("Scores:", s2.scores)
print("Average:", int(s2.average))
print("Letter Grade:", s2.get_letter_grade())

print("-----------------------------------------\n") # Horizontal Line


print("SECTION 2\n")

# Greetings and passing
s1.greet()
print("Passing:", s1.is_passing())

print() # Blank Line

s2.greet()
print("Passing:", s2.is_passing())

print("-----------------------------------------\n") # Horizontal Line

# Update with new scores
print("SECTION 3\n")
s1.add_score(95)
print("After adding a new score to Ava:")
print("New average:", int(s1.average))
print("New letter grade:", s1.get_letter_grade())
print("\n")