#Writing function base on the given docstring
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num,2)

num = float(input("Enter a number to be rounded to 2 decimal places \n >"))  
print (round_to_two_places(num))