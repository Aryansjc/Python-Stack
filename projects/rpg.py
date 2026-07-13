import random

print("-------------------------------------------------------------------------------------------------")
print("                                            SURVIVAL GAME")
print("-------------------------------------------------------------------------------------------------")
print("RULES:")
print("1. Reach 100 miles to win the game.")
print("2. You have to start with 100 Health and 50 Food.")
print("3. Each day you can choose to travel, rest or hunt.")
print("4. There are some random events that can happen each day.")
print("5. If your health reaches 0 you die and lose the game.")
print("6. If you run out of food then you will starve and your health will keep on decreasing each day.")
print("-------------------------------------------------------------------------------------------------")

d=0
h=100
f=50
day=1
win=100
evt=["None","Berries","Sick","Bandits","Bear"]
wts=[40,30,15,10,5]

while d<win and h>0:
    print("------------------------------------------")
    print("               Day "+str(day))
    print("------------------------------------------")
    print("Distance: "+str(d)+" | Health: "+str(h)+" | Food: "+str(f))
    print("Choose from the below: \n" 
    "- Travel(T)\n" 
    "- Rest(R)\n"
    "- Hunt(H)")
    c=input("Choice: ")
    if c=='T' or c=='t':
        d=d+random.randint(10,20)
        f=f-5
        h=h-5
        print("You have travelled!")
    elif c=='R' or c=='r':
        h=h+20
        f=f-5
        print("You have rested!")
        if h>100:
            h=100
    elif c=='H' or c=='h':
        f=f+15
        h=h-5
        print("You have hunted for food!")
        f=f-5
    else:
        print("Bad Choice! You stood around and wasted food!")
        f=f-5

    if f<0:
        f=0
        h=h-20
        print("Starving! You are hungry as you have run out of food. Your health is decreasing.")
    if h>0:
        e=random.choices(evt,weights=wts)[0]
        if e=="Berries":
            f=f+10
            print("EVENT: YOOU FOUND SOME BERRIES!\n" \
            "You have geined +10 food.")
        elif e=="Sick":
            h=h-15
            print("EVENT: YOU HAVE FALLEN SICK!\n" \
            "You have caught a fever. Your health is decreasing by 15.")
        elif e=="Bandits":
            f=f-15
            print("EVENT: BANDITS STOLE YOUR FOOD! \n" \
            "Your food is decreasing by 15")
            if f<0:
                f=0
        elif e=="Bear":
            print("EVENT: A BEAR ATTACKED YOU!  -40 Health")
            h=h-40
        else:
            print("EVENT: A peaceful and adventurous day without any special events.")
    day=day+1

print("--------------------------------------------------------------------")
print("                              GAME OVER")
print("--------------------------------------------------------------------")
if h<=0:
    print("You have fallen during the journey. You have travelled "+str(d)+" miles")
elif d>=win:
    print("CONGRATS! You have survived and completed the game in "+str(day-1)+" days")