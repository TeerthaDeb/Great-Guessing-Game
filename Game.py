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
    
    score = 0
    good_letter_guess = 0
    bad_letter_guess = 0
    actual_word = ""
    good_guess = 0
    bad_guess = 0
    status = ""

    def __init__(self , word: str) -> int:
        
        self.actual_word = word

        self.score = 30 ##The maximum possible score
        
        for i in word:
            self.score -= letter_frequency[i] * 2 / 10  ## Decrease the maximum scoring possiblity by the letter_frequency. So that there are equal distribution of scores for all the words.
    
    ##getters:

    def get_good_guess(self):
        return self.good_guess
    
    def get_bad_guess(self):
        return self.bad_guess
    
    def get_good_letter_guess(self):
        return self.good_letter_guess
    
    def get_bad_letter_guess(self):
        return self.bad_letter_guess
    
    def get_score(self):
        ##must modify the score before returning
        return self.score
    
    def get_actual_word(self):
        return self.actual_word
    
    def get_status(self):
        return self.status
    
    ##setters:
    def made_good_guess(self):
        self.status = "Success"
        self.good_guess += 1
        return self.get_good_guess()
    
    def made_bad_guess(self):
        self.bad_guess += 1
        return self.get_bad_guess()
    
    def made_good_letter_guess(self):
        self.good_letter_guess += 1
        if self.good_letter_guess == 4:
            self.status = "Success"
        return self.get_good_letter_guess()
    
    def made_bad_letter_guess(self):
        self.bad_letter_guess += 1
        return self.get_bad_letter_guess()

    def user_gave_up(self):
        #add something here
        self.status = "Gave up"
        return self.get_score()

    def printScore(self):
        scr = self.get_score()
        print(scr)
        return
    
    def print_score_borard(gameList : list):
        os.system("cls") # clears the screen
        print("++")
        print("++ Game Report")
        print("++\n")
        final_score = 0
        print("Game\t\tWord\t\tStatus\t\tBad Guesses\tMissed Letters\t\tScore")
        print("----\t\t----\t\t------\t\t-----------\t--------------\t\t-----")
        for i in range(len(gameList)):
            print(f'{i+1 : <4d}\t\t{gameList[i].get_actual_word() : <4s}\t\t{gameList[i].get_status() : <6s}\t\t{gameList[i].get_bad_guess() : <7d}\t\t{gameList[i].get_bad_letter_guess(): <13d}\t\t{gameList[i].get_score() : <5.2f}')
            final_score += gameList[i].score

        print("\n\nFinal Score:" , final_score)