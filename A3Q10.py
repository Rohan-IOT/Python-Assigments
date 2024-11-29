n=int(input("Enter a number:"))
while n!=0:
    r=n%10
    n=n//10
    if str(r) in str(n):
        print("It's not a Happy number.")
        break
else:
    print("It's a Happy number.")
