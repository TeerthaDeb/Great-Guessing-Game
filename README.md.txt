# Word Guessing Game

This Python project implements a word guessing game where users try to guess a randomly selected four-letter word. The game is structured with multiple files, each serving a specific purpose.

## Files

1. **Game.py**: Defines the `Game_Class` that represents a word guessing game. It tracks the score, guesses, and status of the game. The class contains methods for handling good and bad guesses, as well as updating the game status.

2. **Guess.py**: Contains the `Guess_Class`, a class with static methods for handling user input and game logic in the guessing game. It provides options for guessing letters, guessing the entire word, giving up, and quitting the game.

3. **StringDatabase.py**: Defines the `StringDataBase` class responsible for reading a file named "four_letters.txt," filtering out all non-four-letter words, and providing a random word from the filtered list.

4. **Words.py**: The main script of the program. It handles command-line arguments, initializes the game, and enters an infinite loop where users can play the game. The loop continues until the user chooses to quit.

## How to Run

To run the program, execute the `Words.py` script from the command line. If you want to enable test functionality, include the 'test' argument. By default, the program runs in play mode.

```bash
python Words.py [test]
```

or 

```bash
python Words.py
```
# Gameplay

- The game randomly selects a four-letter word from a predefined list.
- Users can guess letters or the entire word.
- Feedback is provided for correct and incorrect guesses.
- Users can give up to see the correct word.
- The game continues until the user decides to quit.

# Features

- **Score Tracking**: The game keeps track of the score, good and bad guesses, and overall status.
- **Word Database**: The program reads a file to obtain a database of four-letter words for the game.
- **User Interaction**: Users interact with the game through a simple command-line interface.

# Notes

- The program supports a test mode, allowing certain functionalities to be enabled.
- Users can quit the game at any time and view a final score report.

# Author
Maharaj Teertha Deb