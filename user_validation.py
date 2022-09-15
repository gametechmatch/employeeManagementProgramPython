########################################################################
# user_validation.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This program handles most user validation
########################################################################

########################################################################
# This function prints the main menu and returns the user's menu choice
# to the main program
########################################################################
def main_menu():
    valid_input = False
    while not valid_input:

        # Print the menu options and get the user choice
        choice = (input("___________________________________________________________________\n"
                        "| 1. Print Employees\n"
                        "| 2. Add Employee\n"
                        "| 3. Delete Employee\n"
                        "| 4. Save and Quit\n"
                        "___________________________________________________________________\n"
                        )).replace(" ", "").replace(".", "")

        # Check if the choice equals one of the menu options. Reprint the menu if invalid input
        # is given
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            valid_input = True
        else:
            valid_input = False

    # Convert the choice to an integer
    choice = int(choice)

    # Set up a message that corresponds to the menu choice selected
    if choice == 1:
        choice_message = "Print Employees"
        choice_message2 = 'print'
    elif choice == 2:
        choice_message = "Add Employee"
        choice_message2 = 'add'
    elif choice == 3:
        choice_message = "Delete Employee"
        choice_message2 = 'delete'
    elif choice == 4:
        choice_message = "Save and Quit"
        choice_message2 = 'save and quit'

    # Print message as a header for the menu option chosen
    print(f"\n*************** {choice}: {choice_message.upper()} ***************")

    # Return the choice and corresponding message to the main program
    return choice, choice_message2

###########################################################################################
# This functions gets the employee number (employee ID)
##########################################################################################
def get_employee_number():
    employee_number = "A"
    while not employee_number.replace(" ", "").isdigit():
        employee_number = input("Employee Number: ")

    # Return the employee number to the program using this function
    return employee_number

###########################################################################################
# This function gathers the type of employee
##########################################################################################
def get_employee_type(choice_message):
    # Obtain the type of employee that will be added
    waitingforvalidinput = True
    while waitingforvalidinput:
        print(f"Please enter the type of employee you want to {choice_message}.")
        employee_type = input("1 = Production Worker\n2 = All Other\n").replace(" ", "")

        # If user enters valid input, return input to main program,
        # otherwise, repeat loop
        if employee_type == '1' or employee_type == '2':
            employee_type = int(employee_type)
            return employee_type

###########################################################################################
# This function gets the employee information that is associated with the type of
# worker they are (either a production worker or all other types of workers)
##########################################################################################
def get_employee_info(employee_type):
    # 1 for adding production workers
    if employee_type == 1:
        name, shift, pay = get_production_worker_data()

        # Return data gathered to the program using this function
        return name, shift, pay

    # 2 for adding all non-production workers
    else:
        name = get_name()

        # Return data gathered to the program using this function
        return name

###########################################################################################
# This function gathers the data for all production workers
##########################################################################################
def get_production_worker_data():
    name = get_general_employee_data()
    shift = get_employee_shift()
    pay = get_employee_pay()

    # Return data gathered to the program using this function
    return name, shift, pay

###########################################################################################
# This function gathers the data for all non-production workers
##########################################################################################
def get_general_employee_data():
    name = get_name()

    # Return data gathered to the program using this function
    return name

###########################################################################################
# This function asks the user for the employee's name
##########################################################################################
def get_name():
    # Ask user for employee first name
    employee_first_name = "1"
    while not employee_first_name.replace(" ", "").isalpha():
        employee_first_name = input("Employee First Name: ").upper()

    # Ask user for employee last name
    employee_last_name = "2"
    while not employee_last_name.replace(" ", "").isalpha():
        employee_last_name = input("Employee Last Name: ").upper()

    # Put first and last name together
    employee_name = f"{employee_first_name} {employee_last_name}"

    # Return employee_name to program using this function
    return employee_name

###########################################################################################
# This function asks the user for the employee's shift
##########################################################################################
def get_employee_shift():
    # Ask user for employee shift
    waiting_for_valid_input = True
    while waiting_for_valid_input:
        print("Please enter a 1 for first shift or 2 for second shift.")
        employee_shift = input("Employee Shift: ")

        # If user enters a 1 or a 2, return input to program, otherwise,
        # ask for shift again
        if employee_shift == '1' or employee_shift == '2':
            employee_shift = int(employee_shift)

            # Return employee_shift to program using this function
            return employee_shift

###########################################################################################
# This function asks the user for the employee's pay
##########################################################################################
def get_employee_pay():
    getting_pay = True
    while getting_pay:

        # Ask user for employee pay
        employee_pay = "A"
        while not employee_pay.replace(" ", "").replace(".", "").isdigit() \
                or not len(employee_pay) >= 3:
            employee_pay = input("Employee Pay with cents: ")

        if '.' not in employee_pay[-1:-3] and employee_pay[-3] == '.' \
            and '.' not in employee_pay[:-3]:
                # Convert employee_pay from a string variable to a float variable
                employee_pay = float(employee_pay)

                # Return to program using this function if employee pay
                # within hourly pay range, otherwise, ask for pay again
                if employee_pay >= 15 and employee_pay <= 30:
                    return employee_pay
                else:
                    user_entered_pay = 'not in range'

###########################################################################################
# This function asks user if the program should exit to the main menu or loop back and
# let the user try the same menu option that was originally chosen
###########################################################################################
def try_again_confirmation(choice_message):
    waiting_for_valid_response = True
    while waiting_for_valid_response:
        # Ask user if they want to return to main menu or repeat selected menu option
        print("___________________________________________________________________\n"
              f"|Do you want to {choice_message} an additional employee?")
        user_input = input(f"|Y = yes\n|N = no\n"
                           "___________________________________________"
                           "________________________\n"
                           ).lower().replace(" ", "").replace(".", "")

        # If user enters valid input, return response to the program using this function
        if user_input == "y" or user_input == "n":
            return user_input

        # Print message and return to beginning of loop if invalid input entered
        else:
            print("\nI'm sorry. I did not understand.\n")

###########################################################################################
# This function asks user if the program should continue with a change when the data
# entered cannot be pulled from the "employees" dictionary
###########################################################################################
def simple_choice_confirmation(choice_message):
    waiting_for_valid_input = True
    while waiting_for_valid_input:
        # Print out info entered by user and ask if change should continue
        print(f"\nDo you want to {choice_message} the selected employee?")
        user_choice = input(f"Y = {choice_message} employee\n"
                            f"N = No do not {choice_message} employee:\n"
                            ).lower().replace(" ", "").replace(".", "")

        # If user enters valid input, return response to the program using this function
        if user_choice == "y" or user_choice == "n":
            print("\nSounds good.\n")
            return user_choice

        # Print message and return to beginning of loop if invalid input entered
        else:
            print("I'm sorry. I don't understand.")

###########################################################################################
# This function re-prints the info the user entered for an individual employee
##########################################################################################
def repeat_user_input(employee_number, name, shift, pay):
    print("\nYou entered:\n"
          f"Employee Number: {employee_number}\n"
          f"Name: {name}")
    # If the shift doesn't equal 0, then it is a production
    # worker and the shift and pay also will be printed
    if shift != 0:
        print(f"Shift: {shift}\n"
          f"Pay: {pay}")

###########################################################################################
# This function checks if an employee number exists in the dictionary "employees" and
# returns the result to the program using this function
##########################################################################################
def find_employee_number(employee_number, employees):
    if employee_number in employees:
        return 'in'
    else:
        return 'not in'
