mark=int(input("Enter your marks:"))
match mark//10:
    case 10|9:
        print("Grade A")
    case 8:
        print("Grade B")
    case 7:
        print("Grade C")
    case 6:
        print("Grade D")
    case 5:
        print("Grade E")
    case _:
        print("Fail")
    
