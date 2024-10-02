import numpy as n

def inputRule():
        print("Welcome to game \n")
        print("1|2|3\n4|5|6\n7|8|9")
        user1='X'
        user2='O'
        print("user1 symbel is:---> ",user1)   
        print( "user2 symbel is :--->",user2)  
        inputval(user1,user2)
        
arr=n.array(["","","","","","","","",""])
unique_input=set()
def inputval(user1,user2):
    for i in range(0,9):
        while(True):
            if i%2==0:
                user1_1=int(input(" user 1:--Enter your index in which you want to put your symbel:->"))
                if user1_1 not in unique_input:
                    if(user1_1==1):
                        arr[0]=user1
                    elif(user1_1==2):
                        arr[1]=user1
                    elif(user1_1==3):
                        arr[2]=user1   
                    elif(user1_1==4):
                        arr[3]=user1
                    elif(user1_1==5):
                        arr[4]=user1
                    elif(user1_1==6):
                        arr[5]=user1
                    elif(user1_1==7):
                        arr[6]=user1  
                    elif(user1_1==8):
                        arr[7]=user1
                    elif(user1_1==9):
                        arr[8]=user1
                    unique_input.add(user1_1)
                    break
                else:
                    print("input is alredy taken")
            else:
                user2_2=int(input(" user2---Enter your index in which you want to put your symbel:->"))
                if user2_2 not in unique_input:
                    if(user2_2==1):
                        arr[0]=user2
                    elif(user2_2==2):
                        arr[1]=user2
                    elif(user2_2==3):
                        arr[2]=user2    
                    elif(user2_2==4):
                        arr[3]=user2
                    elif(user2_2==5):
                        arr[4]=user2
                    elif(user2_2==6):
                        arr[5]=user2
                    elif(user2_2==7):
                        arr[6]=user2   
                    elif(user2_2==8):
                        arr[7]=user2
                    elif(user2_2==9):
                        arr[8]=user2
                    unique_input.add(user2_2)
                    break
                else:
                    print(" sorry , input is alredy taken please enter diffrent input")
        print(arr.reshape(3,3))
        check(user1,user2)
             

win_con=[[0,3,6],
         [1,4,7],
         [2,5,8],
         [0,1,2],
         [3,4,5],
         [6,7,8],
         [2,4,6],
         [0,4,8]]
def check(user1,user2):
                if(arr[0]==user1 and arr[3]==user1 and arr[6]==user1):
                    print('user1 is win ')
    
                elif(arr[1]==user1 and arr[4]==user1 and arr[7]==user1):
                    print('user1 is win ')
                    
    
                elif(arr[2]==user1 and arr[5]==user1 and arr[8]==user1):
                    print('user1 is win ')    
                    
                elif(arr[0]==user1 and arr[1]==user1 and arr[2]==user1):
                    print('user1 is win ')
                     
                elif(arr[3]==user1 and arr[4]==user1 and arr[5]==user1):
                    print('user1 is win ') 
                    
                elif(arr[6]==user1 and arr[7]==user1 and arr[8]==user1):
                    print('user1 is win ') 
                    break
                elif(arr[2]==user1 and arr[4]==user1 and arr[6]==user1):
                    print('user1 is win ') 
                         
                elif(arr[0]==user1 and arr[4]==user1 and arr[8]==user1):
                    print('user1 is win ')
                    
                
                elif(arr[0]==user2 and arr[3]==user2 and arr[6]==user2):
                    print("user2 win")
                    
                elif(arr[1]==user2 and arr[4]==user2 and arr[7]==user2):
                    print('user2 is win ') 
                     
                elif(arr[2]==user2 and arr[5]==user2 and arr[8]==user2):
                    print('user2 is win ')  
                      
                elif(arr[0]==user2 and arr[1]==user2 and arr[2]==user2):
                    print('user2 is win ')  
                    
                elif(arr[3]==user2 and arr[4]==user2 and arr[5]==user2):
                    print('user2 is win ') 
                    
                elif(arr[6]==user2 and arr[7]==user2 and arr[8]==user2):
                    print('user2 is win ')  
                    break
                elif(arr[2]==user2 and arr[4]==user2 and arr[6]==user2):
                    print('user2 is win ') 
                          
                elif(arr[0]==user2 and arr[4]==user2 and arr[8]==user2):
                    print('user2 is win ')
                elif(i==6):
                    print("Game draw") 
                    break
                else:
                    print("contnue")  
inputRule()
