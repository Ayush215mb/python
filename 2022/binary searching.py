

import pickle
stu= {}
found= False
print("Searching")
fin= open('student.dat','rb')
try:
    while true:
        stu= pickle.load(fin)
        if stu['marks']>45:
            print(stu)
            found=True
        if found== False:
            print("no records found")
        else:
            print("Search succesful")
except EOFError:
 
            
