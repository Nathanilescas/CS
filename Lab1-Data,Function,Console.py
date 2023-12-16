'''
Lab 01 - Programming in Python: Data, Functions, and Console I/O

Description: A program to calculate annual car emissions.

Developer Name: Nathan Ilescas

Date: 9/19/2023

'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################
#None for this lab

##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################

### Step 2 Create your function definition for calc_car_emissions here
'''Calculates the average annual vehicle emissions using equation from the instructions
  ----------
  mpg
    vehicle's average miles per gallon
  avg_miles_driven
    average number of miles driven per year
  '''
def calc_car_emissions(avg_miles_driven, mpg):
  avg_annual_emissions = float(19.6*(avg_miles_driven/mpg))
  return avg_annual_emissions


##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################


# Get input from user
# Since we are going to be calling the function calc_car_emissions(mpg, avg_miles_driven)
# We know that we are going to need a variable for mpg and avg_miles_driven
# We now have the two variables we need for our calc_car_emissions, so we can call it with those values
# We are also going to assign the value to a variable so we can use it later
# Print out the values
# Calculate and print the US average
# Calculate and print the two comparison values
mpg = float(input("enter miles per gallon:"))
avg_miles_driven = float(input("enter average miles driven: "))



print("Your car produces", calc_car_emissions(avg_miles_driven, mpg),"pounds of CO2 per year.")

print("The average car is driven 11388 miles per year and gets 21.6 MPG, it produces ","{:.2f}".format(calc_car_emissions(11388,21.6)),"pounds of CO2 per year.")

print("If your mpg was",int(mpg+2)," then your car emissions would be ","{:.2f}".format(calc_car_emissions(avg_miles_driven,(mpg+2)))," pounds of CO2 per year.  That's",
       "{:.2f}".format(calc_car_emissions(avg_miles_driven, mpg) - calc_car_emissions(avg_miles_driven,(mpg+2)))," lbs less!")

print("If you drove 10% less miles, then your car emissions would be ","{:.2f}".format(calc_car_emissions(avg_miles_driven,mpg) - calc_car_emissions(avg_miles_driven *.10,mpg))," pounds of CO2 per year.  That's ","{:.2f}".format(calc_car_emissions(avg_miles_driven,mpg) - (calc_car_emissions(avg_miles_driven,mpg) - calc_car_emissions(avg_miles_driven *.10,mpg)))," lbs less!")