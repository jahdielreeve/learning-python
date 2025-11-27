#Practice while loop and import library from py
import random

print('Rock,Paper,Scissors, Lets play!')
print('Type quit to stop playing')

while True:
    
    user_choice = input('Choose rock/paper/scissors > ').lower()
    my_list = ['rock','paper','scissors']
    pc_choice = random.choice(my_list)
    
    if user_choice == 'quit':
        print('Thank you for playing')
        break
# Use break to exit/stop loop
# Use 'continue' to return to the start of the loop again, good for restarting loop
    if user_choice not in my_list:
        print('Try again with a valid choice')
        continue
# When doing if else indentation is important to set the function within a condition, will cause IndentationError   
    print('Computer choice: ' + pc_choice + ', Your choice: ' + user_choice)
    if (user_choice == pc_choice):
        print('Its a Draw')
    elif((user_choice == 'paper' and pc_choice == 'rock') 
    or (user_choice == 'rock' and pc_choice == 'scissors') 
    or (user_choice == 'scissors' and pc_choice == 'paper')):
        print('You Win')
    else:
        print('You Lose')  