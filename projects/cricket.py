import random
tr=0
w=0
b=6
i=0
ar=[]
print("--------------------------------------------------------------------------------------")
print("                                   Cricket Match")
print("--------------------------------------------------------------------------------------")
print("SUPER OVER CRICKET MATCH")
print("Possible outcomes for a ball: ")
print("1. Wicket: w")
print("2. Wide: wd")
print("3. Runs: 1,2,3,4,5,6")
print("-------------------------------------------------------------------------------------")

while i<b:
    num=random.randint(0,8)
    if num==7:
        v="w"
    elif num==8:
        v="wd"
    else:
        v=str(num)
    
    ar.append(v)
    if v=="w":
        w=w+1
        i=i+1
        print("Ball "+str(i)+": OUT!")
        
    elif v=="wd":
        tr=tr+1
        print("Wide! +1 run")
    else:
        i=i+1
        print("Ball "+str(i)+": "+v)
        tr=tr+1
print("--------------------------------------------------------------------------------------")
print("Over History: ", ar)
print("Total runs scored: ",tr)
print("Total Wickets lost: ",w)
