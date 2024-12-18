file1=(r"E:\PYTHON\file.txt","w")

file1.write('10290390')
file1.close()

def COUNTLINES():
    file1=open(r"E:\PYTHON\file.txt","r")
    lines=file.readlines()
    count=0
    for w in lines:
        if w[0]=="A" or w[0]=="a":
            count=count+1
    print("total lines stat=rted with 'A' , 'a' is",count)



    file1.close()
