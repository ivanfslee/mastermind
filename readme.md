# Mastermind

[Mastermind](<https://en.wikipedia.org/wiki/Mastermind_(board_game)>) is a two player game where one player is the "Codemaker" and the other player is the "Codebreaker".

The Codemaker creates a code composed of a sequence of four numbers, each number between zero and seven (inclusive). The Codebreaker has 10 attempts to guess the code. After each attempt, feedback is given to the Codebreaker showing how many numbers they have correct and how many numbers they have correct in the right location.

The game is over when the Codebreaker guesses the Codemaker's code correctly or when the Codebreaker has made 10 failed guesses.

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

Alternatively, you can download the project files directly from github by clicking on the green "Code" button at the top of the page and selecting "Download ZIP".

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

The main game loop involves comparing the Codebreaker's guess against the Codemaker's code. If the guess matches the code, then the Codebreaker wins! If the guess doesn't match the code, feedback is given to the Codebreaker indicating how many numbers and locations they got correct. If the Codebreaker runs out of guesses without guessing the code correctly, then the game is over.

**Setup phase**

1. Prompt the user for the difficulty level. The difficulty level is an integer that corresponds to the number of numbers the Codebreaker will need to guess.

2. Prompt the user for their name.

3. Prompt the user for their intended role - Codebreaker or Codemaker.

_Diagram 1_ below outlines the initial questions prompted to the user.

<div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/game_setup_1.png"
    alt="game setup prompts 1">
    <p>Diagram 1 - game setup prompts 1</p>
</div>

If the user chooses to be the Codebreaker then:

4. Prompt the user for their opponent type - human or computer.

5A. If the opponent is a human, then prompt the human for their name.

5B. If the opponent is the computer, then a code is generated using the random.org API. Then go to step 7.

6. Prompt the human opponent to create a code for the Codebreaker to guess. Then go to step 7.

_Diagram 2_ below, outlines this portion of the game setup phase.

<div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/game_setup_2.png"
    alt="game setup prompts 2">
    <p>Diagram 2 - game setup prompts 2</p>
</div>

From step 3, if the user chooses to be the Codemaker then:

4. Prompt the user for their opponent type - human or computer.

5A. If the opponent is human, it will prompt them for their opponent's name.

5B. If the opponent is the computer, then prompt Player 1, the human Codemaker to create a code for the computer Codebreaker to guess. Then go to step 7.

6. Prompt Player 1, the human Codemaker to create a code for the human Codebreaker to guess. Then go to step 7.

_Diagram 3_ below, outlines this portion of the game setup phase.

<div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/game_setup_3.png"
    alt="game setup prompts 3">
    <p>Diagram 3 - game setup prompts 3</p>
</div>

**Main game loop**

7. Prompt the Codebreaker to guess the Codemaker's code

8. The Codebreaker's guess is checked against the Codemaker's code and feedback is generated and displayed to the Codebreaker.

9. If the Codebreaker's guess matches the Codemaker's code, then the game is over. If the guess doesn't match the code and the Codebreaker still has guesses left, then go back to step 7. Otherwise, if the Codebreaker doesn't have any guesses left, then the game is over.

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

_Diagram 5_ below illustrates how the different classes interact with one another. The `CLI` class can be thought of as the top-most "visual" layer which the user will directly see and interact with. Anything below the CLI class makes up the non-visual layer and underlying logic of the game. The `CLI` class interfaces with the `Game` class. Because the `Game` class contains the core game logic, it can be thought of as the central hub that coordinates in turn with the other `Feedback` and `Player` classes.

<div style="text-align: center;">
    <img
    src="https://github.com/ivanfslee/mastermind/raw/main/assets/class_structure.png"
    alt="Class structure diagram">
    <p>Diagram 5 - class structure</p>
</div>

The `utils` folder has various modules that contain helper functions used by the different classes. The `validate_input.py` module, contains helper functions that will validate user input. The `get_random_numbers.py` module contains a helper function that makes an HTTP request to the random.org API endpoint in order to generate random numbers.

The `assets` folder contains images used in the readme.md file.

The `tests` folder contains unit tests several modules.

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
