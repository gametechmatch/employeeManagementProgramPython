########################################################################
# employees.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This program holds the Employees class
########################################################################
from production_worker import *

class Employees:

    ########################################################################
    # This method prints all employee data in the dictionary "employees"
    ########################################################################
    def print_employees(self):
        for employee in self.values():
            print(f"\nEmployee Name: {employee[0]}\n"
                  f"Employee Number: {employee[1]}")
            if len(employee) == 4:
                print(f"Employee Shift: {employee[2]}\n"
                      f"Employee Pay: {employee[3]}")

    ########################################################################
    # This method prints the data for an individual employee
    ########################################################################
    def print_individual_employee(self, employees):

        # Make a holder for the employee info
        this_employee = list(employees[self])

        # Print the applicable employee info
        print(f"\nEmployee Name: {this_employee[0]}\n"
              f"Employee Number: {this_employee[1]}")
        if len(this_employee) == 4:
            print(f"Employee Shift: {this_employee[2]}\n"
                  f"Employee Pay: {this_employee[3]}")
