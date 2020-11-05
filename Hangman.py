import random
import time

# Initial step to invite to game :

print("Welcome to Hangman! game\n")
name = input("Please Enter your name : ")
print("Hello! ",name," Best of luck")
time.sleep(2)
print("The game is about to begun")
time.sleep(5)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","tushar","amitabh"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_"*length
    already_guessed = []
    play_game =""

# A loop to re-execute the game when first round ends

def play_loop():
    global play_game
    play_game = input("Do you want to play the game ? Press 'Y' or 'N'")
    while play_game not in ['y','Y','n','N']:
        play_game = input("Do you want to play the game ? Press 'Y' or 'N'")
    if play_game == 'y' or play_game == 'Y':
        main()
    elif play_game == 'n' or play_game =='N':
        print("Thanks!!")
        exit()

# Initializing all conditions of Game

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the hangman word : " + display + " Enter your guess : ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print("Invalid Input!!\nPlease try a Letter")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index+1:]
        display = display[:index] + '_' + display[index+1:]
        print(display + '\n')
    elif guess in already_guessed:
        print('Try another letter.')

    else :
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong Guess " + str(limit - count) + " guesses remaining.")

        elif count == 2 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess " + str(limit - count) + " guesses remaining.")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess " + str(limit - count) + " guesses remaining.")

        elif count == 4 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong Guess " + str(limit - count) + " guesses remaining.")

        elif count == 5 :
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was : ",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats you guessed the word correctly")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()




