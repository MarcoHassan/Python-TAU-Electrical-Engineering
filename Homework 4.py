# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:39:05 2018

@author: Marco Hassan
"""
###############################
# Homework 4
# Name: TYPE YOUR NAME HERE
# Student ID: TYPE YOUR ID HERE
###############################

#------------------------------------------------------------------------------
#
#                Change the code only in the relevant places!
#
#------------------------------------------------------------------------------
def print_database(seats_plan):
    ''' Print out the seats database
        Print '.' for every free seat.
        Print 'X' for every occupied seat.
    '''
    # Your code for question #1 starts here
    
    for row in seats_plan:
        s = ""
        for column in row:
            if column == True:
                s += str(".") + " "
            else:
                s += str("X") + " "
        print(s)
    
    # Your code for question #1 ends here
    
#------------------------------------------------------------------------------
def check_indexes(n, row, seat):
    ''' Check whether the indexes fit the database size
        n:      Size of seats database
        row:    The row number of the required seat
        seat:   The index of the required seat in the row
        Return: Boolean answer
    '''
    # Your code for question #2 starts here
    
    if n > row and n > seat:
        return True
    
    else:
        return False
    
    # Your code for question #2 ends here

#------------------------------------------------------------------------------
def make_reservation(seats_plan, row, seat):
    ''' Book a specific seat if it is available
        seats_plan: The seats database, a 2D array of booleans
        row:        The row index of the required seat
        seat:       The index of the required seat in the row
        Return:     True upon the case when the seat was available
                    False otherwise
    '''
    # Your code for question #3 starts here
    
    if seats_plan[row][seat] == True:
        seats_plan[row][seat] = False
        return True
    
    else:
        return False
    
    
    # Your code for question #3 ends here

#------------------------------------------------------------------------------
def cancel_reservation(seats_plan, row, seat):
    ''' Cancel a reservation of a specific seat
        seats_plan: The seats database, a 2D array of booleans
        row:        The row index of the required seat
        seat:       The index of the required seat in the row
        Return:     True upon the case when the seat was reserved
                    False otherwise
    '''
    # Your code for question #4 starts here
    
    if seats_plan[row][seat] == False:
        seats_plan[row][seat] = True
        return True
    
    else:
        return False
    
    # Your code for question #4 ends here

#------------------------------------------------------------------------------
#
#                  DO NOT CHANGE CODE BEYOND THIS POINT
#
#------------------------------------------------------------------------------
def setup_database(n):
    ''' Prepare the seats. All the seats are available
        at the beginning. Allocate a 2D array of booleans.
        Initialize all the values to True.
        n:  The size of the array.
        Return: The seats database.
    '''
    seats_plan = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(True)
        seats_plan.append(row)    
    return seats_plan 

#------------------------------------------------------------------------------
def print_main_menu():
    print( 'Main Menu:')
    print( '[1] Print seats database')
    print( '[2] Make reservation')
    print( '[3] Cancel reservation')
    print( '[4] Quit')
    
#------------------------------------------------------------------------------
def convert_input_to_command(choice):
    ''' Analyze input string. If the string contains one
        of the predefined values then convert the obtained
        value into an integer command.
        Otherwise return the input string 
        Return: command index
    '''
    result = choice
    if '1' == choice or\
       '2' == choice or\
       '3' == choice or\
       '4' == choice:
        result = int(choice)
    return result

#------------------------------------------------------------------------------
def ask_for_row_and_seat(n):
    ''' Ask user to give the row and seat numbers to operate on.
        Pay attention that user counts seats in the range 0 to N.
        Return: row and seat indexes
    '''
    row = int(input('Enter row number [0-{0}]'.format(n-1)))
    seat = int(input('Enter seat number [0-{0}]'.format(n-1)))
    return row,seat

#------------------------------------------------------------------------------
def report_command_result(command, result):
    if 2 == command:
        if result:
            print( 'The seat is reserved')
        else:
            print( 'The seat was reserved already')
    elif 3 == command:
        if result:
            print( 'The seat is available again')
        else:
            print( "The seat wasn't reserved")
    
#------------------------------------------------------------------------------
''' The entry point. Allocate database, run dialog loop
    till user decides to quit
'''
# The size of the cinema database
n = 5

# Auxiliary checks
test_database = setup_database(n)
assert check_indexes(5,4,3) == True, \
       'A correct index is considered invalid.'
assert check_indexes(5,5,3) == False, \
       'An invalid index is considered correct.'
assert make_reservation(test_database,3,4) == True, \
       'Reservation of a vacant seat failed.'
assert make_reservation(test_database,3,4) == False, \
       'Reservation of a booked seat succeeded.'
assert cancel_reservation(test_database,3,4) == True, \
       'Cancelling reservation of a booked seat failed.'
assert cancel_reservation(test_database,3,4) == False, \
       'Cancelling reservation of a vacant seat succeeded.'

# Allocate the cinema database
seats_plan = setup_database(n)

# Interactive dialog processing starts here
while True:
    print_main_menu()
    choice = input( 'Enter [1-4]:')
    command = convert_input_to_command(choice)
    if 1 == command:
        print_database(seats_plan)
    elif 2 == command or 3 == command:
        row, seat = ask_for_row_and_seat(n)
        if not(check_indexes(n, row, seat)):
            print( 'Invalid request. Index is out of range.')
            continue
        result = True
        if 2 == command:
            result = make_reservation(seats_plan, row, seat)
        else:
            result = cancel_reservation(seats_plan, row, seat)
        report_command_result(command, result)    
    elif 4 == command:
        break
    else:
        print( 'Invalid choice')

#============================ END OF FILE =====================================

