import numpy as np
# win_con are the wining conditions 
win_con=[[0,3,6], 
         [1,4,7],
         [2,5,8],
         [0,1,2],
         [3,4,5],
         [6,7,8],
         [2,4,6],
         [0,4,8]]
arr=np.array(["","","","","","","","",""])# <-- this is numpy array , 
                                          #it set to be a null until the input
                                          # is enterd by user
unique_input=set()#<-- this is set to save unique input
# the win_c is a function which checks for winning conditions 
def win_c():
    for pattern in win_con:
        pos1val=arr[pattern[0]] 
        pos2val=arr[pattern[1]]
        pos3val=arr[pattern[2]]
        if(pos1val !="" and pos2val !="" and pos3val !=""):
             if(pos1val==pos2val and pos2val==pos3val):
                print("winner is :--->",pos1val)
                return True
    return False 
# inputval is a function in which we call win_c function and also takes input form user             
def inputval(user1,user2):
    for i in range(0,9):
        while(True):
            if i%2==0:
                user_input=int(input(" user 1:--Enter your index in which you want to put your symbel:->"))
                symbel=user1
                # if user1_1 not in unique_input:
                #     if(user1_1==1):
                #         arr[0]=user1
                #     elif(user1_1==2):
                #         arr[1]=user1
                #     elif(user1_1==3):
                #         arr[2]=user1   
                #     elif(user1_1==4):
                #         arr[3]=user1
                #     elif(user1_1==5):
                #         arr[4]=user1
                #     elif(user1_1==6):
                #         arr[5]=user1
                #     elif(user1_1==7):
                #         arr[6]=user1  
                #     elif(user1_1==8):
                #         arr[7]=user1
                #     elif(user1_1==9):
                #         arr[8]=user1
                #     unique_input.add(user1_1)
                #     break
                # else:
                #     print("input is alredy taken")
            else:
                user_input=int(input(" user2---Enter your index in which you want to put your symbel:->"))
                symbel=user2
                # if user2_2 not in unique_input:
                #     if(user2_2==1):
                #         arr[0]=user2
                #     elif(user2_2==2):
                #         arr[1]=user2
                #     elif(user2_2==3):
                #         arr[2]=user2    
                #     elif(user2_2==4):
                #         arr[3]=user2
                #     elif(user2_2==5):
                #         arr[4]=user2
                #     elif(user2_2==6):
                #         arr[5]=user2
                #     elif(user2_2==7):
                #         arr[6]=user2   
                #     elif(user2_2==8):
                #         arr[7]=user2
                #     elif(user2_2==9):
                #         arr[8]=user2
            if user_input not in unique_input and 1<= user_input <=9:
                    arr[user_input-1]= symbel      
                    unique_input.add(user_input)
                    break
            else:     
                    print(" sorry , input is alredy taken please enter diffrent input")
        print(arr.reshape(3,3))
        if win_c(): 
         return  
    print("game draw")          
                       
user1='O'
user2='X' 
print( "user1:--",user1 , "\n" ,"user2:--",user2)  
inputval(user1,user2) 
             