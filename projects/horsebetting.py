import random
import time

print("-----------------------------------------------------------------------------------------")
print("                                    HORSE RACING BETTING")
print("-----------------------------------------------------------------------------------------")
print("RULES:")
print("1. You start your betting with $100.")
print("2. You can bet on any of the 4 horses.")
print("3. If your horse wins, you will get the betting amount as the prize.")
print("4. If your horse loses, you will lose the betting amount.")
print("-----------------------------------------------------------------------------------------")

b=100
t=20
while b>0:
    print("Your balance: $"+str(b))
    h=int(input("Pick a horse to win (1-5): "))
    a=int(input("How much do you want to bet: $"))
    if a>b:
        print("You do not have enough monry for the bet.")
        continue
    
    print("\n ---------------------- THE RACE BEGINS ----------------------\n")
    
    p=[0,0,0,0,0]
    w=-1
    while w==-1:
        for i in range(5):
            s=random.randint(1,3)
            p[i]+=s
            if p[i]>=t:
                p[i]=t
                if w==-1:
                    w=i+1

        for i in range(5):
            track=""
            for j in range(p[i]):
                track= track+"-"
            track=track+str(i+1)
            for j in range(t-p[i]):
                track=track+"-"
            print(track)

        print("##########################################")
        time.sleep(0.5)

    print("Horse "+str(w)+" wins the race.")
    if h==w:
        print("Congrats! You won $"+str(a))
        b=b+a
    else:
        print("You lost $"+str(a))
        b=b-a

    if b<=0:
        print("You are out of money. GAME OVER!")
        break
    q=input("Bet again (y/n): ")
    if q=='n':
        print("Thank You for playing. You are leaving with $"+str(b))
        break
    print("\n\n\n\n")