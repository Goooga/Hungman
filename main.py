import random
import os


def check(letter,word):
    i = 0
    for c in word:
        if c == letter:
            return i
        else:
            i+=1
    return -1


tries = 9 
errors = 0
hits = 0
words = ['харомы','топар','апеляцией','личность','водяный']
word = random.choice(words)
guess = []
for i in range(len(word)):
    guess.append('_')
used = []


while errors<tries:
    
    
    os.system('cls')
    print(*guess)
    print(f"U have {tries-errors} tries of {tries} left")


    letter = input()
    if not letter in used:
        used.append(letter)
        if letter in word:
            print("Right!")
            index = check(letter,word)
            guess[index] = letter
            hits+=1
            if hits == len(word):
                os.system('cls')
                print(*guess)
                print("U won the game!!!")
                break
        
        
        else:
            errors+=1
            print("Wrong!")
    
    
    else:
        print("U already used this letter!")
        input("press Enter!")
else:
    print("u lose")
    input("press Enter!")