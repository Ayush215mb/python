

import pickle
stu={}
fin= open("Student.dat","rb")
try:
    print("Below are the records")
    while True:
        stu= pickle.load(fin)
        print(stu)
except EOFError:
    fin.close()
