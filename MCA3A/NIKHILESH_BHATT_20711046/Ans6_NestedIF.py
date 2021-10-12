num=int (input("Enter a Number"))

if num==10:
    if num<20:
        print("Number is less than 20")
        if num<10:
            print("Number is less than 10")
        else:
            print("Number is greater than 10 and less than 20")
    else:
        print("Num is not = 10")
else:
    print("Error!!  Entered Number should be 10")
