# The `Guess_Class` is a class that contains static methods for handling user input and game logic in
# a guessing game.


import os
import Game

debug = False

wrdlst = []
letters_guessed = []
current_guessed = "----"

class Guess_Class:

    @staticmethod
    def quit_game(list_of_games : list):
        """
            The `quit_game` function prints the score board for a list of games and exits the program.
            
        Args:
            list_of_games(list): The parameter `list_of_games` is a list that contains instances of the
            `Game` class
        """
        Game.Game_Class.print_score_board(list_of_games)
        exit() ## the final way to exit the game

    @staticmethod
    def guess_a_letter(current_word : str , g1 : Game.Game_Class):
        """
            This Function asks user to enter an alphabet, checks the input for validity,
            upon valid input entry, the function checks the alphabet if it is in the word.
            If yes, then update current_guess with the letter.
            Funally it provides feedback.
        Args:
            current_word (str): The Current Word that we are guessing.
            g1 (Game.Game_Class): An instance of the game class.
        """

        global letters_guessed #Load the letters that have been guessed
        global current_guessed #Load the current guessed words

        temp = input("\nEnter a letter: ") # Users are asked to enter a letter.
        
        # The code block you provided is responsible for validating the user's input when they are
        # guessing a letter.
        while(len(temp) > 1 or temp in letters_guessed):

            if(len(temp) > 1): # if user enters more than 1 letter
                temp = input("Enter one letter only: ")

            else:   #if the letter has already been checked.
                print("You already checked for the letter: " + temp)
                temp = input("Enter another letter: ")

        check_if_there = False # flag that checks if entered letter is in the word, how many times it was into the word

        
        # The code block you provided is iterating over each character in the `current_word` string and
        # checking if it matches the `temp` letter that the user guessed.
        for i in range(0, len(current_word)):
            if (current_word[i] == temp.lower()):
                check_if_there += 1
                current_guessed = current_guessed[0 : i] +  temp + current_guessed[i+1 : ] #update the current guessed variables
                
        print() # print a newline

        # The code block you provided is checking if the guessed letter occurs multiple times in
        # the word. If it does, it prints a proper message.
        if(check_if_there > 1):
            print("@@")
            print("@@ Wow." , temp , "occurs multiple times in the word.")
            print("@@")
            g1.made_good_letter_guess()
            g1.made_good_letter_guess() # call it two times, because two letters are guessed already

        # The block is responsible for providing feedback to the user when they
        # guess a letter that is actually in the word or not.
        elif(check_if_there):
            print("@@")
            print("@@ Wow." , temp , "is actually in the word.")
            print("@@")
            g1.made_good_letter_guess()
            
        # The block you provided is responsible for providing feedback to the user when they guess a
        # letter that is not in the word.
        else:
            print("@@")
            print("@@ FEEDBACK: Try something else." , temp , "is not in the word.")
            print("@@")
            g1.made_bad_letter_guess()

        letters_guessed.append(temp) # store the letters that have been guessed.

        if(debug):
            print("From Debug:")
            print("\tletters_guessed = " , letters_guessed)
            print("\ttemp = " , temp)
            print("\tcurrent_word = " , current_word)
            print("\tcurrent_guessed = " , current_guessed)

        input("\n\nPress any key to continue ... ") #Pause the screen before cleaning up.
        
    @staticmethod
    def guess_word(current_word : str , g1 : Game.Game_Class) -> bool:
        """_summary_
            The function `guess_word` takes a current word as input and prompts the user to guess the word,
            providing feedback and returning True if the guess is correct, and False otherwise.
        
        Args:
            current_word (str): The current_word parameter is a string that represents the word that the
                                user needs to guess
            g1 (Game.Game_Class): This parameter is an instance of the class Game_Class which contains 
                                    all the game information and has been passed as reference.


        Returns:
            bool:   The function `guess_word` returns a boolean value. It returns `True` if the user's
                    guessed word matches the current word (ignoring case), indicating that the guess was correct. It
                    returns `False` if the guessed word does not match the current word, indicating that the guess
                    was incorrect.
        """
        
        
        guessed_word = input("\nMake your guess: ") ## ask user input

        # The code is checking if the guessed word is equal to the current word(ignoring case).
        # If it is, it means the user has made a correct guess and the function
        # returns True. It also provides feedback to the user by printing a message.
        if guessed_word == current_word.lower():
            print("\n@@")
            print("@@ FEEDBACK: Your're Cool. you made a correct guess!")
            print("@@")
            g1.made_good_guess()
            input("\n\nPress any key to continue ... ") # Pause the screen before clearing
            return True
        
        # The `else` block is executed when the user's guessed word does not match the current word.
        # It provides feedback to the user by printing a message 
        # and prompts the user to press any key to continue. 
        # Finally, it returns `False` to
        # indicate that the user's guess was incorrect.
        else:
            print("\n@@")
            print("@@ FEEDBACK: Can't even guess a word ? Try again...")
            print("@@")
            g1.made_bad_guess()
            input("\n\nPress any key to continue ... ")
            return False
        
    @staticmethod
    def user_gave_up(current_word: str , g1 : Game.Game_Class):
        """
        When user gives up, show them what was the word.
        Args:
            current_word (str): The current_word parameter is a string that represents the word that the
                                user needs to guess
            g1 (Game.Game_Class): This parameter is an instance of the class Game_Class which contains 
                                    all the game information and has been passed as reference.

        """
        print("\n@@")
        print("@@ FEEDBACK: You gave up !!! You could easily guessed this... '" + current_word + "'")
        print("@@")
        g1.user_gave_up() ## Update the game status
        
        input("\n\nPress any key to continue ... ") # pause the screen until user presses enter


    @staticmethod
    def main_screen(current_word : str , test_allowed:bool , list_of_games:list):
        """
        __summary__:    This function displays a welcome screen with options for users.

        Args:
                current_word (str) : The word that user trying to guess.
                test_allowed (bool) : A boolean value indicating whether test is allowed or not.
                list_of_games (list) : List containing all games played so far.
        """

        g1 = Game.Game_Class(current_word) ## making an instance of the Game Class to hold each games data
        global letters_guessed 
        global current_guessed

        while '-' in current_guessed:        # While the letter was guessed properly.

            os.system("cls") # Clears the screen.

            print("++")
            print("++The great guessing game")
            print("++\n")

            if(test_allowed): #if test is allowed , display the word
                print("Current Word:" ,current_word)

            #Main Menu:
            print("Current Guess:" ,current_guessed)
            print("Letters Guessed:" , end = " ")

            for i in letters_guessed: # Print the letters that has been guessed so far.
                print(i , end = " ")

            print("\n\ng = guess , t = tell me, l for a letter, and q to quit") # The options

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
            
            
            if choice_from_main_menu == 'q':            #Checking whether wants to quit or not. if they do, they will be redirected to the score board.
                #This is the only way to exit the game.
                Guess_Class.quit_game(list_of_games)
            
            elif choice_from_main_menu == 'l': # Checking user wants toguess a letter.
                Guess_Class.guess_a_letter(current_word , g1)

            elif choice_from_main_menu == 'g':  #if user wants to guess the whole word. 
                if(Guess_Class.guess_word(current_word , g1)):
                    current_guessed = current_word #If user guessed the word correctly, store the word in currenct_guess.

            elif choice_from_main_menu == 't': # If user wants to give up and see the current word.
                Guess_Class.user_gave_up(current_word , g1)
                break   #break the  while loop.
            
        
        list_of_games.append(g1)   # append the current game status to the list.
        del g1 # delete g1 as it will be defined in the next game(If user wants to play.)
        # Reset current_guessed and letter_guessed (list) for next use.
        current_guessed = "----" 
        letters_guessed = [] 