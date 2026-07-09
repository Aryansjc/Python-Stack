p1=[1,1]
p2=[1,1]
t=1
print("--------------------------------------------------------------------------------------")
print("                                   CHOPSTICKS")
print("--------------------------------------------------------------------------------------")
print("RULES: ")
print("1. Each player starts with 1 finger on each hand.")
print("2. When its your turn, you can attack (a) or split (s)")
print("3. Attack: You can attack the opponents hand with one of your hands. The number of fingers on your hand will be added to the opponenets hand.")
print("4. Dead hand: If a hand reaches 5 fingers, it is considered dead and cannot be used to attack or split.")
print("5. Split: You can redistribute the fingers on your hands. You can even bring all fingers on one hand unless it doesnt exceed 4 and the other hand is dead.")
print("6. TO WIN YOU MUST MAKE BOTH OF YOUR OPPONENTS HANDS DEAD.")
print("--------------------------------------------------------------------------------------")
print("FOR HANDS: 0 is left and 1 is right ")
print("--------------------------------------------------------------------------------------")

while True:
    if p1[0]==0 and p1[1]==0:
        print("Player 2 WINS!")
        break
    if p2[0]==0 and p2[1]==0:
        print("Player 1 WINS!")
        break
    print("-------------------------SCOREBOARD-------------------------")
    print("P1 hands: ",p1)
    print("P2 hands: ",p2)

    if t==1:
        print("Player 1's turn: ")
        m=input("Type 'a' to attack or 's' to split: ")
        if m=='a':
            atk=int(input("Which hand to use (0,1): "))
            tgt=int(input("Which hand to attack (0,1): "))

            if p1[atk]==0:
                print("Can't attack with a dead hand!")
            else:
                p2[tgt]=p2[tgt]+p1[atk]
                if p2[tgt]>=5:
                    p2[tgt]=0
                
                t=2
        elif m=='s':
           l=int(input("New fingers on left hand: "))
           r=int(input("New fingers on right hand: "))

           if(l+r)==(p1[0]+ p1[1]):
               p1[0]=l
               p1[1]=r
               t=2
           else:
               print("Wrong Split! Try again.")
    
    elif t==2:
        print("Player 2's turn: ")
        m=input("Type 'a' to attack or 's' to split: ")

        if m=='a':
            atk=int(input("Which hand to use(0,1): "))
            tgt=int(input("Which hand to attack(0,1): "))
            if p2[atk]==0:
                print("Can't attack with a dead hand.")
            else:
                p1[tgt]=p1[tgt]+p2[atk]
                if p1[tgt]>=5:
                    p1[tgt]=0
                t=1

        elif m=='s':
            l=int(input("New fingers for left hand: "))
            r=int(input("New fingers for right hand: "))

            if (l+r)==(p2[0]+p2[1]):
                p2[0]=l
                p2[1]=r
                t=1
            else:
                print("Wrong Split! Try again.")