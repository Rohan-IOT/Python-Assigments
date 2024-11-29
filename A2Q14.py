mark=int(input("Enter your marks :"))
attendance=int(input("Enter your attendence:"))
assign=int(input("Enter your assignment completion:"))
match mark//10:
    case 10|9:
        print("A")
    case 8:
        print("B")
    case 7:
        print("C")
    case _:
        print("F")
if attendance >=90:
    print("Excellent")
elif attendance >=80 and attendance <= 89:
    print("Good")
elif attendance <80:
    print("Poor")
if assign >=90 and assign <=99:
    print("Good")
else:
    print("Poor")
    if attendance >=90 and assign <99:
           print("Bonus of 5% on score =",(mmark)+(mark*0.05))
    elif attendance <80 and assign <90:
           print("Penalty of 10% on score =",(mark)-(mark*0.10))
