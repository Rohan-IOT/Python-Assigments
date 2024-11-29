'''n=int(input("Enter a number:"))
s=0
j=1
for i in range(1,n+1):
    if i%2!=0:
        print(i*j,end='')
        s=s+(i*j)
        j=-j
print("Sum of series:",s)'''



n=int(input("enter a number: "))
j=1
sum=0
for i in range(1,2*n,2):
    sum=sum+(i*j)
    j = -j
print(sum)
