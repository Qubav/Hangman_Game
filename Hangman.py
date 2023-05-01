from random_word import RandomWords
from os import system as sys
from art import logo

# Function checks if letter chosen by player occurs in guessed word. If letter occurs, then function inserts the letter in appropriate positions in blanks(guessed)
# and returns True(letter occured) and updates guessed, if the letter doesn't occure, fucntion returns False(not occured) and blanks(guessed) without update.
def check_letter_occurence(word: str, letter: str, guessed: str):
    num_occ = word.count(letter)
    new_guessed = list(guessed)

    if num_occ > 0:
        for count, char in enumerate(word):
            if char == letter:
                new_guessed[count] = letter
       
        new_guessed = "".join(new_guessed)

        return True, new_guessed
    
    else:
        return False, guessed

# Function checks if drwan word is same as guessed word by comparison strings that contains both.
# If strings are the same, function returns True, else it returns False.
def check_if_player_won(word: str, guessed: str):

    if word == guessed:
        return True
    
    else:
        return False

# Function chceck if chosen letter was already chosen and its position is discovered. Function can be also used to see if player alredy chosen letter and it was alredy said it doesn't occur in guessed word.
# If chosen letter is in string that contains blanks and discovered letters that means it was already chosen, so function returns True, else it returns False.
def was_letter_alredy_chosen(letter: str, guessed: str):
    num_occ = guessed.count(letter)

    if num_occ > 0:
        return True
    
    else:
        return False

# Function that allows user to paly game, comumnicates with user, stores variables and main loop
# stages is list of ASCI arts of stages of game, if help value is True it shows player the word(mainly used for debugging)
def hangman_game(stages: list, help: bool = False):
    
    # variables
    lifes = 6
    r = RandomWords()
    r_word = r.get_random_word()
    guessed = ""
    wrong_guesses = ""
    for _ in r_word:
        guessed += "_"
    game_won = False

    # commmunication with player
    print(logo)
    print("GAME STARTED!")
    if help is True:
        print(f"Psst... The word is {r_word}.")
    print(stages[6 - lifes])
    print(f"You have {lifes} life left.")
    print(f"Guess word {guessed}!")

    # loop that performs all activities that takes part in every round of the game, brakes if player wins game or player has no lifes left
    while lifes > 0 and game_won is not True:
        
        # player chooses letter
        chosen_letter = input("Choose one letter. ")
        chosen_letter = chosen_letter.lower()
        sys("cls")

        # checking if letter was already guessed 
        if was_letter_alredy_chosen(letter = chosen_letter, guessed = guessed):
            print(f"You already chose letter {chosen_letter} that occurs in the guessed word!")
            occured = True

        # checking if letter was already chosen but doesn't occure in the word
        elif was_letter_alredy_chosen(letter = chosen_letter, guessed = wrong_guesses):
            print(f"You already chose letter {chosen_letter} that doesn't occure in guessed word!")
            occured = False
        
        # if letter wasn't alredy chosen checking if it occurs in the word
        # if letter occurs gessed(variable - string with blanks) is updated and occued valuse is True, 
        # if it doesn't guessed is not updated, occured value is Fals, wrog_guesses string is updated and player loses one life
        else:
            occured, guessed = check_letter_occurence(r_word, chosen_letter, guessed)
            print(f"You chose letter {chosen_letter}.")
            if occured is False :
                lifes -= 1
                wrong_guesses += chosen_letter
        
        # checking if player won game by guessing the word
        game_won = check_if_player_won(r_word, guessed)

        # printing ASCI art for appropriate stage of game based on player lifes left
        print(stages[6 - lifes])

        # communication with player based on game state
        # if one of gameending criteria is True ending game
        if game_won is True :
            print(f"You win! Congratulations!\nYou guessed {guessed}.\nU still have {lifes} left.")

        elif lifes == 0:
            print(f"I am sorry, but You lost.\nYou guessed {guessed}\nThe word was {r_word}.")

        else:
            if occured is False:
                print(f"Letter {chosen_letter} didn't occure in word!")

            if lifes == 1:
                print(f"You have only {lifes} life left!\nYou guessed {guessed}")

            else:
                print(f"You have {lifes} lifes left.\nYou guessed {guessed}")
        
    # communication with player
    print("GAME ENDED!\n")

# used ASCI art list source: https://inventwithpython.com/invent4thed/chapter8.html
hangman_stick_person_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


if __name__ == "__main__":
    sys("cls")
    hangman_game(stages = hangman_stick_person_pics, help = True)
