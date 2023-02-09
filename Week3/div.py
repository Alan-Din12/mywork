#div.py
# program that reads in two numbers and outputs the integer answer and remainder
#Author : Alan Dineen

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y)
remainder = int(x%y)
print("{} divided by {} is {} remainder {}" .format (x, y, answer, remainder))

