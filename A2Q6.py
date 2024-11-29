import random
comp=random.randint(0,9)
user=int(input("Enter the number between 0 to 9:"))
if(comp==user):
    print("You got it right.")
elif(comp==user+1 or comp==user-1):
    print("You nearly got it.")
else:
    print("You got it wrong.")

