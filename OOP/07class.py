class Student:
    # Class variable (shared by all objects)
    school_name = "ABC School"

    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.data = {self.name: self.marks}  # store in dictionary

    # Instance method
    def display(self):
        print("Student Data:", self.data)

    # Instance method
    def update_marks(self, new_marks):
        self.marks = new_marks
        self.data[self.name] = new_marks
        print("Marks updated!")

    # Class method
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school
        print("School name changed to", cls.school_name)

    # Static method
    @staticmethod
    def is_pass(marks):
        return marks >= 40

    # Magic method
    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}, School: {self.school_name}"


# Taking input from user
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

# Creating object
s1 = Student(name, marks)

# Using methods
s1.display()
print(s1)

print("Pass Status:", Student.is_pass(marks))

s1.update_marks(85)
s1.display()

Student.change_school("XYZ School")
print(s1)