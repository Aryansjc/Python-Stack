import random
g=[]
num=random.randint(1,100)
print("-------------------------------------------------------------------------------------")
print("                                 Guess The Number")
print("-------------------------------------------------------------------------------------")
gu=True

print("The computer has selected a number between 1 and 100. You have to guess the number.")

while gu:
    i=input("Enter your guess: ")
    guess=int(i)
    g.append(guess)

    if guess<num:
        print("You have guessed lower! Try again")
    elif guess>num:
        print("You have guessed higher! Try again")
    else:
        print("Congrats! You have guessed the number correctly.")
        
        gu=False
