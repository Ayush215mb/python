fileout= open("student.dat","w+")
for i in range(5):
    name=input("Enter name of student: ")
    fileout.write(name)

fileout.close()
