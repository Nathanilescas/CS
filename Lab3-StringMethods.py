'''
Lab 03 - Programming in Python: Strings

Description: Demonstrate String methods in Python

Developer Name: Nathan Ilescas 

Date: 10/12/2023

'''

#################################################
#	TODO: str.count(sub[, start[, end]])
#################################################

my_string = "sally sells seashells by the seashore"
print("There are " + str(my_string.count("s")) + " \"s\" in the string.")

my_string = "banana"
print("There are " + str(my_string.count("an")) + " \"an\" in the string.")

my_string = "hey there"
print("There are " + str(my_string.count("e")) + " \"e\" in the string.")

#################################################
#	TODO: str.find(sub[, start[, end]])
#################################################

my_string = "ellHo"
print("\"H\" is in the spot: " + str(my_string.find("H")))

my_string = "The dog jumped over the fence"
print("\"dog\" is in the spot: " + str(my_string.find("dog")))

#################################################
#	TODO: str.replace(old, new[, count])
#################################################

my_string = "Hello"
print("Hello was replaced with " + my_string.replace("H", "J"))

my_string = "There is a snake in my boot"
print("There is a snake in my boot was replaced with " + my_string.replace("snake", "squirrel"))
#################################################
#	TODO: str.split([sep], [maxsplit])
#################################################

my_string = "Banana"
print(my_string.split(sep= "n", maxsplit=2))

my_string = "algorithm"
print(my_string.split(sep= "i", maxsplit=1))

#################################################
#	TODO: str.strip([chars])
#################################################

my_string = "Hello"
print("We removed the H from hello to create " + my_string.strip("H"))

my_string = "Bananas"
print("We removed the s in Bananas to create " + my_string. strip ("s"))