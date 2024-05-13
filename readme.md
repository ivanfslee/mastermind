# Mastermind

[Mastermind](<https://en.wikipedia.org/wiki/Mastermind_(board_game)>) is a two player game where one player is the "codemaker" and the other player is the "codebreaker".

The codemaker creates a code composed of a sequence of four numbers, each number between zero and seven (inclusive). The codebreaker has 10 attempts to guess the code. After each attempt, feedback is given to the codebreaker showing how many numbers they have correct and how many numbers they have correct in the right location.

The game is over when the codebreaker guesses the codemaker's code correctly or when the codebreaker has made 10 failed guesses.

## Requirements

- Python >= 3.10

This software requires you have Python version 3.10 or newer installed.

I use f-strings and certain type hinting syntax that is only available starting from Python version 3.10.

## Installation

1. `git clone` the repo or download the code

2. `cd` into the project directory

3. Run the `main.py` file by running the command `python main.py` in your command line.

## Code Structure

The entry point of the game starts in `main.py`, which will instantiate a CLI instance object, set up the game, instantiate a Game instance and run the `play` method, which starts up the main game loop.

The game code involves 4 different classes - `CLI`, `Player`, `Game`, `Feedback`.

The `CLI` class is involved in getting and validating user input and displaying messages and prompts to the user.

The `Game` class is responsible for storing any relevant state that the game will rely on as well as running the logic of the main game loop.

The `Player` class is responsible for instantiating player instances and storing their relevant details such as, name, role, and kind (i.e. human or computer).

The `Feedback` class is responsible for processing player guesses and determines how many numbers and locations that the guess contains.

The diagram below illustrates how the different classes interact with one another. The `CLI` class can be thought of as the top-most "visual" layer which the user will directly see and interact with. Anything below the CLI class makes up the non-visual layer and underlying logic of the game. The `CLI` class interfaces with the `Game` class. Because the `Game` class contains the core game logic, it can be thought of as the central hub that coordinates in turn with the other `Feedback` and `Player` classes.

![Code Structure](/assets/code_structure.png)

The `utils` folder has various modules that contain helper functions used by the different classes. The `validate_input.py` module, contains helper functions that will validate user input. The `get_random_numbers.py` module contains a helper function that makes an HTTP request to the random.org API endpoint in order to generate random numbers.

## Extensions

From the base requirements in the PDF that was given to me, I extended the game to include other features such as:

- Adding the functionality to allow the player to configure the "difficulty level" of the game. The difficulty level corresponds to the amount of numbers the codebreaker will need to guess. e.g. a difficulty level of 7 means the codebreaker will need to guess a sequence of 7 numbers.

- Adding the functionality to allow the human player to be the codemaker and the computer to be the codebreaker.

- Adding the functionality to allow two human players to play each other on the same machine. One human will be the codemaker and the other will be the codebreaker.

## Known Issues

**Problem:**
SSL certificate issue on MacOS

You may get the following urlopen error when making a request to the random.org API

`<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1006)>`

**Solution:**
A solution is to update the SSL certificate directory on MacOS.

- Press "command + space" button or open Spotlight
- type "Install Certificates.command"

This will update your local SSL certificates and resolve the issue.

See this [link](https://support.chainstack.com/hc/en-us/articles/9117198436249-Common-SSL-Issues-on-Python-and-How-to-Fix-it) for more information.
