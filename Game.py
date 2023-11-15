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
    letters_guessed = 0
    words_guessed = 0
    actual_word = ""

    def __init__(self , word: str) -> int:
        
        self.actual_word = word
        
        for i in word:
            self.score += letter_frequency[i]

        return self.score
    
    def wordGuessed(self , word_guessed_by_user : str):
        if self.actual_word != word_guessed_by_user:
            self.score -= self.score * 10/100 ##decrease 10% score

    def letterGuessed(self , letter_user_guessed : chr):
        
        if letter_user_guessed not in self.actual_word: ## decrease score by 25%
            self.score -= 25/100 * (letter_frequency[letter_user_guessed] / 2)
        
        else: #decrease score by 13%
            self.score -= 13/100 * (letter_frequency[letter_user_guessed] / 2)

    def printScore(self):
        print(self.score)



if __name__ == "__main__":
    game = Game_Class('ohed')
    game.wordGuessed("ohed" , "ohad")
    game.printScore()