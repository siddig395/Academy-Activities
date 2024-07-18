# 1- Math Challenge

This repository contains a Python script that generates a math challenge for the user. The challenge consists of solving 100 math problems, and the script measures the time taken to complete all the problems.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Code Explanation](#code-explanation)

## Overview

The Math Challenge is a simple Python script that generates random math problems using basic arithmetic operators. The user is prompted to solve each problem, and the script keeps track of the number of incorrect attempts and the total time taken to complete the challenge.

## Features

- Generates random math problems with addition, subtraction, and multiplication.
- Measures the time taken to complete the challenge.
- Tracks the number of incorrect attempts.

## Code Explanation 

- imports
  import random: Used for generating random operands and selecting random operators.
  import time: Used for measuring the time taken to complete the challenge.
  
- Constant
OPERATORS = ["+", "-", "*"] : List of arithmetic operators used in the problems.
MIN_OPERAND = 0 : Minimum value for the operands.
MAX_OPERAND = 100 : Maximum value for the operands.
TOTAL_PROBLEM = 10 : Total number of problems in the challenge.

- Functions
  - generate_problem : Generates a random math problem. Randomly selects operands and operator. Returns the problem as a string (expr) and its evaluated answer (answer).
  - main code:
    - Initializes the count of incorrect attempts (wrong).
    - Prompts the user to start the challenge.
    - Records the start time.
    - Loops through the total number of problems, generating and prompting for each problem.
    - Checks the user's answer and increments the wrong count if incorrect.
    - Records the end time and calculates the total time taken.
    - Prints a completion message with the total time.



# 2- Story Game

This repository contains a Python script that generates a story by asking the user to provide words (Nouns, Adjectives, Adverbs) which are then inserted into predefined placeholders in the story.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Code Explanation](#code-explanation)

## Overview

The Story Game is a fun Python script that allows users to contribute to a story by providing words that fit into specified categories (nouns, adjectives, adverbs). These words are then incorporated into a predefined story template, creating a unique and personalized story.

## Features

- Prompts the user to input words of specific types (nouns, adjectives, adverbs).
- Incorporates user-provided words into a predefined story template.
- Displays the final story with the inserted words.

## Code Explanation

- Story Template: Reads the content of story.txt into a string variable story.
- Extracting Placeholders: Iterates through the story template to find placeholders marked by < and >. Adds each placeholder to a set words.
- Collecting User Inputs: Prompts the user to provide words for each placeholder. Stores the user inputs in a dictionary answers.
- Replacing Placeholders with User Inputs: Replaces each placeholder in the story template with the corresponding user-provided word. Prints the final story with the inserted words.

# 3- PIG (Dice Game)

This repository contains a Python script that implements a dice game where players take turns rolling a die. If a player rolls a 1, they lose their points for that turn. The first player to reach 100 points wins the game.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Code Explanation](#code-explanation)

## Overview

The Dice Game is a fun and simple Python script where multiple players can compete to reach 100 points first. Each player takes turns rolling a die, and if they roll a 1, they lose all points accumulated during that turn. Players can choose to end their turn voluntarily to add their turn's points to their total score.

## Features

- Allows 2 to 8 players to play.
- Players take turns rolling a die.
- If a player rolls a 1, they lose their points for that turn.
- First player to reach 100 points wins.

## Code Explanation 

- Imports and Roll Function:
  - random: Used to generate random numbers for die rolls.
  - roll(): Function that returns a random number between 1 and 18, simulating a die roll.
- Number of Players: Prompts the user to enter the number of players. Ensures the number of players is between 2 and 8.
- Game Setup:
  - max_score: The score required to win the game.
  - player_scores: A list initialized to keep track of each player's score.
- Game Loop:
  - Players take turns to roll the die.
  - If a player rolls a 1, they lose their points for that turn.
  - Players can choose to end their turn voluntarily.
- Determine Winner: Determines the player with the highest score once a player reaches 100 points. Announces the winner.


