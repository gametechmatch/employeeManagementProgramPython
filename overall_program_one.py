########################################################################
# overall_program_one.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This is the main program that runs all code
########################################################################
# import other classes and programs
from user_validation import *
from employees import *
from production_worker import *

########################################################################
# This function is the main function that runs all code
########################################################################
def main():
    # Set up dictionary called "employees" to work with
    employees = {'12345': ['Jane Doe', '12345', 1 , '15.75'],
                 '01': ['Mary Ann', '01'],
                 '02': ['Tina George', '02', 2 , '17.00']}

    working = True
    while working:

        # Ask user for menu option to choose from
        choice, choice_message = main_menu()

        # Route to the correct function depending on the menu option chosen
        if choice == 1:  # Print employees
            # Check if dictionary empty
            empty_result = check_if_dictionary_empty(employees, choice_message)

            # If dictionary is not empty, proceed with printing
            if empty_result == "not_empty":
                Employees.print_employees(employees)

        elif choice == 2:  # Add employee
            employees = adding_employee(employees, choice_message)

        elif choice == 3:  # Delete employee
            employees = deleting_employee(employees, choice_message)

        elif choice == 4:  # Save and quit
            working = False

        else:
            print("Overall Program Error")

########################################################################
# This function processes the request to add an employee to the
# dictionary "employees"
########################################################################
def adding_employee(employees, choice_message):
    still_adding = True
    while still_adding:
        # Get the employee number
        employee_number = get_employee_number()

        # Check if employee number already in employees
        employee_number_check = find_employee_number(employee_number, employees)

        # Return to main menu if employee number already in dictionary
        # "employees"
        if employee_number_check == 'in':
            print("That number already exists for the following employee:")
            Employees.print_individual_employee(employee_number, employees)

        # Continue the add request if employee not in "employees"
        else:
            # Get the employee type
            employee_type = get_employee_type(choice_message)

            # If user enters 1 for production worker
            if employee_type == 1:
                # Obtain info for employee to add
                name, shift, pay = get_employee_info(employee_type)

                # Re-print what user entered
                repeat_user_input(employee_number, name, shift, pay)

                # Ask user for confirmation to add employee
                confirmation = simple_choice_confirmation(choice_message)

                # If user enters y for yes, add employee
                if confirmation == 'y':
                    employees = Production_Worker.add_production_worker(employee_number,
                                                                        name, shift, pay, employees)

            # If user enters 2 for all other employees
            elif employee_type == 2:
                # Obtain information for employee to add
                name = get_employee_info(choice_message)

                # Re-print what user entered
                repeat_user_input(employee_number, name, 0, 0)

                # Ask user for confirmation to add employee
                confirmation = simple_choice_confirmation(choice_message)

                # If user enters y for yes, add employee to dictionary "employees"
                if confirmation == 'y':
                    employees = Employee.add_employee(employee_number, name, employees)
            else:
                print("Adding worker error")
                print(employee_type)
                print(type(employee_type))

        # Ask user if they need to add another employee
        add_another = try_again_confirmation(choice_message)

        # Exit to the main menu if user enters n for no to add another employee
        if add_another == 'n':
            return employees

########################################################################
# This function processes the request to delete an employee from the
# dictionary "employees"
########################################################################
def deleting_employee(employees, choice_message):
    still_deleting = True
    while still_deleting:
        # Check if dictionary empty
        empty_result = check_if_dictionary_empty(employees, choice_message)

        # If dictionary is not empty, proceed with printing
        if empty_result == "empty":
            return employees

        # Get the employee number
        employee_number = get_employee_number()

        # Check if employee number is in dictionary "employees"
        employee_number_check = find_employee_number(employee_number, employees)

        # If employee number not in dictionary "employees" return to main menu
        if employee_number_check == 'not in':
            print("I'm sorry. That employee number is not present in the current" 
                  "list of employees.")

        # If employee number in dictionary "employees" continue with delete request
        else:
            # Print the employee info
            Employees.print_individual_employee(employee_number, employees)

            # Ask user for confirmation to delete employee
            confirmation = simple_choice_confirmation(choice_message)

            # If user enters y for yes, delete employee
            if confirmation == 'y':
                employees = Employee.delete_employee(employee_number, employees)

        # Ask user if they need to delete another employee
        add_another = try_again_confirmation(choice_message)

        # Exit to the main menu if user enters n for no to add another employee
        if add_another == 'n':
            return employees

###########################################################################################
# This  function checks if the dictionary "employees" is empty
###########################################################################################
def check_if_dictionary_empty(employees, choice_message):
    if employees:
        return "not_empty"
    else:
        print("I'm sorry. The dictionary is currently empty."
              f"There are no employees to {choice_message}")
        return "empty"

#Execute main program
if __name__ == '__main__':
    main()
