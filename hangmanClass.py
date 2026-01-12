# A Practical Introduction to Python Programming #
# Hangman - My Project #
# 38139596 #
# 29/12/2022 - 07/01/2023 #

import random
import pickle
import re
import string

playerID = {}
correctSize = []
lettersFound = []
correctGuesses = []
incorrectGuesses = []
lengthsAvailable = set()

class hangmanPlayer: # Creates hangman player
    def __init__(self, firstName, number):
        self.firstName = firstName # Stores the name of the player
        self.number = number # Stores the number of the player
    def welcome(self):
        print("Hello " + self.firstName + " (Player " + str(self.number) + ")!") # Prints welcome message
    def yourTurn(self):
        print("It's your turn " + self.firstName + " (Player " + str(self.number) + ").") # Shows who is the player that goes next
    def victoryMessage(self):
        print("Congratulations " + self.firstName + " (Player " + str(self.number) + "), you have just won.") # Prints victory message

while True:
    try:
        simulation = input("Would you like to play or run a simulation of hangman?\n[Please insert 'p' to play or 's' to run a simulation.]\n")
        # Decide wether to play or run a simulation of the game
        if simulation == 'p':
            print("You are now going to play Hangman.")
            break
        elif simulation == 's':
            print("A simulation of Hangman will now be run.")
            break
        else:
            print("Option not valid.")
    except:
        print("Option not valid.")

while True:
    try:
        players = int(input("Please insert the number of players:\n[Please insert a value from 1 to 7.]\n")) 
        # Displays a message asking to insert number of players
        if players <= 7 and players > 0:
            break
        else:
            print("This game is for 1 to 7 players only. Please insert new value.")
    except:
        print("That is not an integer. Please insert new value from 1 to 7.")

while True:
    try:
        wordLength = int(input("Please select the word lenght:\n[Please insert a value from 1 to 31, except 26 or 30.]\n"))
        # Displays a message asking to select the word lenght
        if wordLength == 26 or wordLength == 30:
           print("There are no words with 26 or 30 letters on the list. Please insert new value between 1 and 31, except 26 or 30.") 
        elif wordLength <= 31 and wordLength > 0:
            break
        else:
            print("The length of the word should be between 1 and 31, except 26 or 30. Please insert new value.")
    except:
        print("That is not an integer. Please insert new value between 1 and 31, except 26 or 30.")

with open ("words.txt", "r") as allWords:
    myWords = allWords.read() # Opens words.txt
    
noLines = myWords.replace("\n", " ").lower()
words = noLines.split(" ") # Creates a list with all the words in the file

for eachword in words: # Creates a smaller list, with only the words of the selected size
    if len(eachword) == wordLength:
        correctSize.append(eachword)
    else:
        pass
    
def lengthOfWord(wordList): # This function was created to find out the possible lengths of the words
    for word in wordList:
        lengthsAvailable.add(len(word))
lengthOfWord(words)

secretWord = random.choice(correctSize) # Generates the word that the players are trying to guess
secretLetters = list(secretWord) # Creates a list with all the letters of the word
lettersIndex = dict(enumerate(secretLetters)) # Creates a dictionary with the index of the letters of the word
underlinedWord, n = re.subn("[a-z]", "_", secretWord) # Hides all the letters of the word
underlinedLetters = list(underlinedWord) # Creates a list with the letters of the word hidden    

with open("hangmanStates.pkl", "rb") as pickleRead: # Imports the hangman states
    hangmanPickle = pickle.load(pickleRead)

for x in range(1, players + 1): # Allows players to pick their name
    global individual
    individual = input("Please insert your name:\n")
    insertPlayer = hangmanPlayer(individual, x)
    insertPlayer.welcome() # Show individual player welcome message
    playerID[x] = individual # Saves ID to dictionary

