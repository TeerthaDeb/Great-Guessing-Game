import sys

import Guess
import StringDatabase

debug = False

if __name__ == "__main__":

    command_line_args = sys.argv[1:] #Store the commandline Arguments in 'command_line_args'
    if(debug):
        print("Command line arguments are ", command_line_args)

    # The code is checking if the string 'test' is present in the command line arguments. If it is,
    # then the variable `test_allowed` is set to `True` and the message "Test has been allowed" is
    # printed. Otherwise, `test_allowed` remains `False`.
    test_allowed = False
    if 'test' in command_line_args:
        test_allowed = True
        print("Test has been allowed")


    strdtbs1 = StringDatabase.StringDataBase()
    current_word = strdtbs1.readFile()
    Guess.Guess_Class.main_screen(current_word , test_allowed)
    