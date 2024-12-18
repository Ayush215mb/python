#WAP to accept three numbers  frm the user and then find the biggest number
a=int(input('enter first no.:'))
b=int(input('enter second no.'))
c=int(input('enter third no.:'))
if a>b:
    big=a
else:
    big=b
if big>c:
    print('the largest no.among',a,b,c,'=',big)
else:
    print('the largest no. among',a,b,c,'=',c)


        

              
