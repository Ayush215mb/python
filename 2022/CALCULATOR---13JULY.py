


#                            CALCULATOR


def add(a,b):
    c= a+b
    print("After adding both numbers: ",c)



def sub(a,b):
    d= a-b
    print("After subtracting the second number from first number: ",d)




def mult(a,b):
    e= a*b
    print("After multiplying both numbers: ",e)


def div(a,b):
    k=a/b
    print("After dividing: ",k)







                        #________main_________





while True:
    a=int(input("enter the first number:"))
    b=int(input("Enter the second number:"))

    print("\n")
       
    print("PRESS")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.STOP\n")
    
    ch=int(input("chose what you want to do:"))

    if ch==1:
        add(a,b)
        
    elif ch==2:
        sub(a,b)
        

    elif ch==3:
        mult(a,b)
        

    elif ch==4:
        div(a,b)
        

    elif ch==5:
        break

        
    else:
        print("invalid option")
        






    









