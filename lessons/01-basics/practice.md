# First Python Program

Use these:

- `#` → Comments
- print() → Display
- input() → Get user input
- str(), int(), float() → Convert types
- len() → Count characters
- `+` → Join strings

## Example:
```
# Program says hello and asks for my name
print("Hello, world!")
print("What is your name?")
my_name = input(">")

print("It is good to meet you, " + my_name)
print("The length of your name is:")
print(len(my_name))

print("What is your age?")
my_age = input(">")

print("You will be " + str(int(my_age) + 1) + " in a year.")
```

# Practice Exercises

## Exercise 1: Greeting Upgrade
Modify the "Hello, World" program to:
* Ask for first and last name separately.
* Display a greeting using both.
* Show total number of letters in the full name (excluding spaces).

> **Example Output:**
> What is your first name? John
> What is your last name? Doe
> Nice to meet you, John Doe!
> Your name has 7 letters.

## Exercise 2: Age in the Future
* Ask the user for their current age.
* Ask how many years into the future they want to look.
* Print how old they’ll be then.

> **Example Output:**
> How old are you? 20
> How many years into the future? 5
> In 5 years, you will be 25.

## Exercise 3: Simple Math Game
* Ask for two numbers.
* Print their sum, difference, product, and quotient.

> **Example Output:**
> Enter first number: 10
> Enter second number: 4
> Sum: 14
> Difference: 6
> Product: 40
> Quotient: 2.5

## Exercise 4: Personalized Message
* Ask for name, favorite color, and favorite animal.
* Print a fun personalized sentence.

> **Example Output:**
> What is your name? Alice
> Favorite color? Blue
> Favorite animal? Cat
> Nice to meet you, Alice!
> I bet a blue cat would be your dream pet.

## Exercise 5: Temperature Converter
* Ask for a temperature in Celsius.
* Convert it to Fahrenheit using $F = (C \times 9/5) + 32$.

> **Example Output:**
> Enter temperature in Celsius: 25
> 25°C is 77.0°F

## Exercise 6: Word Reverser
* Ask the user for a word.
* Print it reversed.
* Show how many letters it has.

> **Example Output:**
> Enter a word: Python
> Reversed: nohtyP
> This word has 6 letters.

## Exercise 7: Name Initials
* Ask for first, middle, and last name.
* Display the user’s initials in uppercase.

> **Example Output:**
> Enter your first name: Tony
> Enter your middle name: Stark
> Enter your last name: Rogers
> Your initials are: TSR

## Bonus Challenge
Combine multiple exercises into one program! For example:
* Ask name and age.
* Print a greeting.
* Tell how old the user will be next year.
* Show how many letters are in their name.