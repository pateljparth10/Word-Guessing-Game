word_guess= "Mississippi"
word_split= word_guess.split()
guess_list = []
blank_word = []
guesses_remain = 7
answer = True

for i in range(len(word_guess)):
    blank_word.append("_")
  
while (guesses_remain > 0 and answer):
    print(blank_word)
    guess = str(input("Guess a letter in the word or the word itself?"))

    for i in range(len(guess_list)):
        if (guess == guess_list[i]):
            guesses_remain -=1
            print("You have already guesses that. You have " +str(guesses_remain) + " remaining. You have already guesses " + str(guess_list))
    try:    
        if (len(guess) != len(word_guess) and len(guess) != 1 ):
            guess_list.append(guess)
            guesses_remain -=1
            raise ValueError
    except ValueError:
        print("That is not a valid entry")
    
    if(len(guess) == 1):
        if(word_guess.find(guess)== -1):
            guess_list.append(guess)
            guesses_remain -=1
            print(guess + " was not in the word. You have " + str(guesses_remain) + " Try again!")
        else:
            guess_list.append(guess)
            for position,letter in enumerate(word_guess):
                if (letter == guess):
                    blank_word[position] = guess
            print(blank_word)
    

    if(len(guess) == len(word_guess)):
        if (guess == word_guess):
            print("Congratgulation! You guessed the word correctly!")
            answer_valid = False
        else:
            guess_list.append(guess)
            guesses_remain -= 1
            print(guess + " was not correct. You have " +str(guesses_remain)+ " remaining. Try again!")
    

    
    



