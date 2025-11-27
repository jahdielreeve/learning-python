Chapter 1: Hello, Python
Brief overview of Python syntax, variable assignment, and arithmetic operators

## Variable assignment:
- =, is called the assignment operator.
- can reassign the_variable to refer to a different type, like a string or a boolean.
Note: Python doesn't require "declare" before assigning and tell what type of value the variable is

## Function calls:
- call functions by putting parentheses after function name e.g. print ()
- inputs (or arguments) can be put into the function inside the parentheses '()'
- comments begin with the # symbol

# Code example 1
if fish_number > 0:
    print("I don't want ANY fish!")

meat_number = 6
	
# Code explanation
- Some languages use {curly braces} to mark the beginning and end of code blocks.
- Python uses colon (:) at the end of the if line indicates that a new code block is starting.
- meat_number without indentation is not part of the if's code blocks
Note: Python's use of meaningful whitespace, lead to more consistent and readable code than languages that do not enforce indentation of code blocks
- Strings can be marked either by double or single quotation marks.
- But "I don't want ANY fish!", "don't" contains single-quote character, will confuse Python if we surround the string with single-quotes 