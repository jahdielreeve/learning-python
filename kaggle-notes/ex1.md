# 📘 Hello, Python Exercise
*Arithmetic operations, variables, and basic expressions.*  
---


## 🧮 Arithmetic Operators Reference

| Operator | Name            | Description                                           |
|---------|-----------------|-------------------------------------------------------|
| a + b   | Addition        | Sum of a and b                                        |
| a - b   | Subtraction     | Difference of a and b                                 |
| a * b   | Multiplication  | Product of a and b                                    |
| a / b   | True division   | Quotient of a and b                                   |
| a // b  | Floor division  | Quotient without fractional part                      |
| a % b   | Modulus         | Remainder when a is divided by b                      |
| a ** b  | Exponentiation  | a raised to the power of b                            |
| -a      | Negation        | The negative of a                                     |

---

## 📝 Qns.1 — Notes
```python
pi = 3.14159  # approximate
diameter = 3
```
## 🎯 Task
Create a variable radius equal to half the diameter.
Create a variable area using the formula: pi × radius².
## ✅ My Answer
```python
radius = diameter / 2
area = pi * radius ** 2
print(radius)
print(area)
```
*'**' use as power in math, r to power of 2*
---
---

## 📝 Qns.2 — Swap Variables
## 🎯 Task
Swap variables a and b.
```python
a = [1,2,3]
b = [3,2,1]
``` 
## 💡My idea
Use another variable → reassign values.

## ✅ My Answer
```python
c = a
a = b
b = c
print(a)
print(b)
```
---

## 📝 Qns.3 — Add Parentheses
## 🎯 Task
Add parentheses so the expression evaluates to 0.
- Original expression:
```python
8 - 3 * 2 - 1 + 1
```
## ✅ My Answer
```python
8 - (3 * 2) - (1 + 1)
```
### 🧠 Note
- Parentheses control priority → override normal operator precedence.
---
## 📝 Qns.4 — Halloween Candy
## 🎯 Scenario
Alice, Bob, and Carol will pool candies and split evenly.
For the sake of their friendship, leftover candies are smashed.
### Example:
91 candies → 30 each → 1 smashed

- Given:
```python
alice_candies = 121
bob_candies = 77
carol_candies = 109
```
## 🎯 Task
Write an expression that calculates how many candies must be smashed.
## ✅ My Answer
```python
to_smash = (alice_candies+bob_candies+carol_candies) % 3
print(to_smash)
```
