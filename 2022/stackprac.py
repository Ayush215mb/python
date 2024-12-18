def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False


def Push(stk,item):
    stk.append(item)
    top=len(stk)-1


def Pop(stk):
    if isEmpty(stk):
        return"Underflow"
    else:
        item=stk.pop()  
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item


def Peek(stk):
    if isEmpty(stk):
        return"Underflow"
    else:
        top=len(stk)-1
        return stk[top]



def Display(stk):
    if isEmpty(stk):
        return"Underflow"
    else:
        top=len(stk)-1
        print(stk[top],"---top")
        for a in range(top -1,-1,-1):
            print(stk[a])


#___________________________MAIN___

stack=[]
top=None

while True:
    print("Choose the Stack Operations to be performed: ")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch=int(input("Enter the number of your choice: "))


    if ch==1:
        print("\n")
        element= int(input("Enter the element to add:"))
        print("\n")
        Push(stack,element)
    elif ch==2:
        item= Pop(stack)
        if item=="Underflow":
            print("\n")
            print("There is no element to Pop")
            print("\n")
        else:
            print("\n")
            print("The popped item is:", item)
            print("\n")
    elif ch==3:
        item= Peek(stack)
        if item=="Underflow":
            print("\n")
            print("There is no element in the stack")
            print("\n")

        else:
            print("\n")
            print("The topmost item is :", item)
            print("\n")

    elif ch==4:
        print("\n")
        Display(stack)
        print("\n")
    elif ch==5:
        break
    else:
        print("Invalid Choice")
        print("\n")