import random as rm
print()
print()
print("WelCome To Guess The Number Game..!!!")
print("-"*37)
print()
print("Select The Number Of Rounds--->","(","1","3","5",")")
print("-"*27)
r=int(input("Enter No of Rounds :"))
if r==1:
    t=10
    cc=rm.choice([j for j in range(t)])
    for i in range(1,r+1):
        print()
        print()
        print("*"*35)
        print("Round",i)
        print("*"*8)
        print("Guess The Number (1-10)")
        k=int(input("Enter Your Guess Number :"))
        print()
        if k==cc:
            print(chr(2),chr(2),"You Win The Game",chr(2),chr(2))
            print()
            break
        else:
            print("You Loss the Game")
            print()
        print("The Number is-->",cc)
        print("*"*35)
        break
if r==3:
    t=50
    cc=rm.choice([j for j in range(t)])

    for i in range(1,r+1):
        print()
        print()
        print("*"*35)
        print("Round",i)
        print("*"*7)
        print("Guess The Number (1-50)")
        k=int(input("Enter Your Guess Number :"))
        print()
        if k==cc:
            print(chr(2),chr(2),"You Win The Game",chr(2),chr(2))
            print()
            break
        elif k<cc:
            print("Too Small")
            print("*"*35)
        elif k>cc:
            print("Too Big")
            print("*"*35)
        
    print("You Loss the Game")
    print()
    print("The Number is-->",cc)
    print("*"*35)
if r==5:
    t=100
    cc=rm.choice([j for j in range(t)])

    for i in range(1,r+1):
        print()
        print()
        print("*"*35)
        print("Round",i)
        print("*"*7)
        print("Guess The Number (1-100)")
        k=int(input("Enter Your Guess Number :"))
        print()
        if k==cc:
            print(chr(2),chr(2),"You Win The Game",chr(2),chr(2))
            print()
            break
        elif k<cc:
            print("Too Small")
            print("*"*35)
        elif k>cc:
            print("Too Big")
            print("*"*35)
        
    print("You Loss the Game")
    print()
    print("The Number is-->",cc)
    print("*"*35)

