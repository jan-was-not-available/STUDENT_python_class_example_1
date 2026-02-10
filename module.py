#  Define the Student class
class Student:
    def __init__(self, name, grade_level, scores):
        self.name = name                 # string
        self.grade_level = grade_level    # int (e.g., 9, 10, 11)
        self.scores = scores              # list of numbers
        self.average = self.calculate_average()  # computed property


    def calculate_average(self):    # Average: Divide the sum of all scores by the amount of scores
        return sum(self.scores) / len(self.scores) 


    def add_score(self, new_score): # Add a new score and recalculate the average based on the new score
        self.scores.append(new_score)
        self.average = self.calculate_average()


    def greet(self):                # Print a formatted string that contains the student's name and grade level
        print(f"Hi, my name is {self.name} and I'm in grade {self.grade_level}.") 


    def is_passing(self):           # Return a boolean that indicates if the student is passing
        return self.average >= 63


    def get_letter_grade(self):     # Return a string that indicates the student's letter grade
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 63:
            return "D"
        else:
            return "F"