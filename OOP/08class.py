from abc import ABC, abstractmethod

# Base class (Abstract)
class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_details(self):
        return f"ID: {self.employee_id}, Name: {self.name}"


# Regular full-time employee
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Manager inherits from FullTimeEmployee
class Manager(FullTimeEmployee):
    def __init__(self, name, employee_id, monthly_salary, bonus):
        super().__init__(name, employee_id, monthly_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus


# Developer paid hourly
class Developer(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


#Using the system

employees = [
    FullTimeEmployee("Alice", 101, 5000),
    Manager("Bob", 102, 7000, 2000),
    Developer("Charlie", 103, 50, 160)
]

for emp in employees:
    print(emp.get_details())
    print("Salary:", emp.calculate_salary())
    print("-" * 30)