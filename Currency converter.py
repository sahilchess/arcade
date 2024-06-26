


print("\n" * 50)
print("This is a currecy converter program")
print("WARNING: You may only use one function for two numbers \n")



def USPound(x):
  return x * 0.79
def USRupee(x):
  return x * 83.58
def USYen(x):
  return x * 160.63
def USEuro(x):
  return x * 0.94
def EuroYen(x):
  return x * 171.59
def EuroUS(x):
  return x * 1.07
def EuroPound(x):
  return x * 0.85
def EuroRupee(x):
  return x * 89.24
def RupeeEuro(x):
  return x * 0.011
def RupeeUS(x):
  return x * 0.012
def RupeeYen(x):
  return x * 1.92
def RupeePound(x):
  return x * 0.0095
def PoundUS(x):
  return x * 1.26
def PoundEuro(x):
  return x * 1.18
def PoundYen(x):
  return x * 202.88
def PoundRupee(x):
  return x * 105.53
def YenRupee(x):
  return x * 0.52
def YenEuro(x):
  return x * 0.0058
def YenPound(x):
  return x * 0.0049
def YenUS(x):
  return x * 0.0062


def changetofullword(x):
  if x == "USD":
    return ("US Dollars")
  elif x == "E":
    return ("Euros")
  elif x == "Y":
    return ("Yen")
  elif x == "INR":
    return ("Indian Rupees")
  elif x == "BP":
    return ("Pound Sterlings")


def convert_currency(amount, from_currency, to_currency):
    if from_currency == "USD" and to_currency == "BP":
      return USPound(amount)
    elif from_currency == "USD" and to_currency == "Euro":
      return USEuro(amount)
    elif from_currency == "USD" and to_currency == "Y":
      return USYen(amount)
    elif from_currency == "USD" and to_currency == "INR":
      return USRupee(amount)
    elif from_currency == "E" and to_currency == "Y":
      return EuroYen(amount)
    elif from_currency == "E" and to_currency == "USD":
      return EuroUS(amount)
    elif from_currency == "E" and to_currency == "BP":
      return EuroPound(amount)
    elif from_currency == "E" and to_currency == "INR":
      return EuroRupee(amount)
    elif from_currency == "INR" and to_currency == "Euro":
      return RupeeEuro(amount)
    elif from_currency == "INR" and to_currency == "USD":
      return RupeeUS(amount)
    elif from_currency == "INR" and to_currency == "Y":
      return RupeeYen(amount)
    elif from_currency == "INR" and to_currency == "BP":
      return RupeePound(amount)
    elif from_currency == "BP" and to_currency == "USD":
      return PoundUS(amount)
    elif from_currency == "BP" and to_currency == "E":
      return PoundEuro(amount)
    elif from_currency == "BP" and to_currency == "Y":
      return PoundYen(amount)
    elif from_currency == "BP" and to_currency == "INR":
      return PoundRupee(amount)
    elif from_currency == "Y" and to_currency == "INR":
      return YenRupee(amount)
    elif from_currency == "Y" and to_currency == "E":
      return YenEuro(amount)
    elif from_currency == "Y" and to_currency == "BP":
      return YenPound(amount)
    elif from_currency == "Y" and to_currency == "USD":
      return YenUS(amount)
    else:
      print("ERROR!!!: Invalid input \n")
      print("OH NOES! You have to restart the program becuse one or more of your inputs were wrongs?!?!? \n")
while (True):  
  print("what curency? \n 1. Euro (enter: E) \n 2. USD (enter: USD) \n 3. Indian Rupee (enter: INR) \n 4. Yen  (enter: Y) \n 5. British Pound (enter: BP) \n \n \n")
  
  print("enter 2 currencys to convert\n")
  xqweqw = (input("Enter the currency you want to convert from: \n"))
  y = str(input("\n Enter the currency you want to convert to: \n "))
  z = int(input("\n\n enter amount in " + xqweqw + "\n"))
  if convert_currency(z, xqweqw, y) is not None:
    print(z, changetofullword(xqweqw), "is equal to", convert_currency(z, xqweqw, y), changetofullword(y), "\n")
  
  
  w = str(input("Do you want to convert more? (y/n): \n"))
  if w == "y":
    print("\n")
    continue
  elif w == "n":
    break
  else:
    print("ERROR!!!: Invalid input \n OH NOES! You have to restart the program because your input was wrongs?!?!?\n \n")
    break