print("Your game has been generated and it's ready to go!\nThe output of the game will be loaded to hangmanGame.txt afterwards.\n")
# Prints message saying the game is ready to play or to be simulated
with open("hangmanGame.txt","a") as hangmanGame: # Writes message to hangmanGame.txt file
    hangmanGame.write("Your game has been generated and it's ready to go!\n")

def hangman(): # This is the function that will run the game
    randomList = []
    for y in range(25): # There are 26 words in the alphabet
        if y == 0:
            z = y # y is the number of trials, z is (6 - number of guesses left)
        else:
            pass
        
        for i in range(100): # the order of the players will be randomly generated, so no player has any advantage
            a = random.randint(1, players)
            if len(randomList) == 0: # random list with all the players (it starts empty)
                randomList = list(range(1, players + 1)) # if the list is empty, add all players
                randomList.remove(a) # if a player is selected, it is removed from the list until all players have played once in that round
                turn = a
                break
            else:
                if a in randomList: #ammend loop
                    randomList.remove(a)
                    turn = a
                    break
                else:
                    continue
        currentPlayer = playerID[turn]
        current = hangmanPlayer(currentPlayer, turn)
        current.yourTurn() # Shows who is the player that goes next
        
        print(hangmanPickle[z]) # Prints hangman state
        with open("hangmanGame.txt","a") as hangmanGame: # Writes hangman state to hangmanGame.txt
            hangmanGame.write(hangmanPickle[z])
            hangmanGame.write("\n")
        
        if y == 0:
            currentWord = underlinedWord # The game starts with all letters hidden
            lettersFound = underlinedLetters
            print(currentWord)
            with open("hangmanGame.txt","a") as hangmanGame:
                hangmanGame.write(currentWord)
                hangmanGame.write("\n")
            
        else:
            print(currentWord) # Shows the position of the correctly guessed letters in the word
            with open("hangmanGame.txt","a") as hangmanGame:
                hangmanGame.write(currentWord)
                hangmanGame.write("\n")
            print(f"Your incorrect guesses: {incorrectGuesses}.") # Shows the incorrecly guessed letters
            with open("hangmanGame.txt","a") as hangmanGame:
                hangmanGame.write(f"Your incorrect guesses: {incorrectGuesses}.\n")
        
        guessesLeft = 6 - z # Number of lives avaliable
        print(f"Guesses left: {guessesLeft}")
        with open("hangmanGame.txt","a") as hangmanGame:
            hangmanGame.write(f"Guesses Left: {guessesLeft}\n")
        
        if guessesLeft > 0: 
            pass
        else: # If the number of lives is 0, the game ends
            print(f"Ah, that sucks! Sorry, you lost. The word was {secretWord}.")
            with open("hangmanGame.txt","a") as hangmanGame:
                hangmanGame.write(f"Ah, that sucks! Sorry, you lost. The word was {secretWord}.\n")
            break
        
        while True:
            try:
                global chosenCharacter
                if simulation == 's': # if the game is simulated, the letters will be randomly guessed
                    lowercaseList = list(string.ascii_lowercase) # generates a list with all the lowercase letters
                    randomCharacter = random.choices(lowercaseList, weights=[7.8,2,4,3.8,11,1.4,3,2.3,8.6,.21,.97,5.3,2.7,7.2,6.1,2.8,.19,7.3,8.7,6.7,3.3,1,.91,.27,1.6,.44], k=1)
                    # the probability of a certain letter being chosen is equal to their relative frequency in the English language dictionaries
                    chosenCharacter = randomCharacter[0] # extracts the only character in the list, that becomes the chosen character
                    with open("hangmanGame.txt","a") as hangmanGame:
                        hangmanGame.write(chosenCharacter)
                        hangmanGame.write("\n")
                else: # if the game is played, the current player has the opportunity to take a guess
                    chosenCharacter = input("Please pick a letter or a word that you would like to guess.\n[Only lowercase letters are accepted].\n")
                    with open("hangmanGame.txt","a") as hangmanGame:
                        hangmanGame.write("Please pick a letter or a word that you would like to guess.\n[Only lowercase letters are accepted].\n")
                        hangmanGame.write(chosenCharacter)
                        hangmanGame.write("\n")
                
                if len(chosenCharacter) == 1:
                    if chosenCharacter in incorrectGuesses: 
                        # if the letter guessed has already been guessed incorrectly, the player will receive a warning, instead of losing a life
                        print("You have already guessed incorrectly that letter.")
                        with open("hangmanGame.txt","a") as hangmanGame:
                            hangmanGame.write("You have already guessed incorrectly that letter.\n")
                    elif chosenCharacter in correctGuesses:
                        # if the letter guessed has already been guessed correctly, the player will receive a warning, instead of losing a life
                        print("You have already guessed correctly that letter.")
                        with open("hangmanGame.txt","a") as hangmanGame:
                            hangmanGame.write("You have already guessed correcly that letter.\n")
                    elif chosenCharacter.islower() is True:
                        if chosenCharacter in secretLetters:
                            # if the letter appears in the word, the position of the letter in the word will be revealed
                            print("Well done, your guess was correct.")
                            with open("hangmanGame.txt","a") as hangmanGame:
                                hangmanGame.write("Well done, your guess was correct.\n")
                            correctGuesses.append(chosenCharacter)
                            for count, ele in enumerate(secretLetters):
                                if ele == chosenCharacter:
                                    lettersFound[count] = chosenCharacter
                                else:
                                    continue
                            currentWord = ''.join(c for c in lettersFound)
                            break
                        else:
                            # if the letter doesn't appear in the word, it will be added to the incorrect guesses' list
                            print("Sorry, your guess was incorrect.")
                            with open("hangmanGame.txt","a") as hangmanGame:
                                hangmanGame.write("Sorry, your guess was incorrect.\n")
                            incorrectGuesses.append(chosenCharacter)
                            z += 1
                            break
                    else:
                        # if the character inserted is not valid, the player will receive a warning, instead of losing a life
                        print("Only lowercase letters or words are accepted.")
                        with open("hangmanGame.txt","a") as hangmanGame:
                            hangmanGame.write("Only lowercase letters or words are accepted.\n")
                elif len(chosenCharacter) == len(secretWord):
                    # the player has also the possiblity to guess the secret word
                    if chosenCharacter == secretWord:
                        # if the word guessed is the secret woord, the current player wins
                        currentWord = secretWord
                        break
                    else:
                        # if the string inserted is not the secret word, but has the same length, the player loses a life
                        print("Sorry, your guess was incorrect.")
                        with open("hangmanGame.txt","a") as hangmanGame:
                            hangmanGame.write("Sorry, your guess was incorrect.\n")
                        incorrectGuesses.append(chosenCharacter)
                        z += 1
                        break 
                else:
                    # if the string inserted has a different lenght than the secret word, the player will receive a warning, instead of losing a life
                    print("Please insert only a single letter or a word with the selected size.")
                    with open("hangmanGame.txt","a") as hangmanGame:
                        hangmanGame.write("Please insert only a single letter or a word with selected size.\n")
            except:
                # if the sting inserted doesn't fit any of the criteria, the player will receive a warning, instead of losing a life
                print("Please insert a single lowercase letter or a word with the selected size.")
                with open("hangmanGame.txt","a") as hangmanGame:
                    hangmanGame.write("Please insert a single lowercase letter or a word with the selected size.\n")
               
        if currentWord.isalpha():
            # if all the letters of the secret word have been guessed, the current player wins
            current.victoryMessage()
            print(f"The word was {secretWord}.")
            with open("hangmanGame.txt","a") as hangmanGame:
                hangmanGame.write(f"The word was {secretWord}.")
            break
        else:
            pass
    k = input("Press 'Enter' to exit.") # this message is prompted so that the python file doesn't close automatically after being executed