import random

print("-------------------------------------------------------------------------------------------------")
print("                                            SURVIVAL GAME")
print("-------------------------------------------------------------------------------------------------")
print("RULES:")
print("1. Reach 300 miles to win the game.")
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
win=300
evt=["Rain","Found Ammo","Snake","Wagon Broke","None","Berries","Sick","Bandits","Bear"]
wts=[10,10,5,5,30,10,15,10,5]
w=50
a=10
t1=0
t2=0


while d<win and h>0:
    print("------------------------------------------")
    print("               Day "+str(day))
    print("------------------------------------------")
    print("Distance: "+str(d)+" | Health: "+str(h)+" | Food: "+str(f)+" | Water: "+str(w)+" | Ammo: "+str(a))

    print("Choose from the below: \n" 
    "- Travel(T)\n" 
    "- Rest(R)\n"
    "- Hunt(H)\n" 
    "- Gather Water(G)")
    c=input("Choice: ")
    if c=='T' or c=='t':
        d=d+random.randint(10,20)
        f=f-5
        h=h-5
        w=w-5
        print("You have travelled!")
    elif c=='R' or c=='r':
        h=h+20
        f=f-5
        w=w-5
        print("You have rested!")
        if h>100:
            h=100
    elif c=='H' or c=='h':
        w=w-5
        h=h-5
        if a>0:
            a=a-1
            f=f+random.randint(10,20)

            print("You have hunted for food!")
        else:
            print("You have no more ammo! You failed the hunt.")
    elif c=="G" or c=="g":
        print("You have gathered fresh water.")
        w=w+random.randint(10,20)
        h=h-5
        f=f-5
    else:
        print("Bad Choice! You stood around and wasted food!")
        f=f-5
        w=w-5

    if d>=100 and t1==0:
        print("You have reached the FIRST FORT! Your health is fully recovered.")
        h=100
        t1=1
    if d>=200 and t2==0:
        print("You have reached the SECOND FORT! Your health is fully recovered.")
        h=100
        t2=1


    if f<0:
        f=0
        h=h-20
        print("Starving! You are hungry as you have run out of food. Your health is decreasing.")
    if w<0:
        w=0
        h=h-20
        print("Dehydrated! You are thirsty as you have run out of water. Your health is decreasing.")
        
    
    if h>0:
        e=random.choices(evt,weights=wts)[0]
        if e=="Berries":
            f=f+10
            print("EVENT: YOU FOUND SOME BERRIES!\n" \
            "You have geined +10 food.")
        elif e=="Sick":
            h=h-15
            print("EVENT: YOU HAVE FALLEN SICK!\n" \
            "You have caught a fever. Your health is decreasing by 15.")
        elif e=="Bandits":
            f=f-15
            w=w-15
            a=a-2
            print("EVENT: BANDITS STOLE YOUR FOOD, WATER AND AMMO! \n" \
            "Your food is decreasing by 15, water by 15 and ammo by 2")
            if f<0:
                f=0
            if w<0:
                w=0
            if a<0:
                a=0
        elif e=="Bear":
            print("EVENT: A BEAR ATTACKED YOU!  -40 Health")
            h=h-40
        elif e=="Rain":
            print("EVENT: IT'S RAINING! Your water supply has increased.")
            w=w+10
        elif e=="Wagon Broke":
            print("EVENT: Your wagon broke down! You have lost some distance.")
            d=d-20
        elif e=="Found Ammo":
            print("EVENT: YOU HAVE FOUND SOME AMMO!")
            a=a+5
        elif e=="Snake":
            print("EVENT: A SNAKE BIT YOU! Your healthhas decreased.")
            h=h-20
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
