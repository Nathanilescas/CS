'''

Programming HW 3 - Name Game

Description: Implement a program that can produce a verse of the "Name Game" song given an input name.

Developer Name(s): Nathan Ilescas

Date: 

'''

##########################################
# IMPORTS:
#   modules needed for program
##########################################


##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
#code goes here
def name_game(name):
    print(name.upper())

    if(name.count("B") == 0) :
       firstVers = name + ", " + name + ", " + "bo-B" + name[1:] 
    else: 
        firstVers = name + ", " + name + ", " + "bo-" + name[1:] 
    print(firstVers)

    if(name.count("F") == 0) :
      secondVers = "Banana-fana fo-F" + name[1:]
    else:
      secondVers = "Banana-fana fo-" + name[1:]
    print(secondVers)
  
    if(name.count("M") == 0) :
       thirdVers = "Fee-fi-mo-M" + name[1:]
    else: 
        thirdVers = "Fee-fi-mo-" + name[1:]
  
    print(thirdVers)
    lastVers = name + "!"
    print(lastVers)

    return  ""#stub, replace with your code


##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
#leave the following alone

print(name_game("Abby"))
verse_name = input("Next name: ")
name_game(verse_name)
