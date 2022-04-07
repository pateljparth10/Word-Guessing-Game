import random

guess_list = []
word_list=[]
guesses_remain = 7
answer = True
wins = 0
losses = 0
playing = True
valid_word = False

while playing == True:
    
    while valid_word == False:
        f = open("C:\Repository\Word Guessing Game\words_alpha.txt","r")
        word_from_file = f.readlines()
        value = random.randint(0, len(word_from_file))
        word_guess = word_from_file.pop(value)
        f.close()
        if word_guess not in word_list:
            word_list.append(word_guess)
            blank_word = []

            for i in range(len(word_guess)):
                blank_word.append("_")
            valid_word = True
    
    while (guesses_remain > 0 and answer):
        print(blank_word)
        guess = str(input("Guess a letter in the word or the word itself?"))
        
        try:    
            for i in range(len(guess_list)):
                if (guess == guess_list[i]):
                    raise ValueError

            if (len(guess) != len(word_guess) and len(guess) != 1 ):
                guess_list.append(guess)
                guesses_remain -=1
                raise ValueError
        except ValueError:
            print("That is not a valid entry. You have already guesses " + str(guess_list))
        
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
                    

        if(len(guess) == len(word_guess)):
            if (guess == word_guess):
                print("Congratgulation! You guessed the word correctly!")
                wins +=1
                answer = False
            else:
                guess_list.append(guess)
                guesses_remain -= 1
                print(guess + " was not correct. You have " +str(guesses_remain)+ " remaining. Try again!")

    losses +=1
    print("You have won " + str(wins)+ " games and lost "+ str(losses)+ " games.")
    try_again = str(input("Do you want to play again? Yes or No?"))
    another_game = True
    while another_game:
        if(try_again == "Yes"):
            guesses_remain = 7
            guess_list = []
            valid_word = False
            another_game = False
        elif(try_again == "No"):
            playing = False
            another_game = False
    
    
    

    
    



