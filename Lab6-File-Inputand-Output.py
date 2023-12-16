'''
Lab 06 - Programming in Python: File Input and Output

Description: You are going to learn how to read files, write to files, and you will learn a couple of cool little tricks! Everything we are going to use is built-in for Python and is extremely easy to use!  

Developer Name: Nathan Ilescas

Date: 12/5/2023

'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################
# nothing here this lab
##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
# nothing here this lab
##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
'''your code for step 1 goes below this statement'''

food_file = open("Favorite Foods", 'w')
food_file.write("Nathan Burger\n" + "Eden Pasta\n" + "Evan Pizza\n")
food_file.close()

'''your code for step 2 goes below this statement'''

food_file = open("Favorite Foods", 'r')
for line in food_file:
  name, food = line.split(' ',1)
  print(name, "has a favorite food of", food)
  
'''your code for step 3 goes below this statement'''

mystery_file = open("mystery song", 'r')
solved_file = open("solved song", 'w')
for line in mystery_file:
  for letter in line:
    
    if(letter == ' '):
      solved_file.write(' ')
      
    elif(letter == 'z'):
      solved_file.write('a')
    elif(letter == 'g'):
      solved_file.write('t')
    elif(letter == 'n'):
      solved_file.write('m')
    elif(letter == 'r'):
      solved_file.write('i')
    elif(letter == 't'):
      solved_file.write('g')
    elif(letter == 's'):
      solved_file.write('h')
    elif(letter == 'g'):
      solved_file.write('t')
    elif(letter == 'h'):
      solved_file.write('s')
    elif(letter == 'v'):
      solved_file.write('e')
    elif(letter == 'y'):
      solved_file.write('c')
    elif(letter == 'i'):
      solved_file.write('r')
    elif(letter == 'a'):
      solved_file.write('z')
    elif(letter == 'c'):
      solved_file.write('y')
    elif(letter == 'd'):
      solved_file.write('w')
    elif(letter == 'x'):
      solved_file.write('b')
    elif(letter == 'l'):
      solved_file.write('o')
    elif(letter == 'f'):
      solved_file.write('u')
    elif(letter == 'm'):
      solved_file.write('n')
    elif(letter == 'o'):
      solved_file.write('k')
    elif(letter == 'p'):
      solved_file.write('l')
    elif(letter == 'w'):
      solved_file.write('d')
    elif(letter == 'k'):
      solved_file.write('p')
    elif(letter == 'u'):
      solved_file.write('f')
    elif(letter == 'e'):
      solved_file.write('v')
    elif(letter == 'q'):
      solved_file.write('j')
    else:
      solved_file.write(letter)

mystery_file.close()
solved_file.close()
print("The song's name is Happy by Pharrell Williams")
