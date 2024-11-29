n=int(input("Enter a number:"))
s=0
while n!=0:
    r=n%10
    s=s+r
    n=n//10
if(n%s==0):
    print("It is a harshad number.")
else:
    print("It is not a harshad number")
