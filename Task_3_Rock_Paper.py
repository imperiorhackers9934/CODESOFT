import random
import os
score=0
os.system('cls' if os.name == 'nt' else 'clear')
myd={1:"Rock",2:"Paper",3:"Scissors"}
print("Welcome to Rock-Paper-Scissors Game :>>\nYou Will get 10 points for every win with computer and you will loose 5 points for every defeat\nNo Points will be awarded for Tie\n")
while(True):
    computer=random.randint(1,3)
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    print("[0] Exit\n")
    i=int(input("Enter Your Choice [ 1 / 2 / 3 ] :>> "))
    if(i<0 or i>4):
        print("\nWrong Input ;(\nTry Again\n")
        continue
    elif(i==0):
        print("Your Final Score is "+str(score)+" Points")
        exit()
    elif(i==computer):
        print("Its a Tie no one will get points\n")
        continue
    else:
        print(f"You Choose {myd[i]}\nComputer Choose {myd[computer]}")
        if(i==1 and computer==2):
            print("You Loose :(\n")
            score-=5
        if(i==1 and computer==3):
            print("You Win :)\n")
            score+=10
        if(i==2 and computer==1):
            print("You Win :)\n")
            score+=10
        if(i==2 and computer==3):
            print("You Loose :(\n")
            score-=5
        if(i==3 and computer==1):
            print("You Loose :(\n")
            score-=5
        if(i==3 and computer==2):
            print("You Win :)\n")
            score+=10