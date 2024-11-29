n=int(input("Enter a positive integer:"))
if n<0:
    print("Please enter a positive number.")
else:
    reversed=int(str(n)[::-1])
    print("Reversed number:",reversed)
