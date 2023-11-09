import os

debug = False

wrdlst = []
letters_guessed = ""
current_guessed = "----"

class Guess_Class:

    def quit_game():
        print("Goodbye!") ######### Write proper logic.
        exit()

    def guess_a_letter(current_word : str):
        """
            This Function asks user to enter an alphabet, checks the input for validity,
            upon valid input entry, the function checks the alphabet if it is in the word.
            If yes, then update current_guess with the letter.
            Funally it provides feedback.
        Args:
            current_word (str): The Current Word that we are guessing.
        """

        global letters_guessed 
        global current_guessed

        temp = input("\nEnter a letter: ")
        
        # The code block you provided is responsible for validating the user's input when they are
        # guessing a letter.
        while(len(temp) > 1):
            temp = input("Enter one letter only: ")
            while(temp in letters_guessed):
                print("You already checked for the letter: " + temp)
                temp = input("Enter another letter: ")

        check_if_there = False # flag that checks if entered letter is in the word, how many times it was into the word

        
        # The code block you provided is iterating over each character in the `current_word` string and
        # checking if it matches the `temp` letter that the user guessed.
        for i in range(0, len(current_word)):
            if (current_word[i] == temp.lower()):
                check_if_there += 1
                current_guessed = current_guessed[0 : i] +  temp + current_guessed[i+1 : ]
                
        print()

        # The code block you provided is checking if the guessed letter occurs multiple times in
        # the word. If it does, it prints a proper message.
        if(check_if_there > 1):
            print("@@")
            print("@@ Wow." , temp , "occurs multiple times in the word.")
            print("@@")

        # The block is responsible for providing feedback to the user when they
        # guess a letter that is actually in the word or not.
        elif(check_if_there):
            print("@@")
            print("@@ Wow." , temp , "is actually in the word.")
            print("@@")
            
        # The block you provided is responsible for providing feedback to the user when they guess a
        # letter that is not in the word.
        else:
            print("@@")
            print("@@ FEEDBACK: Try something else." , temp , "is not in the word.")
            print("@@")

        letters_guessed = letters_guessed + " " + temp ## update the 'letters_guessed' variable

        if(debug):
            print("From Debug:")
            print("\tletters_guessed = " , letters_guessed)
            print("\ttemp = " , temp)
            print("\tcurrent_word = " , current_word)
            print("\tcurrent_guessed = " , current_guessed)

        temp = input("\n\nPress any key to continue ... ")
        
    
    def guess_word(current_word : str):
        

    def main_screen(current_word : str , test_allowed:bool):
        """This function displays a welcome screen with options for users."""
        
        os.system("cls") # Clears the screen.

        print("++")
        print("++The great guessing game")
        print("++\n")

        
        
        global letters_guessed 
        global current_guessed
            

        if(test_allowed):
            print("Current Word:" ,current_word)

        #Main Menu:
        print("Current Guess:" ,current_guessed)
        print("Letters Guessed:" ,letters_guessed , "\n")
        print("g = guess , t = tell me, l for a letter, and q to quit")

        if(debug):
            print("From Debug:")
            print("\tletters_guessed = " , letters_guessed)
            print("\tcurrent_word = " , current_word)
            print("\tcurrent_guessed = " , current_guessed)

        # This code is prompting the user to enter an option from the main menu. It checks
        # the validity of the input.
        # If the input is invalid, it prompts the user to re-enter the option until a valid option
        # is provided.
        # And if it is a valid entry, proceed next.
        choice_from_main_menu = input("\nEnter Option: ")
        while len(choice_from_main_menu) > 1 or not choice_from_main_menu in ['g' , 't' , 'l' , 'q']:
            choice_from_main_menu = input("Invalid option. Please re-enter: ")
        
        if choice_from_main_menu == 'q':
            Guess_Class.quit_game()
        
        elif choice_from_main_menu == 'l':
            Guess_Class.guess_a_letter(current_word)

        while '-' in current_guessed:
            Guess_Class.main_screen(current_word , test_allowed)