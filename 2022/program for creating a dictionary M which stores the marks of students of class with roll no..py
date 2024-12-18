#program for creating a dictionary M which stores the marks of students of class with roll no.
M={}
n= int(input('how many students?'))
for a in range (n):
    r,m=eval(input('enter roll no. , marks:'))
    M[r]=m


print('created dictionary')
print(M)
