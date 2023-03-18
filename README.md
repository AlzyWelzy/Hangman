# Hangman Game

Hangman is a classic word-guessing game where the player has to guess a secret word by guessing one letter at a time. For each incorrect guess, a part of the "hangman" is drawn, and the player loses when the hangman is complete. This Python implementation of the game uses the Pygame library to create a graphical version of the game.

## Getting Started

To get started with the Hangman game, you'll need to install the Pygame library. You can do this using pip:

```bash
pip install pygame
```


Once you have Pygame installed, you can clone or download the repository and run the `hangman.py` file to start the game.

## How to Play

When you start the game, you'll see a screen with a blank space for each letter in the secret word. You can start guessing letters by pressing keys on your keyboard. If the letter is in the word, it will be revealed in the blank spaces. If the letter is not in the word, a part of the hangman will be drawn on the screen. You can keep guessing letters until you either guess the word correctly or the hangman is complete.

The game ends when you either win or lose. If you win, you'll see a congratulatory message and the option to play again. If you lose, you'll see a message with the secret word and the option to play again.

## Game Features

The Hangman game in this repository has the following features:

- A list of over 1,000 secret words to choose from
- A graphical interface using Pygame
- A list of hangman graphics that are displayed as incorrect guesses are made
- The ability to play again after winning or losing

## Code Structure

The code for the Hangman game is structured as follows:

- `hangman.py`: The main file that runs the game loop and handles user input.
- `words.txt`: A text file containing a list of words to choose from.
- `assets/`: A directory containing the hangman graphics that are displayed during the game.
<!-- - `util.py`: A module containing utility functions used in the game logic. -->

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome, including bug fixes, new features, or improvements to the existing code.

## License

This project is licensed under the GNU Affero General Public License (AGPL) version 3 - see the [LICENSE](LICENSE) file for details.
