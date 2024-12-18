#                                       TIC TAC TOE

def winX():
    if(gamestr1[0]==gamestr1[1]==gamestr1[2]=='X'):
        print(player1+"wins")

    elif(gamestr1[0]==gamestr2[0]==gamestr3[0]=='X'):
        print(player1+"wins")
        

    elif(gamestr1[2]==gamestr2[2]==gamestr3[2]=='X'):
        print(player1+"wins")
        

    elif(gamestr3[0]==gamestr3[1]==gamestr3[2]=='X'):
        print(player1+"wins")
        

    #diagonal wins-- X wins

    elif(gamestr1[0]==gamestr2[1]==gamestr3[2]=='X'):
        print(player1+"wins")
        

    elif(gamestr3[0]==gamestr2[1]==gamestr1[2]=='X'):
        print(player1+"wins")
        

def winO():
#sidewise wins-- O wins
    if(gamestr1[0]==gamestr1[1]==gamestr1[2]=='O'):
        print(player2+" wins")
            

    elif(gamestr1[0]==gamestr2[0]==gamestr3[0]=='O'):
        print(player1+"wins")
            

    elif(gamestr1[2]==gamestr2[2]==gamestr3[2]=='O'):
        print(player2+" wins")
            

    elif(gamestr3[0]==gamestr3[1]==gamestr3[2]=='O'):
        print(player2 + " wins")
            

#diagonal wins-- O wins

    elif(gamestr1[0]==gamestr2[1]==gamestr3[2]=='O'):
        print(player2+" wins")
            

    elif(gamestr3[0]==gamestr2[1]==gamestr1[2]=='O'):
        print(player2+" wins")

def rowX():
        if (m>0 and m<=3):
            gamestr1[m-1]='X'

        elif(m>3 and m<=6):
            gamestr2[m-4]='X'
        elif(m>6 and m<=9):
            gamestr3[m-7]='X'
        elif(m<0 or m>9):
            print("Invalid option")


def rowO():
        if (n>0 and n<=3):
            gamestr1[n-1]='O'

        elif(n>3 and n<=6):
            gamestr2[n-4]='O'
        elif(n>6 and n<=9):
            gamestr3[n-7]='O'
        elif(n<0 or n>9):
            print("Invalid option")
            
            


#________________________________________main___________________________________

gamestr1= [1,2,3]
gamestr2= [4,5,6]
gamestr3= [7,8,9]
        

player1 = input(str("Name of player1: "))
player2 = input(str("Name of player2: "))

print("\n")


print(player1 + "'s symbol is X")
print(player2 + "'s symbol is O")

print("\n")


for i in range(0,5):
    print( player1 + "'s turn")
    m = int(input("where do you want put your move?"))

    rowX()
    if(rowX()==True):
        break
    else:
        continue

    

    print("\n")

    print(gamestr1)
    print(gamestr2)
    print(gamestr3)

    print("\n")



    winX()
    winO()
    if(winX()==True or winO()==True):
        break   
        

#_____________________________________________player2 turn________________________________________
    
    if(i==4):#to make sure that there are only 9 movess
        break
    
    print( player2 + "'s turn")
    n = int(input("where do you want put your move? "))
    rowO()
    
            
    print("\n")

    print(gamestr1)
    print(gamestr2)
    print(gamestr3)

    print("\n")


    winX()
    winO()
