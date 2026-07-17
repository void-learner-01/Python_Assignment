# Assignment 2

# Q1:Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on the following rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary = int(input("Enter salary: "))

if salary < 30000:
  print("Final tax rate is 5%")
elif salary <= 70000 and salary >= 30000:
  print("Final tax rate is 15%")
else:
  print("Final tax rate is 25%")

#Q2:Write a function that takes two integers a and b prints all even numbers between them (inclusive)
def even_num(a,b):
  for i in range(a, b + 1):
    if i % 2 == 0:
      print(i)

even_num(1, 10)

#Q3:Write a function that prints the digits of a number,For eg: n=312,there are 3,1 and 2 and we need to print them.
def print_digits(n):
  for var in str(n):
    print(var)
print_digits(312)

#Q4:Write a function to return the count the number of digits in a number, n
def count_digits(n):
  return len(str(n))
print(count_digits(312))

#q5:Write a function to return the sum of digits in a number, n
def sum_of_digits(n):
  total = 0
  for digit in str(n):
    total += int(digit)
  return total
print(sum_of_digits(312))

#Q6:Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print(i)

#Q7:Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”
while True:
  user_input = input("Enter a number: ")
  if user_input == "quit":
    break
    number = int(user_input)
    if number > 0:
      print("Positive")
    elif number < 0:
      print("Negative")
    else:
      print("Zero")

#Q8:Letʼs create a simple calculator that performs arithmetic operations. Create a function calculator(a,b,operation) that performs addition, subtraction, multiplication, or division based on the parameter. operation [parameter can have values '+', '-', '*', '/']
def calculator(a, b, operation):
  if operation == '+':
    return a + b
  elif operation == '-':
    return a - b
  elif operation == '*':
    return a * b
  elif operation == '/':
    if b != 0:
      return a / b
    else:
      return "Error: Division by zero"
  else:
    return "Invalid operation"
print(calculator(10, 5, '+'))  
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
  
#Q9:Write a function that returns True if a number is prime and False otherwise, using a loop.
# is_prime(n) -> True/False
# Hint 1: We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number.
# Hint 2: A number n, will always get divided by at least one number in range [2, n-1].
# Non-Prime Example: For number 9, weʼll check in range (2, 8) & itʼll get divided by 3. So itʼs non-prime & weʼll return false for it.
# Prime Example: For number 7, weʼll check in range (2, 6) & it wonʼt get divided by any. So itʼs prime & weʼll return true for it.
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
print(is_prime(1))

#Q10:Letʼs create a“Number Guessing Game”.Givenasecretnumber(alreadydecidedbyyou),writeaprogramthataskstheusertoguessitandprints:
#high•if the guess is above the number"
#Too low•if the guess is below"
#Correct!•if the guess matches
a = int(input("Enter a secret number: "))
if a > 0:
  print("Too high")
elif a < 0:
  print("Too low")
else:
  print("Correct!")
