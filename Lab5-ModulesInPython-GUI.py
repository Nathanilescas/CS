'''

Lab 05 - Programming in Python: Modules & GUIs

Description: Travel from the 1970's into the modern times with tkinter. You are going to create a GUI! This will be a good beggining taste of what is possible with GUI's and you can modify this GUI with anything you want and keep updating it as you learn. I hope you enjoy it!

Developer Name: Nathan Ilescas

Date: 12/03/2023

'''
##########################################
# IMPORTS:
#   modules needed for program
from tkinter import *
##########################################
# This is where you need to import tkinter
##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
def binary():
	user_input = int(entry_1.get()) #retrieves input from user
	answer = bin(user_input)[2:] #converts to binary
	label_2.config(text=answer, bg= "light green") #displays answer
	print(answer) #displays answer

def birthYear():
  userInput = int(entry_one.get())
  answer = (userInput - 2023)
  label_two.config(text= answer, bg="light green")
  print("You were born in " + answer)
##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
'''
root = Tk()

label_1 = Label(root, text = "Enter your number: ")
entry_1 = Entry(root, width = 5)

label_2 = Label(root, text = "Waiting", bg= "yellow")
button_1 = Button(root, text = "Calculate", command = binary)

label_1.grid(row= 0, column = 0)
entry_1.grid(row= 0, column= 1)
label_2.grid(row= 0, column=2)
button_1.grid(row= 0, column=3)

root.mainloop()
'''
###################################################################

secondRoot = Tk()

label_one = Label(secondRoot, text= "How old are you: ")
entry_one = Entry(secondRoot, width = 5)

label_two = Label(secondRoot, text = "Waiting on You", bg= "light blue" )
button_one = Button(secondRoot, text = "Calculate", command = birthYear)

label_one.grid(row= 0, column= 0)
entry_one.grid(row= 0, column= 1)

label_two.grid(row= 0, column= 2)
button_one.grid(row= 0, column= 3)

secondRoot.mainloop()