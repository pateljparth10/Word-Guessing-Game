word_guess= "Mississippi"
word_split= word_guess.split()
guess_list = []
blank_word = []
guesses = 7

for i in range(len(word_guess)):
    blank_word.append("_")
  
def check_guess(guess, guesses):
    if(guess == guess_list):
        guesses -=1
        print("You have already guesses that. You have " +str(guesses) + " remaining. You have already guesses " + str(guess_list))
    if(len(guess) == 1):
        if(word_guess.find(guess)== -1):
            guess_list.append(guess)
            guesses -=1
            print(guess + " was not in the word. You have " + str(guesses) + " Try again!")
        else:
            for position,letter in enumerate(word_guess):
                if (letter == guess):
                    blank_word[position] = guess
            print(blank_word)
    else:
        guess_list.append(guess)
        print("That is not a valid guess. Please try again.")

    if(len(guess) == len(word_guess)):
        if (guess == word_guess):
            print("Congratgulation! You guessed the word correctly!")
        else:
            guess_list.append(guess)
            guesses -= 1
            print(guess + " was not correct. You have " +str(guesses)+ " remaining. Try again!")
    else:
        guess_list.append(guess)
        print("That is not a valid guess. Guess is either too long or too short. Please try again.")
            
check_guess("bob", guesses)  


# while guesses > 0:
#     guess = str(input("Enter a letter or word to guess the correct word."))
