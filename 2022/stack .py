                                                     #stack operations

#functions
def Push(a,val):
    a.append(val)
    print("Value inserted succesfully")


def pop(a):
    x=a.pop()
    print(x,"poped successfully")


def peak(a):
    i=len(a)-1
    print("peak element=",a[i])


def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])



#main

a=[]
while True:
    ch=int(input("1.Push \n2.Pop \n3.Peak \n4.Display \n5.Exit\n Enter your choice:"))

    if ch==1:
        val=int(input("Enter element to push:"))
        Push(a,val)

    elif ch==2:
        if len(a)==0:
            print("stack is underflow")
        else:
            pop(a)


    elif ch==3:
        if len(a)==0:
            print("Stack is underflow")
        else:
            peak(a)



    elif ch==4:
        if len(a)==0:
            print("Stack is underflow")
        else:
            display(a)


    else:
        break


