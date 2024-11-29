import random
comp=random.randint(0,2)
user=int(input("Enter 0 for rock,1 for paper,2 for scissor:"))
if(comp==user):
    print("Draws")
elif(user>comp):
    print("User wins")
else:
    print("Computer wins")
