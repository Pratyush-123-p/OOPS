# Python code to craete a parametrized constructor for employee class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# Example usage:
# Creating an Employee object with name "John", age 30, and salary 50000
john = Employee("John", 30, 50000)

# Accessing the attributes of the created object
print("Name:", john.name)
print("Age:", john.age)
print("Salary:", john.salary)
