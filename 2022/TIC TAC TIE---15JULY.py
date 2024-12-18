#                                                TIC TAC TOE





game='''
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
 '''
print(game)

while True:

#---------------------------------------------------------------------------------FIRST MOVE-------------------------------------------------------------------------------------------------
    print("X's turn")
    A=int(input("Where you want place your first move:"))
                                                                        # FIRST MOVE--->FIRST POSSIBLITY                                                          
    if A==1:
        game='''
         X | 2 | 3
        ---|---|---
         4 | 5 | 6
        ---|---|---
         7 | 8 | 9
         '''
        print(game)


        
#---------------------------------------------------------------------------------SECOND MOVE-------------------------------------------------------------------------------------------------                                                                         
        print("O's turn")
        Y=int(input("where you to place your symbol:"))
                                                                        #SECOND MOVE---->FIRST POSSIBLITY
        if Y==1:
            print("THAT PLACE IS ALREADY TAKEN")


                                                                        #SECOND MOVE---->SECOND POSSIBLITY
        elif Y==2:
            game='''
             X | O | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)

#---------------------------------------------------------------------------------THIRD MOVE-------------------------------------------------------------------------------------------------
            print("X's turn")
            U=int(input("where you want place your symbol:"))


                                                                    #THIRD MOVE---->FIRST POSSIBLITY

            if U==1:
                print("THAT PLACE IS ALREADY TAKEN")


                                                                    #THIRD MOVE----->SECOND POSSIBLITY



            elif U==2:
                print("THAT PLACE IS ALREADY TAKEN")


                                                                    #THIRD MOVE----->THIRD POSSIBLITY


            elif U==3:

                game='''
                 X | O | X
                ---|---|---
                 4 | 5 | 6
                ---|---|---
                 7 | 8 | 9
                 '''

                print(game)


                print("O's turn")


#---------------------------------------------------------------------------------FOURTH MOVE-------------------------------------------------------------------------------------------------
                S=int(input("where you want to place your next move:"))


                                                                    #FOURTH MOVE----->FIRST POSSIBLITY

                if S==1:
                    print("THAT PLACE IS ALREADY TAKEN")

                    
                                                                    #FOURTH MOVE----->SECOND POSSIBLITY

                elif S==2:
                    print("THAT PLACE IS ALREADY TAKEN")

                                                                    #FOURTH MOVE----->THIRD POSSIBLITY
                elif S==3:
                    print("THAT PLACE IS ALREADY TAKEN")
                elif S==4:

                    game='''
                     X | O | X
                    ---|---|---
                     O | 5 | 6
                    ---|---|---
                     7 | 8 | 9
                     '''
                    print(game)
#---------------------------------------------------------------------------------FIFTH MOVE-------------------------------------------------------------------------------------------------

                    print("X's turn")


                
                    H=int(input("Where you want to place your next move:"))
                                                                    #FIFTH MOVE----->FIRST POSSIBLITY
                    if H==1:
                        print("THAT PLACE IS ALREADY TAKEN")
                                                                    #FIFTH MOVE----->SECOND POSSIBLITY
                    elif H==2:
                        print("THAT PLACE IS ALREADY TAKEN")
                                                                    #FIFTH MOVE----->THIRD POSSIBLITY
                    elif H==3:
                        print("THAT PLACE IS ALREADY TAKEN")
                                                                    #FIFTH MOVE----->FOURTH POSSIBLITY
                    elif H==4:
                        print("THAT PLACE IS ALREADY TAKEN")
                                                                    #FIFTH MOVE----->FIFTH POSSIBLITY
                    elif H==5:
                        game='''
                         X | O | X
                        ---|---|---
                         O | X | 6
                        ---|---|---
                         7 | 8 | 9
                         '''

                        print(game)


#---------------------------------------------------------------------------------SIXTH MOVE-------------------------------------------------------------------------------------------------

                        print("O's turn")
                        B=int(input("where you want to place your next move:"))
                                                                    #SIXTH MOVE----->FIRST POSSIBLITY
                        if B==1:
                            print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SIXTH MOVE----->SECOND POSSIBLITY                    
                        elif B==2:
                            print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SIXTH MOVE----->THIRD POSSIBLITY                
                        elif B==3:
                            print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SIXTH MOVE----->FOURTH POSSIBLITY
                        elif B==4:
                            print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SIXTH MOVE----->FIFTH POSSIBLITY
                        elif B==5:
                            print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SIXTH MOVE----->SIXTH POSSIBLITY
                        elif B==6:
                    
                            game='''
                             X | O | X
                            ---|---|---
                             O | X | O
                            ---|---|---
                             7 | 8 | 9
                             '''

                            print(game)

#---------------------------------------------------------------------------------SEVENTH MOVE-------------------------------------------------------------------------------------------------
                            print("X's turn")
                            C=int(input("Where you want to place your next move:"))
                                                                    #SEVENTH MOVE----->FIRST POSSIBLITY
                            if C==1:
                                print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SEVENTH MOVE----->SECOND POSSIBLITY                        
                            elif C==2:
                                print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SEVENTH MOVE----->THIRD POSSIBLITY                
                            elif C==3:
                                print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SEVENTH MOVE----->FORTH POSSIBLITY
                            elif C==4:
                                print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SEVENTH MOVE----->FIFTH POSSIBLITY
                            elif C==5:
                                print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SEVENTH MOVE----->SIXTH POSSIBLITY
                            elif C==6:
                                print("THAT PLACE IS ALREADY TAKEN")
                                                                    #SEVENTH MOVE----->SEVENTH POSSIBLITY
                            elif C==7:
                                   
                                game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     X | 8 | 9
                                    '''
                                print(game)
