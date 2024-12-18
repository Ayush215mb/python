#create a binary file student.dat and add data-rollno, name and marks to it

import pickle
stu= {}
stufile= open("student.dat","wb")
ans="y"
while ans=="y":
    rno= int (input("Enter roll no.:"))
    name= input("Enter name:")
    marks = float(input("Enter marks:"))
    stu["roll"]= rno
    stu["name"]= name
    stu["Marks"]= marks
    pickle.dump(stu,stufile)
    ans=input("Do you wish to continue? (Y/N)")

stufile.close()
