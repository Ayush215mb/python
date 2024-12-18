a=open('file.txt','w+')
stud =int(input("Enter total no. of students: "))


record= " "
for i in range(0,stud):
        name= input("Enter name of student: ")
        Class=input("Enter class: ")
        rollno=input("Enter roll no. ")
        rec= name+ str(Class) + str(rollno)+ "     "

a.write(rec)

a.close()

