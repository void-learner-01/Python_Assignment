# AssignmentProblems

# Q1.Write a program that asks the user for their name and age, then prints a sentence like:
# Hello Shradha, you are 21 years old!

name = input("Enter a name: ")
age = input("Enter your age: ")

print("Hello",name,",","you are",age,"years old!")

# Q2.Take two numbers as input from the user and print their sum, difference, product, and quotient.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Q3.Ask the user to enter two integers and one float. Convert them all to floats and print their average.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = float(input("Enter a float: "))

print((a + b + c) / 3)

# Q4.The user enters a string containing a number (e.g., "45"). Convert it to: "45" • an integer • a float • a string again. Print all three values with their types.

a = input("Enter a: ")
b = int(a)
c = float(a)
d = str(a)

print(b, type(b))
print(c, type(c))
print(d, type(d))

#Q5.Evaluate and print the result of the following expression:
# x =10+3*2**2
#Based on what you learnt in the lecture, explain why the output is what it is.

x =10+3*2**2
print(x)

#Q6.Write a program to swap the values of two numbers entered by the user.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
a,b = b,a

print(a,b)

#Q7.Ask the user for a temperature in Celsius (as a string input). Convert it to a float, then calculate and print the temperature in Fahrenheit. The conversion formula is: Fahrenheit = (Celsius * (9/5)) + 32

Cel = input("Enter temperature: ")
Celsius = float(Cel)
Fahrenheit = (Celsius * (9/5)) + 32
print(Fahrenheit)

#Q8.Take the radius as user input and print the area. Use the formula: π * (radius ** 2) (value of π = 3.14)

radius = int(input("Enter radius: "))
area = 3.14 * (radius ** 2)
print(area)

#Q9.Ask the userfor:Principal(P),Rate(R),Time(T).Convertalltoandcomputesimpleinterest:Q9floatSI=(P∗R∗T)/100
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
SI = (P * R * T) / 100
print(SI)

#Q10.Take a decimal number as input (like 45.78) and output its: • integer part (45) • fractional part (-0.78)

number = float(input("Enter number: "))
integer_part = int(number)
fractional_part = float(number)
print("Integer part:", integer_part)
print("Fractional part:", fractional_part)
