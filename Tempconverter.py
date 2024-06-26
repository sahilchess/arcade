


print("\n" * 50)
print("This is a temp converter program")
print("WARNING: You may only use one function for two numbers \n")


def FC(amount):
  print("You have chosen to convert from Fahrenheit to Celsius\n\n")
  print("Your answer is: ", (amount  - 32) * 5/9, "°C")
def FarenheightKelvin(amount):
  print("You have chosen to convert from Fahrenheit to Kelvin\n\n")
  print("Your answer is: ", (amount - 32) * 5/9 + 273.15, "°K")
def CK(amount):
  print("You have chosen to convert from Celsius to Kelvin\n\n")
  print("Your answer is: ", amount  + 273.15, "°K")
def CF(amount):
  print("You have chosen to convert from Celsius to Fahrenheit\n\n")
  print("Your answer is: ", (amount * 9/5) + 32, "°F")
def KF(amount):
  print("You have chosen to convert from  Kelvin to Fahrenheit\n\n")
  print("Your answer is: ", (amount  - 273.15) * 9/5 + 32, "°F")
def KC(amount):
  print("You have chosen to convert from Kelvin to Celsius\n\n")
  print("Your answer is: ", (amount  - 32) * 5/9, "°C")


def changetofullword(x):
  if x == "K":
    return ("Kelvin")
  elif x == "F":
    return ("Farenheight")
  elif x == "C":
    return ("Celsius")
  else:
    print("ERROR!!!: Invalid input \n")
    print("OH NOES! You have to restart the program becuse one or more of your inputs were wrongs?!?!? \n")



def convert_temp(amount, from_temp, to_temp):
    if from_temp == "F" and to_temp == "C":
      return FC(amount)
    elif from_temp == "F" and to_temp == "K":
        return FarenheightKelvin(amount)
    elif from_temp == "C" and to_temp == "F":
        return CF(amount)
    elif from_temp == "C" and to_temp == "K":
        return CK(amount)
    elif from_temp == "K" and to_temp == "C":
        return KC(amount)
    elif from_temp == "K" and to_temp == "F":
        return KF(amount)
    else:
      print("ERROR!!!: Invalid input \n")
      print("OH NOES! You have to restart the program becuse one or more of your inputs were wrongs?!?!? \n")
            
           
while (True):  
  print("what temps? \n 1. Kelvin (enter: K) \n 2. Farenheight (enter: F) \n 3. Celcius (enter: C) \n \n \n")
  
  print("enter 2 temps to convert\n\n")
  xqweqw = (input("Enter the temp you want to convert from: \n\n"))
  y = str(input(" Enter the temp you want to convert to: \n \n"))
  z = int(input("enter the degrees in " + changetofullword(xqweqw) + ": \n"))
  if convert_temp(z, xqweqw, y) is not None:
    print(z, changetofullword(xqweqw), "is equal to", convert_temp(z, xqweqw, y), changetofullword(y), "\n")
  
  
  w = str(input("Do you want to convert more? (y/n): \n"))
  if w == "y":
    print("\n")
    continue
  elif w == "n":
    break
  else:
    print("ERROR!!!: Invalid input \n OH NOES! You have to restart the program because your input was wrongs?!?!?\n \n")
    break

