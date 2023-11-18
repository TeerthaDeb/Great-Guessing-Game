# The module defines a class called Game_Class that represents a word guessing game and keeps
# track of the score, guesses, and status of the game.

import os
### letter_frequency comes from A2 Assignment instruction itself.
letter_frequency = {
    'a': 8.17,
    'b': 1.49,
    'c': 2.78,
    'd': 4.25,
    'e': 12.70,
    'f': 2.23,
    'g': 2.02,
    'h': 6.09,
    'i': 6.97,
    'j': 0.15,
    'k': 0.77,
    'l': 4.03,
    'm': 2.41,
    'n': 6.75,
    'o': 7.51,
    'p': 1.93,
    'q': 0.10,
    'r': 5.99,
    's': 6.33,
    't': 9.06,
    'u': 2.76,
    'v': 0.98,
    'w': 2.36,
    'x': 0.15,
    'y': 1.97,
    'z': 0.07
}



class Game_Class:
    
    initial_score = 0
    score = 0
    good_letter_guess = 0
    bad_letter_guess = 0
    actual_word = ""
    good_guess = 0
    bad_guess = 0
    status = ""

    def __init__(self , word: str):
        """
        __Summary__:
            The function initializes an object with a given word and calculates the maximum possible score
            for that word based on the frequency of its letters.
        
        Args:
            word (str): The `word` parameter is a string that represents the word for which the scoring is
                        being calculated
        """
        
        self.actual_word = word

        self.score = 30 ##The maximum possible score
        
        for i in word:
            self.score -= letter_frequency[i] * 2 / 10  ## Decrease the maximum scoring possiblity by the letter_frequency. So that there are equal distribution of scores for all the words.

        self.initial_score = self.score ## store the initial store.
        
    ##getters:

    def get_good_guess(self)  -> int:
        """
        The function returns the value of the "good_guess" attribute.
        Return (int): The method is returning the value of the attribute "good_guess".
        """
        return self.good_guess
    
    def get_bad_guess(self) -> int:
        """
        The function returns the value of the "bad_guess" attribute.
        Return(int): The method is returning the value of the attribute "bad_guess".
        """
        return self.bad_guess
    
    def get_good_letter_guess(self) -> int:
        """
        The function returns the number of good letter guesses.
        Return(int) : The method is returning the value of the attribute "good_letter_guess".
        """
        return self.good_letter_guess
    
    def get_bad_letter_guess(self) -> int:
        """
        The function returns the number of bad letter guesses.
        Return (int) : The method is returning the value of the variable "self.bad_letter_guess".
        """
        return self.bad_letter_guess
    
    def get_score(self) -> int:
        """
        The function returns the score after modifying it.
        Return(int): The method is returning the value of the "score" attribute of the object.
        """
        self.score *= self.good_letter_guess / (self.good_letter_guess + self.bad_letter_guess) # the logic to decrease the score.
        return self.score
    
    def get_actual_word(self) -> str:
        """
        The function `get_actual_word` returns the actual word stored in the object.
        Return(str): The method is returning the value of the variable "actual_word".
        """
        return self.actual_word
    
    def get_status(self) -> str:
        """
        The function returns the status of an object.
        Return(str): The status of the object.
        """
        return self.status
    
    ##setters:
    def made_good_guess(self) -> int:
        """
        The function increments the "good_guess" attribute by 1 and returns its current value.
        Return(int): The method `made_good_guess` is returning the value of `self.get_good_guess()`.
        """
        self.status = "Success"
        self.good_guess += 1
        return self.get_good_guess()
    
    def made_bad_guess(self) -> int:
        """
        The function `made_bad_guess` increments the `bad_guess` counter, decreases the `score` by 10%
        of the initial score, and returns the updated `bad_guess` value.
        Return(str): The method `made_bad_guess` returns the number of bad guesses made, which is obtained
        by calling the `get_bad_guess` method.
        """
        self.bad_guess += 1
        self.score -= self.initial_score * 10 / 100 ## if making a bad guess, decrease 10%
        return self.get_bad_guess()
    
    def made_good_letter_guess(self) -> int:
        """
        The function increments the count of good letter guesses and checks if the count is equal to 4,
        in which case it updates the status to "Success" and returns the count of good letter guesses.
        Return(int): The method is returning the value of `self.get_good_letter_guess()`.
        """
        self.good_letter_guess += 1
        if self.good_letter_guess == 4:
            self.status = "Success"
        return self.get_good_letter_guess()
    
    def made_bad_letter_guess(self) -> int:
        """
        The function increments the count of bad letter guesses and returns the updated count.
        Return(int): The method is returning the value of the variable `self.bad_letter_guess`.
        """
        self.bad_letter_guess += 1
        return self.get_bad_letter_guess()

    def user_gave_up(self) -> int:
        """
        The function "user_gave_up" updates the score and status of a user who gave up.
        Return(int): the score as a string.
        """
        self.score -= self.initial_score
        self.status = "Gave up"
        return self.get_score()
    
    @staticmethod
    def print_score_board(gameList: list):
        """
        The function `print_score_board` takes a list of game objects and prints a formatted score board
        with information about each game and the final score.

        Args:
            gameList(list): The `gameList` parameter is a list of objects representing different games.
            Each object in the list should have the following methods:
        """
        os.system("cls")  # clears the screen
        print("++")
        print("++ Game Report")
        print("++\n")
        final_score = 0
        print("Game\t\tWord\t\tStatus\t\tBad Guesses\tMissed Letters\t\tScore")
        print("----\t\t----\t\t------\t\t-----------\t--------------\t\t-----")
        for i in range(len(gameList)):
            print(f'{i+1 : <4d}\t\t{gameList[i].get_actual_word() : <4s}\t\t{gameList[i].get_status() : <6s}\t\t{gameList[i].get_bad_guess() : <7d}\t\t{gameList[i].get_bad_letter_guess(): <13d}\t\t{gameList[i].get_score() : <5.2f}')
            final_score += gameList[i].score

        print(f"\n\nFinal Score: {final_score:.2f}")
        print("\n")
        print("@@Thenk you for trying our program.")
        print("\n\n\n\n")
