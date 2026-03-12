class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, my name is {self.name}. I am {self.age} years old and in grade {self.grade}."

    def is_passing(self):
        return self.grade >= 50


# Creating an object
student1 = Student("Alice", 16, 85)

print(student1.introduce())
print("Passing:", student1.is_passing())