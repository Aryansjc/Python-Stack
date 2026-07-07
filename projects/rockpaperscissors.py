import random
options=["rock","paper","scissors"]
p=0
c=0
print("--------------------------------------------------------------------------------------")
print("                                    Rock, Paper, Scissors")
print("--------------------------------------------------------------------------------------")
print("You would be playing 5 rounds against the computer. ")
print("The player with the most wins after the game is over will WIN.")
print("--------------------------------------------------------------------------------------")

for r in range(1,6):
    print(f"\n------------------------ Round {r} ------------------------")

    pc=input("Enter your choice (rock, paper, scissors): ").lower()
    if pc not in options:
        print("That is not a valid choice. You lost.")
        c=c+1
        continue
    cc=random.choice(options) 
    print(f"Computer chose: {cc}")

    match pc:
        case "rock":
            if cc=="rock":
                print("It is a tie.")
            elif cc=="paper":
                print("Paper covers Rock.")
                c=c+1
            else:
                print("Rock smashes Scissors.")
                p=p+1
        case "paper":
            if cc=="paper":
                print("It is a tie.")
            elif cc=="rock":
                print("Paper covers Rock.")
                p=p+1
            else:
                print("Scirrors cut Paper.")
                c=c+1
        case "scissors":
            if cc=="scissors":
                print("It is a tie.")
            elif cc=="rock":
                print("Rock smashes Scissors.")
                c=c+1
            else:
                print("Scissors cut Paper.")
                c=c+1

print("--------------------------------------------------------------------------------------")
print("                                       Game Over")
print("--------------------------------------------------------------------------------------")

print(f"Final Score - Player: {p} | Computer: {c}")

if p>c:
    print("Congrats! You have won the game.")
elif p<c:
    print("Boom! The computer has won the game.")
