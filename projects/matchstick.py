m=[]
for i in range(21):
    m.append("| ")

print("--------------------------------------------------------------------------------------")
print("                                        MATCHSTICK")
print("--------------------------------------------------------------------------------------")
print("RULES: ")
print("There are 21 matchstickes. ")
print("You and computer will take turns to pick 1, 2 or 3 matchsticks.")
print("The last one to pick the last match loses!")

while len(m)>0:
    print(f"Sticks ({len(m)}): ", end="")
    for s in m:
        print(s, end=" ")
    print("\n")
    p=0
    v=False
    while v== False:
        j=input("Choose 1, 2 or 3 matchsticks: ")
        if j.isdigit():
            p=int(j)
            if p<1 or p>3:
                print("Invalid input. Choose from 1, 2 or 3 matchsticks: ")
            elif p>len(m):
                print("Not enough Sticks left!")
            else:
                v=True
        
    for i in range(p): 
        m.pop()
        
    if len(m)==0:
        print("You took the last one! YOU LOSE.")
        break
    print("\n Computer's Turn: ")
    c=4-p
    if c>len(m):
        c=len(m)

    print(f"Computer takes {c} matchsticks.")

    for i in range(c):
        m.pop()

    if len(m)==0:
        print("Computer took the last matchstick! YOU WIN.")
        break