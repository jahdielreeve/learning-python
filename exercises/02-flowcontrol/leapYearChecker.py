print('Enter a year')
#Use int() function to convert string input to integer
year = int(input('>'))
#Logic for leap years:
# 1. Divisible by 4
# 2. but divisible by 100 NOT leap year
# 3. but divisible by 400 is leap again
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Its a leap year')
else:
    print('Not a leap year')