#---------------------------------------------------------------------------------EIGTH MOVE-------------------------------------------------------------------------------------------------
                                print("O's turn")
                                D=int(input("where you want to place your next move"))
                                                                    #EIGTH MOVE----->FIRST POSSIBLITY
                                if D==1:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->SECOND POSSIBLITY                        
                                elif D==2:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->THIRD POSSIBLITY                
                                elif D==3:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->FORTH POSSIBLITY
                                elif D==4:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->FIFTH POSSIBLITY
                                elif D==5:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->SIXTH POSSIBLITY
                                elif D==6:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->SEVENTH POSSIBLITY
                                elif D==7:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->EIGHTH POSSIBLITY
                                elif D==8:
                                    game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     X | O | 9
                                    '''
                                print(game)
                                print("X's turn")

#---------------------------------------------------------------------------------NINTH MOVE-------------------------------------------------------------------------------------------------                                
                                E=int(input("where you want to place your next move:"))
                                                                    #NINTH MOVE----->FIRST POSSIBLITY
                                if E==1:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SECOND POSSIBLITY
                        
                                elif E==2:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->THIRD POSSIBLITY                
                                elif E==3:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->FOURTH POSSIBLITY
                                elif E==4:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->FIFTH POSSIBLITY
                                elif E==5:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SIXTH POSSIBLITY
                                elif E==6:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SEVENTH POSSIBLITY
                                elif E==7:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->EIGHTH POSSIBLITY
                                elif E==8:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->NINTH POSSIBLITY
                                elif E==9:
                                    game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     X | O | X
                                    '''
                                print(game)
                                print("X WINS :) ")
                                break

#---------------------------------------------------------------------------------NINTH MOVE ENDS-------------------------------------------------------------------------------------------------      



                                                                      #EIGTH MOVE----->NINTH POSSIBLITY

                            elif D==9:
                                game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     X | 8 | O
                                    '''
                                
                                    
                                print(game)
                                print("X's turn")
                                
                                E=int(input("where you want to place your next move:"))
                                                                    #NINTH MOVE----->FIRST POSSIBLITY
                                if E==1:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SECOND POSSIBLITY
                        
                                elif E==2:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->THIRD POSSIBLITY                
                                elif E==3:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->FOURTH POSSIBLITY
                                elif E==4:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->FIFTH POSSIBLITY
                                elif E==5:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SIXTH POSSIBLITY
                                elif E==6:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SEVENTH POSSIBLITY
                                elif E==7:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->EIGHTH POSSIBLITY
                                elif E==8:
                                    game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     X | X | O
                                    '''
                                    print(game)
                                    print("NO ONE WINS")
                                    break
                                                                    #NINTH MOVE----->NINTH POSSIBLITY
                                elif E==9:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                

