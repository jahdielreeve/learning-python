# 📘 Python Learning Log — Chapter 2: Functions and Getting Help
*A summary of calling functions (fn), defining our own fn and using docstrings*

---

## 📝 Key Concepts

### 📌 Getting Help, using help () function
- help() function is most important Python function 
- key to understand other function when knowing how to use help ()

**Example:**
```python
help(round)

Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
```
### 🔍 Code Explanation
help() function displays two things:
1. the header of that function round(number, ndigits=None). 
- tells us that round() takes an argument we can describe as number. 
- optionally it can also take in a separate argument which is described as 'ndigits'.
2. Follow by a brief descriptions of what the function does.

### 🧠 Note
- To learn a function using help () only pass in the name of the function itself, 
and not the result of calling that function.

**Example:**
```python
help(round(-2.01))

Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 ...
```
- Python evaluates an expression like this from the inside out. 
- First it calculates the value of round(-2.01), 
- then it provides help on the output of that expression. 
*End up the help() will be explaining on Integer instead. TAKE NOTE!!*
---

### 📌 Defining functions
- Uses *def* keyword
- indented block of code following the *:* is run when the fn is called
See the least_difference fn example below

### 💻 Code Example
```python
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
```
### 🔍 Code Explanation
1. *least_difference* function takes in 3 arguments (args): a, b, c.
2. Fn start with a header *def* with the indented block of code to be ran when fn is called
3. *return* is another keyword uniquely associated with functions.
- When Python encounters a return statement, it exits the function immediately
- Also passes the value or output on its right hand side to the calling context
- Right hand side: *min(diff1, diff2, diff3)* is the output when *least_difference(a, b, c)* is called 

**Example:**
```python
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

Console output: 
9 0 1
```

### 📌 Docstrings
- When defining a function, we can provide a description in it, 
- which is called the *docstring*.

### 💻 Code Example
```python
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
```
### 🔍 Code Explanation
1. docstring start with a triple-quoted string *"""* immediately after the header of the function
2. when a defined function contained a docstring, using help () on the function will shows docstring
**Example:**
```python
help(least_difference)

Help on function least_difference in module __main__:

least_difference(a, b, c)
    Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
```
3. When writing docstring, the last two lines are an example function call and result.
NOTE *>>>* is a reference to the command prompt used in Python interactive shells. Python doesn't run this example call.
4. Good programmers use docstrings unless they expect to throw away the code