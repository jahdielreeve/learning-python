#Use print function to give instruction on terminal
print('Enter a number')
#Use int() function to convert string input to integer
number = int(input('>'))
if number >= 1 and number <= 10:
    print('In Range')
else: 
    print('Out of Range')