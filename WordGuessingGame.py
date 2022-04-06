word_guess= "Mississippi"
word_split= word_guess.split()
word_list = []
blank_word = []
guesses = 7
print(len(word_guess))
for i in range(len(word_guess)):
    blank_word.append("_")
print(blank_word)

for position,letter in enumerate(word_guess):
    if (letter == "i"):
       blank_word[position] = "i"
print(blank_word)