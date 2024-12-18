myfile=open("prog1.txt","r")
line=" "
while line:
    line=myfile.readline()
    for word in line.split():

        print(word,end="#")
    print()
myfile.close()
