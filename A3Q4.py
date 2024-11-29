n=int(input("Enter a number:"))
sum=0
fact=1
for i in range(n+1):
    if i==0:
        fact=1
    else:
        fact=fact*i
    sum=sum+fact
print("Sum of series is:",sum)
        
