print('Welcome to Digital Odd-Even Game by Bijosh')

print('PROJECT OEG')
#variables for future use
user_score=0
even_toss=0
odd_toss=0
computer_score=0
final_choice_of_comp=0
comp_first_batting=False
comp_first_bowling=False
user_first_batting=False
user_first_bowling=False
out_message=0
oh_out_message=0
decision='ok'


import random


#for toss
print(' ---Toss--- ')



choose=input('Choose odd or even:- ')
tossbot=random.randint(1,6)
print(f'So You Have Chosen {choose}')



user_toss=int(input('Enter A No. b/w 1 & 6'))
user_score_toss=user_toss+tossbot
print(f'The total is {user_score_toss}')



#toss calculation
if user_score_toss%2==0:
    even_toss='even'
    print(even_toss)
else:
    odd_toss='odd'
    print(odd_toss)



#to decide who won and choose what they want

#if i won
if choose==even_toss:
    print('You have win the toss And Computer has lost the toss  ')
    user_choice1=input("What do u want to choose bat or bowl  ")
    print(f'User choose to  {user_choice1}')
elif choose==odd_toss:
    print('You have win the toss And Computer has lost the toss  ')
    user_choice1=input("What do u want to choose bat or bowl  ")
    print(f'User choose to  {user_choice1}')




#if computer won the toss 
elif choose!=even_toss:
    print('You have lost the toss And Computer has Won the toss ')
    choices_for_comp=['bat','bowl']
    final_choice_of_comp=random.choice(choices_for_comp)
    print(f'Computer choose to  {final_choice_of_comp}')
elif choose!=odd_toss:
    print('You have lost the toss And Computer has Won the toss ')
    choices_for_comp=['bat','bowl']
    final_choice_of_comp=random.choice(choices_for_comp)
    print(f'Computer choose to  {final_choice_of_comp}')

#linkig to bat and bowl for comp and user 

if (final_choice_of_comp == 'bat'):
    user_choice1 = 'bowl'
elif(final_choice_of_comp == 'bowl'):
    user_choice1 = 'bat'




#decision of first batting and first bowling
if final_choice_of_comp == 'bat':
    comp_first_batting=True
    user_first_batting=False
    user_first_bowling=True
    comp_first_bowling=False

elif final_choice_of_comp == 'bowl':
    comp_first_batting=False
    user_first_batting=True 
    comp_first_bowling=True
    user_first_bowling=False

elif user_choice1 == 'bat':
    user_first_batting=True
    user_first_bowling=False
    comp_first_batting=False
    comp_first_bowling=True

elif user_choice1 == 'bowl':
    user_first_bowling=True
    user_first_batting=False
    comp_first_batting=True
    comp_first_bowling=False

