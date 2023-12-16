'''
Lab 02 - Python Branching and Looping

Description: Demonstrate branching + looping in Python

Developer Name: Nathan Ilescas 

Date: 10/05/2023
'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################


##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
# 
def factorial(num):
  startingNumber = num - 2
  baseNumber = num * (num -1)
  while(startingNumber >= 1):
    baseNumber *= startingNumber
    startingNumber -= 1
  return baseNumber
  
def state_of_water(temperature): 
  if temperature <= 0:
    return "solid"
  elif 0 < temperature < 100:
    return "liquid"
  else:
    return "gas" 
##C° = (F° - 32)/9 x 5
def F_to_C(f):
  celsius= (f-32)/9 *5
  return celsius 

def letter_grade (grade):
  if grade >= 90 and grade <= 100 :
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
    return "C"
  elif grade >= 60: 
    return "D"
  elif grade >= 0 :
    return "F"
  else: return "error"
##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
#code goes here

userInput = int(input("enter a number:"))
print(factorial(userInput))

temperature = float(input("enter a temperature in degrees celsius:"))
print(f"at{temperature} degrees celsius, the state of water is {state_of_water(temperature)}")

f = float(input("enter a temperature in degrees fahrenheit:"))
celsius= F_to_C(f)
print(f"{f} degrees fahrenheit is equal to {celsius:.2f} degrees celsius.")

grade = float(input("enter a grade:"))
print(letter_grade(grade))
