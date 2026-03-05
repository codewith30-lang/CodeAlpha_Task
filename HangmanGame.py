import random

alphabet = ["meat", "pet", "mat", "pen"]
word = random.choice(alphabet)

display = [" "] * len(word)    #display = [" ", " ", " ", " ", " "]  
chances = 5

while chances > 0:

    print("Word is:", " ".join(display))  # .join(display) joins list elements into one string.
    letter = input("Guess a letter: ")

    if letter in word:
        for i in range(len(word)):     #for i, ch in enumerate(word):        or       # for i in enumerate(word): 
           if word[i] == letter:                                                      #      if i[1] == letter:
                display[i] = letter                                                   #          display[i[0]] = letter
            
                
    else:
        print("Wrong guess!")
        chances -= 1
        print("Chances left:", chances)

    if " " not in display:
        print("Correct answer,YOU WIN!", word)
        break

if chances == 0 and " " in display:

    print("You lost 😢 The word was:", word)
