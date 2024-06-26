
print("This is a calculator program")
print("WARNING: You may only use one function for two numbers \n")


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def add(x, y):
  return x + y
def sub(x, y):
  return x - y
def mult(x, y):
  return x * y
def div(x, y):
  return x / y
def exp(x, y):
  return x ** y

i =int(input("what operation? \n 1. Addition (enter: a) \n 2. Subtraction (enter: b) \n 3. Multiplication (enter: c) \n 4. Division (enter: d) \n 5. Exponent (enter: e)"))

if i == "a":
  print(add(x, y))
elif i == "b":
  print(sub(x, y))
elif i == "c":
  print(mult(x, y))
elif i == "d":
  print(div(x, y))
elif i == "e": 
  print(exp(x, y))
else:
  print("ERROR!!!: Invalid input \n")
  print("OH NOES! You have to restart the program becuse one of your inputs were wrongs?!?!?")
