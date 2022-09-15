########################################################################
# production_worker.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This program holds the production_worker class
########################################################################

from employee import *

class Production_Worker(Employee):

    # The __init__ method initializes the attributes
    def __init__(self, name, shift_number, pay_rate):
        Employee.__init__(self, name)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # The setter methods accept arguments for the
    # shift or pay rate
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # The getter methods return the shift or
    # pay rate
    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate

    # The __str__ method returns the object's state as a string
    def __str__(self):
        Employee.__str__(self)
        return f'Shift Number: {self.__shift_number}\n\t' \
               f'Pay Rate: {self.__pay_rate}'

    # This method adds a production worker to the dictionary "employees"
    def add_production_worker(self, name, shift_number, pay_rate, employees):
        employees[self] = [name, self, shift_number, pay_rate]
        return employees
