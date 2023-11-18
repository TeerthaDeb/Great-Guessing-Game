# The code you provided is the main script of a Python program. Users are expected to run the program from here.:

import sys
import os
import Guess
import StringDatabase

debug = False ## for debugging only

if __name__ == "__main__":

    os.system("cls") ## clears the screen

    command_line_args = sys.argv[1:] #Store the commandline Arguments in 'command_line_args'

    # The code is checking if the variable `debug` is set to `True`. If it is, then it prints the
    # message "Command line arguments are " followed by the value of the `command_line_args` variable.
    # This is used for debugging purposes to see the command line arguments that were passed to the
    # script.
    if(debug):
        print("Command line arguments are ", command_line_args)

    # The code is checking if the string 'test' is present in the command line arguments. If it is,
    # then the variable `test_allowed` is set to `True` and the message "Test has been allowed" is
    # printed. Otherwise, `test_allowed` remains `False`.

    test_allowed = False #this variable will keep track if test is allowed or not.

    # This code is checking if the string 'test' is present in the command line arguments. If it is,
    # then it sets the variable `test_allowed` to `True` and prints the message "Test has been
    # allowed". This allows the script to enable certain test functionality if the 'test' argument is
    # passed in the command line.
    if 'test' in command_line_args:
        test_allowed = True
        print("Test has been allowed")

    if "test" not in command_line_args and "play" not in command_line_args:
        print("You did not enter in what mode you are trying to run the program.")
        print("However this program will run in play mode by default. if you want to run in test mode, write 'test' in the command line argument while starting the program.")

    input("Press any key to continue.")

    strdtbs1 = StringDatabase.StringDataBase() #Creating an instance of StringDataBaseClass
    strdtbs1.readFile() ## Reading the 4 letters word file.

    list_of_games = [] # This list will store all the game information

    # The code snippet `while (True):` creates an infinite loop. This means that the code inside the
    # loop will keep executing repeatedly until a certain condition is met to break out of the loop.
    while (True): # Once inside the loop, only way to get out is to quit
        current_word = strdtbs1.provide_a_random_word() #Find a random word from the 4 letters word.
        Guess.Guess_Class.main_screen(current_word , test_allowed , list_of_games) # Go to the main screen.
    