#for batting 
#1
while(decision == 'ok'):
    while user_first_batting==True and comp_first_bowling == True :
        print('############')
        a=input('Enter Your batting number to Continue OR q to quit ')
        if (a!='q'):
            bot=random.randint(1,6)
            print(f'You have entered {a}')
            print(f'The Computer is bowling and has entered {bot}')
            if (bot==int(a)):
                print('---------------')
                out_message='You Are Out'
                print(f'{out_message}')
                comp_first_batting =True
                user_first_bowling=True
                comp_first_bowling=False
                user_first_batting-False
                print(f'Computer Score = {computer_score}')
                print(f'User Score =  {user_score}')
                
                #winner Announcement
                while user_score!=0 and computer_score!=0:
                    if(user_score>computer_score):
                        print('The User has Won The Match')
                        user_first_batting=False
                        comp_first_bowling=False
                        break
                    else:
                        print('The Computer has Won The Match')
                        user_first_batting=False
                        comp_first_bowling=False
                        break

            else:
                user_score=int(a)+user_score
                print(f'User total score so far is {user_score}')  
        else:
            print('Thankyou for playing')
            user_first_batting=False
            comp_first_bowling=False
            break
            
            
  
                   

 
     #2
        while user_first_bowling==True and comp_first_batting==True:
            print('############')
            user_input1=input('Enter Your Bowling number to continue OR q to quit')
            if (user_input1!="q"):
                bot1=random.randint(1,6)
                print(f'You have entered  {user_input1}')
                print(f'The Computer is Batting and has entered  {bot1}')
                if int(user_input1) == bot1:
                    print('--------------')
                    oh_out_message='Oh You have bowled out computer!'
                    print(f'{oh_out_message}')
                    comp_first_batting=False
                    user_first_bowling=False
                    comp_first_bowling=True
                    user_first_batting=True
                    print(f'Computer Score = {computer_score}')
                    print(f'User Score = {user_score}')

                    #winner announcement
                    while user_score!=0 and computer_score!=0:
                        if user_score>computer_score:
                            print('The User has Won the Match')
                            user_first_bowling=False
                            comp_first_batting=False
                            user_first_batting=False
                            comp_first_bowling=False
                            break
                        else:
                            print('The Computer Has Won The Match')
                            user_first_bowling=False
                            comp_first_batting=False
                            user_first_batting=False
                            comp_first_bowling=False                           
                            break

                else:
                    computer_score=int(user_input1)+computer_score
                    print(f'Computer Score So Far is {computer_score}')          

            else:
                print('Thanks For playing')
                user_first_bowling=False
                comp_first_batting=False
                break

    decision='n'


                




#for bowling
#1
    while user_first_bowling==True and comp_first_batting==True:
        print('############')
        user_input1=input('Enter Your Bowling number to continue OR q to quit')
        if (user_input1!="q"):
            bot1=random.randint(1,6)
            print(f'You have entered  {user_input1}')
            print(f'The Computer is Batting and has entered  {bot1}')
            if int(user_input1) == bot1:
                print('--------------')
                oh_out_message='Oh You have bowled out computer!'
                print(f'{oh_out_message}')
                print(f'Computer Score So Far {computer_score}')
                comp_first_batting=False
                user_first_bowling=False
                comp_first_bowling=True
                user_first_batting=True
                print(f'Computer Score = {computer_score}')
                print(f'User Score = {user_score}')

                #winner announcement
                while computer_score!=0 and user_score!=0:
                    if(user_score>computer_score):
                        print('The User Has Won the Game ')
                        user_first_bowling=False
                        comp_first_batting=False
                        break
                    else:
                        print('The Computer Has Won The Game')
                        user_first_bowling=False
                        comp_first_batting=False
                        break



            else:
                computer_score=int(user_input1)+computer_score
                print(f'Computer Score So Far is {computer_score}')

        else:
            print('Thanks For playing')
            user_first_bowling=False
            comp_first_batting=False
   
            break


     #2
        while user_first_batting == True and comp_first_bowling == True :
            print('############')
            a=input('Enter Your batting number to Continue OR q to quit ')
            if (a!='q'):
                bot=random.randint(1,6)
                print(f'You have entered {a}')
                print(f'The Computer is bowling and has entered {bot}')
                if (bot==int(a)):
                    print('---------------')
                    out_message='You Are out'
                    print(f'{out_message}')
                    comp_first_batting =True
                    user_first_bowling=True
                    comp_first_bowling=False
                    user_first_batting-False
                    print(f'Computer Score = {computer_score}')
                    print(f'User Score = {user_score}')

                    #winner announcement
                    while user_score!=0 and computer_score!=0:
                        if (user_score>computer_score):
                            print('The User has Won The Match')
                            user_first_batting=False
                            comp_first_bowling=False
                            user_first_bowling=False
                            comp_first_batting=False
                            break
                        else:
                            print('The Computer has Won The Match')
                            user_first_batting=False
                            comp_first_bowling=False
                            user_first_bowling=False
                            comp_first_batting=False                            
                            break



                else:
                    user_score=int(a)+user_score
                    print(f'User total score so far is {user_score}')

            else:
                print('Thankyou for playing') 
                user_first_batting=False
                comp_first_bowling=False
                break        

    decision='n'        
                



print('The Match has Ended')    





