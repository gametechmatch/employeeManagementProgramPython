########################################################################
# employee.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This program holds the Employee class
########################################################################

class Employee:

    # The __init__ method initializes the attributes
    def __init__(self, name):
        self.__name = name
        self.__employee_number = self

    # The setter methods accept arguments for the
    # name or employee number
    def set_name(self, name):
        self.__name = name

    def set_employee_number(self):
        self.__employee_number = self

    # The getter methods return the name or
    # employee number
    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__employee_number

    # The __str__ method returns the object's state as a string
    def __str__(self):
        return f'Name: {self.__name}\n\t' \
               f'Employee Number: {self.__employee_number}'

    # This method adds an employee to the dictionary "employees"
    def add_employee(self, name, employees):
        employees[self] = [name, self]
        return employees

    # This method deletes an employee from the dictionary "employees"
    def delete_employee(self, employees):
        if self in employees:
            del employees[self]
            print("Employee Deleted")
        return employees
