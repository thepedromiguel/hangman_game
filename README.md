# Hangman Game

## 29/12/2022 - 07/01/2023 

I decided to create a multiplayer of Hangman that is playable, as well as simulated.
The difference is that, in the playable version, the players can guess the letters, while in the simulated version, the letters are guessed automatically.

Due to the way I coded the game, using a function instead of a class, the hangman.py file only has a single line, which executes the function.
When launching the game, the user can either insert 'p' to play the game or 's' to simulate it.
Afterwards, the user can select the number of players (from 1 to 7), the word length and the name of the players.
If the playable version is selected, the players will then guessed a letter (or a word) on their turn.
The game ends when one of the players completes the word, or there are no lives left, and the output will be saved to hangmanGame.txt.


The first 16 lines of hangmanClass.py include imported libraries, and sets, lists, tuples or dictionaries created. Most of the lines are commented, so I
	won't write it again to keep the briefing short. I'll just explained the most relevant sections.

Lines 29-66 contain three different while loops with indented try and except blocks. I used them so that, if the input inserted by the user is invalid, the 
	game doesn't break and they are able to insert a new input.

The function in lines 80-83 detects the length of the words. I discovered that the list has words from 1 to 31 letters. However, there are no words with 26 or
	30 letters.

Lines 85-89 separate the letters of the secret word and replaced them with underscores for the start of the game. I spent quite some time in this part, even 
	using Google to help me. 

I also googled lines 94-99, since I couldn't store the players' information. I got a persistent error where every player was number 1.

I used similar lines to lines 103-104 throughout the project to write the output to hangmanGame.txt. I spent some hours trying to find a way to export the
	output to a .txt file, but the only feasible solutions involved using a terminal. Therefore, I decided to export only the most relevant information.

Instead of having the players playing in order, I decided to randomise the order (lines 114-130) to make the game fairer. Since the numbers are randomly 
	generated, I created an empty list that will append the number of the players that have played, so that no players play multiple times in a row by 
	chance. Once the list gets full, it is reset. It also took me some time to make the random functions work correctly.

Lines 167-246 contain a while loop that contains constrains for all the possible inputs.
Lines 170-177 (if-statement) generate a random letter if the game is simulated. Since the computer seems to be really bad at playing hangman, I googled the
	letters relative frequency in English dictionaries (https://en.wikipedia.org/wiki/Letter_frequency) and how to create a random function using probabilities.
	The computer hasn't guessed any word in any of the trials, but the number of correct letters increased significantly.
The if-statement in lines 185-222 address all inputs of length 1. There are 5 possible outcomes. If the player has already guessed that letter incorrectly, they
	will be alerted and won't lose any lives. The same if the player has already guessed that letter correctly, or if if they inserted an invalid character.
	If they guess a new correct letter, its position will be revealed. If they guess a new incorrect letter, it will be added to the incorrect guesses list, and
	they will lose a life.
If the game is not simulated, the players also have the opportunity to guess the secret word, instead of just a letter. If they guess the correct word, they win the
	game. If the guess is incorrect and has the same length as the secret word, they lose a life. Else, they will be alerted that the guess has a different length,
	or is simply invalid, and they won't lose any lives.

The last line (257) was inserted so that, when running the game on Python, it won't close automatically after somebody wins, or they run out of lives. If the user 
	still exits the game by mistake, they can see the output on hangmanGame.txt.


I started by creating a playable game, but then I realised that the goal of the task was to run a simulation. I had already wrote 100 lines of code; so , instead of
	starting from the beginning, I decided to finish the code, and then add some random functions so that it could run automatically. I also had some problems 
	trying to develop the whole game using class. Thus, I only used classes to store the name and number of each player, and instead use a function to execute the
	game. 
Overall, it was a great experience, and an amazing opportunity to practice what I have learnt during the previous 10 weeks.
