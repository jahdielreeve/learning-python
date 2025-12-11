# Use help function to understand more of the other functions
help(round)
# help() mention that round() ndigits (the second argument) may be negative
# test what happen when given a negative ndigits

num = int(input("Enter a value to be rounded to the nearest 10,000 \n>"))

newNum = round(num,-5)
print(newNum)