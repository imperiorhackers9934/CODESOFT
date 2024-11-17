def calc(a,b,op):
    if(op==1):
        return (a+b)
    elif(op==2):
        return (a-b)
    elif(op==3):
        return (a*b)
    elif(op==4):
        return (a/b)
    elif(op==5):
        return (a**b)
    else:
        raise ValueError
while True:
    print("<","-"*6,"Calculator","-"*6,">")
    print("[0] Exit")
    print("[1] Addition (x+y)")
    print("[2] Subtraction (x-y)")
    print("[3] Multiplication (x*y)")
    print("[4] Division (x/y)")
    print("[5] Exponent (x^y)")
    try:
        i=int(input("\nEnter the Requried Operation:>> "))
        if(i==0):
            print("Thanks for Using ;)")
            exit()
        a=int(input("Enter The Value x :>> "))
        b=int(input("Enter The Value y :>> "))
        print("The Result for this Arithematic operation is -: "+str(calc(a,b,i))+"\n\n")
        if input("Do you Want to Continue [Yes/No] :>> ")=='Yes' or 'Yes'.lower():
            continue 
        else:
            print("Thanks for Using ;)")
            exit()
    except Exception as e:
        print("Error Occured! Please Try Again")
    finally:
        continue