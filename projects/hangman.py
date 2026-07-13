print("--------------------------------------------------------------------------------------")
print("                                                          HANGMAN")
print("--------------------------------------------------------------------------------------")

w=['H','A','C','K','C','L','U','B']
l=8
d=['-','-','-','-','-','-','-','-']
g=[]
a=8

while a>0:
    print("Word to guess: "," ".join(d))
    print("Guessed Letters: ",g)
    print("Attempts Left: ",a)
    ans=input("Guess a letter: ")

    if len(ans) !=1:
        print("Please type exactly one letter.")
        print("-------------------------------")
        continue
    if ans in g:
        print("You already guessed that letter!")
        print("--------------------------------")
        continue

    g.append(ans)
    if ans in w:
        print("Correct!")
        for i in range(len(w)):
            if w[i]==ans:
                d[i]=ans
    else:
        print("Wrong")
        a=a-1

    if '-' not in d:
        print("Word: "," ".join(w))
        print("You WIN!")
        break
    print("------------------------------------------")
if a==0:
    print("You LOSE!")
    print("The word was: ","".join(w))