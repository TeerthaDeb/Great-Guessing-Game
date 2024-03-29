# The `StringDataBase` class reads a file named "four_letters.txt", filters out all the words that are
# not 4 letters long, and provides a random word from the filtered list.

import random

wordlst = []
debug = False

class StringDataBase:
    def readFile(self):

        """
            The function `readFile()` reads a file named "four_letters.txt" and filters out all the words
            that are not 4 letters long, storing the 4-letter words in the `wordlst` list.
        """
        global wordlst

        # The code is trying to open a file named "four_letters.txt" in read mode using the `open()`
        # function. If the file is successfully opened, it reads the contents of the file using the
        # `read()` method and splits the contents into a list of words using the `split()` method.
        try:
            '''
                The code is trying to open a file named "four_letters.txt" in read mode using the `open()`
                function. If the file is successfully opened, it reads the contents of the file using the
                `read()` method and splits the contents into a list of words using the `split()` method.
            '''
            with open("four_letters.txt", "r") as file:
                lines = file.read().split()
                while lines:
                    # The code is iterating over each word in the `lines` list and checking if the length
                    # of the word is equal to 4. If it is, the word is appended to the `wordlst` list.
                    # This code is essentially filtering out all the words that are not 4 letters long and
                    # storing the 4-letter words in the `wordlst` list.
                    for word in lines:
                        if len(word) == 4:
                            wordlst.append(word)
                            # After processing one line (i.e., after reading a set of four letter words), we remove
                    lines = file.read().split()

            file.close() ## close the file.

        except FileNotFoundError as e:
            '''
                If an error occurs while opening or reading from the file (e.g., the file does not exist),
                And quit.
            '''
            print("The file is not there. Please place the file into the same folder and run the program again to continue.")
            return

        except Exception as e:
            '''
                If any other type of exception occurs during this process, such as an IOError or OSError,
            '''
            print("Though the file was opened " , e , "Occured")
        
        if(debug):
            print("The word list is: ")
            print(wordlst)
            input("press any key to move further")
        
    
    def provide_a_random_word(self) -> str:
        global wordlst
        """The function `provide_a_random_word` returns a random word from a global list called `wordlst`.

        Returns:
            str: a randomly selected word from the `wordlst` list.
        """
        s = wordlst[random.randint(0 , len(wordlst))] #Select a Random Word from the list
        if(debug):
            print("Randomly selected word : ",s)
            input("press any key to continue")
        return s