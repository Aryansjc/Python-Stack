import random

print("--------------------------------------------------------------------------------------------------------------")
print("                                                LCR")
print("--------------------------------------------------------------------------------------------------------------")
print("RULES: ")
print("1. Every player starts with 3 chips.")
print("2. When its your turn, you roll dice equal to the number of chips you have (maximum up to 3 dice)")
print("3. THE DICE: ")
print("         L: Give one chip to the player on your left.")
print("         R: Give one chip to the player on your right.")
print("         C: Put one chip in the center.")
print("         '.': Do noting. Just skip your turn.")
print("4. Even when you have no chips left, you can still play in the game and wait for someone to pass you a chip.")
print("5. The game ends when only one player has chips left. That player wins all the chips in the center.")

p=[3,3,3]
n=len(p)
c=0
i=0

while True:
    alive=0
    for x in p:
        if x>0:
            alive+=1
    
    if alive<=1:
        break
    chips=p[i]
    if chips >0:
        print("----------------------------")
        print("Player "+str(i)+" turn: ")
        print ("Chips: "+ str(p))
        print("Center: "+ str(c))

        ro=chips
        if ro>3:
            ro=3

        input("Press enter to roll "+ str(ro)+ " dice:")
        for d_num in range(ro):
            d=random.choice(["L","R","C","."])
            print("Rolled: "+d)
            if d=="L":
                p[i]-=1
                left=(i-1)%n
                p[left]=p[left]+1

            elif d=="R":
                p[i]-=1
                right=(i+1)%n
                p[right]+=1
            elif d=="C":
                p[i]-=1
                c+=1
            elif d==".":
                pass
    
    i=(i+1)%n

print("---------------------------------------------------------")
print("                      GAME OVER")
print("---------------------------------------------------------")
print("Final chips: "+str(p))
print("Center: "+str(c))

for i in range(n):
    if p[i]>0:
        print("Player "+str(i)+" wins the game and takes the "+str(c)+" chips in the center.")
print("----------------------------------------------------------------------------------------")