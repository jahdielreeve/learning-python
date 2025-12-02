# Task 1: Modify the following function such that it take in a second args representing the number of friends.
# Task 2: If no second argument is provided, it should assume 3 friends
# Task 3: Update the docstring to reflect this new behaviour.


# def to_smash(total_candies):
#    """Return the number of leftover candies that must be smashed after distributing
#       the given number of candies evenly between 3 friends.
    
#    >>> to_smash(91)
#    1
#    """
#    return total_candies % 3

print("Enter total number of candies to be distribute between total number of friends")
print("Leftover to be smashed will be calculate")
print("If number of friends is not given, by default there will be 3 friends")

total_candies = int(input("Number of candies given = \n>"))
inputFriends = input("Number of friends (optional) = \n>").strip()

if inputFriends:
    noOfFriends = int(inputFriends)
else:
    noOfFriends = 3
    
def to_smash(total_candies, noOfFriends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between total no. of friends.
    
    Default number of friends = 3 if no second arguments
    
    >>> to_smash(105, 10)
    5
    """
    return total_candies % noOfFriends
    
print("Leftover candies to be smashed is shown below")
print(to_smash(total_candies, noOfFriends))