#---------------------------------------------------------------------------------EIGTH MOVE ENDS-------------------------------------------------------------------------------------------------

                                
                                   
                                                             
                                                                       #SEVENTH MOVE----->EIGHTH POSSIBLITY
                                elif C==8:                                 
                                    game='''
                                         X | O | X
                                        ---|---|---
                                         O | X | O
                                        ---|---|---
                                         7 | X | 9
                                        '''
                                    print(game)
                                    print("O's turn")
                                D=int(input("where you want to place your next move"))
                                                                    #EIGTH MOVE----->FIRST POSSIBLITY
                                if D==1:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->SECOND POSSIBLITY                        
                                elif D==2:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->THIRD POSSIBLITY                
                                elif D==3:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->FORTH POSSIBLITY
                                elif D==4:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->FIFTH POSSIBLITY
                                elif D==5:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->SIXTH POSSIBLITY
                                elif D==6:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #EIGTH MOVE----->SEVENTH POSSIBLITY
                                elif D==7:
                                    game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     O | X | 9
                                    '''
                                print(game)
                                print("X's turn")
                                
                                E=int(input("where you want to place your next move:"))
                                                                    #NINTH MOVE----->FIRST POSSIBLITY
                                if E==1:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SECOND POSSIBLITY
                        
                                elif E==2:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->THIRD POSSIBLITY                
                                elif E==3:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->FOURTH POSSIBLITY
                                elif E==4:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->FIFTH POSSIBLITY
                                elif E==5:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SIXTH POSSIBLITY
                                elif E==6:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->SEVENTH POSSIBLITY
                                elif E==7:
                                    print("THAT PLACE IS ALREADY TAKEN")
                                                                    #NINTH MOVE----->EIGHTH POSSIBLITY
                                elif E==8:
                                    game='''
                                     X | O | X
                                    ---|---|---
                                     O | X | O
                                    ---|---|---
                                     X | X | O
                                    '''
                                    print(game)
                                    print("NO ONE WINS")
                                    break                          #EIGTH MOVE----->EIGHTH POSSIBLITY




                                elif D==8:
                                    print("THAT PLACE IS ALREADY TAKEN")


                                
                                    
                                    
                                    

                                    

                    
                           
                    
                    

                    



























































































                    


                                                                          #SECOND MOVE---->THIRD POSSIBLITY  
        elif Y==3:
            game='''
             X | 2 | O
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



                                                                        #SECOND MOVE---->FOURTH POSSIBLITY
        elif Y==4:
            game='''
             X | 2 | 3
            ---|---|---
             O | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)


                                                                        #SECOND MOVE---->FIFTH POSSIBLITY
        elif Y==5:
            game='''
             X | 2 | 3
            ---|---|---
             4 | O | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)


                                                                           #SECOND MOVE---->SIXTH POSSIBLITY 
        elif Y==6:
            game='''
             X | 2 | 3
            ---|---|---
             4 | 5 | O
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



                                                                            #SECOND MOVE---->SEVENTH POSSIBLITY
        elif Y==7:
            game='''
             X | 2 | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             O | 8 | 9
             '''
            print(game)


                                                                                #SECOND MOVE---->EIGHTH POSSIBLITY
        elif Y==8:
            game='''
             X | O | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)


                                                                                #SECOND MOVE---->NINTH POSSIBLITY
        elif Y==9:
            game='''
             X | 2 | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | O
             '''
            print(game)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                                #FIRST MOVE---->SECOND POSSIBLITY
    elif A==2:
        game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
        print(game)


        print("O's turn")
        Y=int(input("where you to place your symbol:"))

        
                                                                            #SECOND MOVE---->FIRST POSSIBLITY    
        if Y==1:

            game='''
             O | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)
            

                                                                            #SECOND MOVE---->SECOND POSSIBLITY
        elif Y==2:
            print("THAT PLACE IS ALREADY TAKEN")



                                                                            #SECOND MOVE---->THIRD POSSIBLITY
                                                                            
        elif Y==3:
            game='''
             1 | X | O
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



                                                                             #SECOND MOVE---->FOURTH POSSIBLITY
        elif Y==4:
            game='''
             1 | X | 3
            ---|---|---
             O | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



                                                                            #SECOND MOVE---->FIFTH POSSIBLITY
        elif Y==5:
            game='''
             1 | X | 3
            ---|---|---
             4 | O | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)


                                                                        #SECOND MOVE---->SIXTH POSSIBLITY
        elif Y==6:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | O
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



                                                                            #SECOND MOVE---->SEVENTH POSSIBLITY
        elif Y==7:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             O | 8 | 9
             '''
            print(game)


                                                                            #SECOND MOVE---->EIGHTH POSSIBLITY
        elif Y==8:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | O | 9
             '''
            print(game)

                                                                        #SECOND MOVE---->NINTH POSSIBLITY
        elif Y==9:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | O
             '''
            print(game)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

    elif A==3:
        game='''
             1 | 2 | X
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
        print(game)




        print("O's turn")
        Y=int(input("where you to place your symbol:"))

        if Y==1:
            game='''
             O | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)
            


        elif Y==2:
            game='''
             O | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            



        elif Y==3:
            print("THAT PLACE IS ALREADY TAKEN")



        elif Y==4:
            game='''
             1 | X | 3
            ---|---|---
             O | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



        elif Y==5:
            game='''
             1 | X | 3
            ---|---|---
             4 | O | 6
            ---|---|---
             7 | 8 | 9
             '''
            print(game)



        elif Y==6:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | O
            ---|---|---
             7 | 8 | 9
             '''
            print(game)




        elif Y==7:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             O | 8 | 9
             '''
            print(game)



        elif Y==8:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | O | 9
             '''
            print(game)


        elif Y==9:
            game='''
             1 | X | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | O
             '''
            print(game)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif A==4:
        game='''
             1 | 2 | 3
            ---|---|---
             X | 5 | 6
            ---|---|---
             7 | 8 | 9
             '''
        print(game)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif A==5:
        game='''
             1 | 2 | 3
            ---|---|---
             4 | X | 6
            ---|---|---
             7 | 8 | 9
             '''
        print(game)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif A==6:
        game='''
             1 | 2 | 3
            ---|---|---
             4 | 5 | X
            ---|---|---
             7 | 8 | 9
             '''
        print(game)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif A==7:
        game='''
             1 | 2 | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             X | 8 | 9
             '''
        print(game)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    elif A==8:
        game='''
             1 | 2 | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | X | 9
             '''
        print(game)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    elif A==9:
        game='''
             1 | 2 | 3
            ---|---|---
             4 | 5 | 6
            ---|---|---
             7 | 8 | X
             '''
        print(game)











































































































        

        
    
        
