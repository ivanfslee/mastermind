# Mastermind

[Mastermind](<https://en.wikipedia.org/wiki/Mastermind_(board_game)>) is a two player game where one player is the "codemaker" and the other player is the "codebreaker".

The codemaker creates a code composed of a sequence of four numbers, each number between zero and seven (inclusive). The codebreaker has 10 attempts to guess the code. After each attempt, feedback is given to the codebreaker showing how many numbers they have correct and how many numbers they have correct in the right location.

The game is over when the codebreaker guesses the codemaker's code correctly or when the codebreaker has made 10 failed guesses.

## Requirements

- Python >= 3.10

This software requires you have Python version 3.10 or newer installed.

I use f-strings and certain type hinting syntax that is only available starting from Python version 3.10.

## Installation

To install and run this project, follow these steps:

1. Clone the repository by running this command in your terminal:

```bash
git clone https://github.com/ivanfslee/mastermind.git
```

Alternatively, you can download the project files directly from github.

2. Navigate to the project directory:

```bash
cd /path/to/project/directory/mastermind
```

3. Run the `main.py` file, which will start the game in the terminal.

```bash
python main.py
```

The project does not use any additional third-party libraries.

## Game Structure

The game has 2 phases. The setup phase and the main game loop.

The setup phase prompts the user for certain information such as difficulty level, player name, opponent type (human or computer), and role type (codemaker or codebreaker).

**Setup phase**

1. Prompts the user for the difficulty level. The difficulty level is an integer that corresponds with the number of numbers the codebreaker will need to guess.

2. Prompts the user for their name.

3. Prompts the user for their intended role - codebreaker or code maker

 <div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/game_setup_1.png"
    alt="game setup prompts 1">
    <p>Diagram 1 - game setup prompts 1</p>
</div>

4. Prompts the user for their opponent type - human or computer

5A. If their opponent is human, it will prompt them for their opponent's name.

5B. If their opponent is the computer,

6. Prompts the human codemaker to create a code for the codebreaker to guess

**Main game loop**

7. Prompts the codebreaker to guess the codemaker's code

8. The codebreaker's guess is checked against the codemaker's code and feedback is generated and displayed to the codebreaker.

9. If the codebreaker's guess matches the codemaker's code, then the game is over. If the guess doesn't match the code and the codebreaker still has guesses left, then go back to step 7. Otherwise, if the codebreaker doesn't have any guesses left, then the game is over.

_Diagram 4_ below outlines the main game loop.

<div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/main_game_loop.png"
    alt="main game loop diagram">
    <p>Diagram 4 - main game loop</p>
</div>

## Code Structure

The entry point of the game starts in `main.py`, which will instantiate a CLI instance object, set up the game, instantiate a Game instance and run the `play` method, which starts up the main game loop.

The game code involves 4 different classes - `CLI`, `Player`, `Game`, `Feedback`.

The `CLI` class is involved in getting and validating user input and displaying messages and prompts to the user.

The `Game` class is responsible for storing any relevant state that the game will rely on as well as running the logic of the main game loop.

The `Player` class is responsible for instantiating player instances and storing their relevant details such as, name, role, and kind (i.e. human or computer).

The `Feedback` class is responsible for processing player guesses and determines how many numbers and locations that the guess contains.

The _Diagram 5_ below illustrates how the different classes interact with one another. The `CLI` class can be thought of as the top-most "visual" layer which the user will directly see and interact with. Anything below the CLI class makes up the non-visual layer and underlying logic of the game. The `CLI` class interfaces with the `Game` class. Because the `Game` class contains the core game logic, it can be thought of as the central hub that coordinates in turn with the other `Feedback` and `Player` classes.

<div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/class_structure.png"
    alt="Class structure diagram">
    <p>Diagram 5 - class structure</p>
</div>

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
