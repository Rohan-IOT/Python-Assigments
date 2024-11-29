n=int(input("Enter a number:"))
s=0
sq=n*n
while sq!=0:
    r=sq%10
    s=s+r
    sq=sq//10
if(s==n):
    print("It's a neon number")
else:
    print("It's not a neon number")
    

