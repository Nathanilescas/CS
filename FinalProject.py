'''
If you are completing your final project in Python and NOT using a tkinter GUI, please complete it in this repl.  Be sure all of your team members are joined to this project repl - if anyone joins the wrong team let me know and I can fix it.

(If you are using Snap! then complete your project at snap.berkeley.edu/run and upload your .xml file to Canvas).

(If you are using Python WITH a tkinter GUI then use the Final Project - Python (tkinter) repl instead).
Final Project: Interactive To-Do List

Description: The program has a user to-do list that is constantly evolving based on inputs and outputs. The program will ask the user if they have any tasks to add or subtract from the list, if yes then it will be added/subtracted. If no changes are to be made, the computer will say "Great, here is a list of the remaining tasks you need to complete". The user can also ask "what is on my to-do list and the list will be repeated back to them.

Developer Name(s): Evan Buchholtz, Nathan Ilescas, Eden Nomes

Date: 11/21/2023
'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################
import time
todo_list = []
todo_list_bool = []

##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
#Evan B: This function will add a task to the todo list based on user input
def add_task(task):
  todo_list.append(task) 
#Allows user to add a task to be saved and defined
  for task in todo_list:
    task = task
#Defining tasks for the following functions
    todo_list_bool.append(False)


# Mark complete function: Eden Nomes
# This function will mark a task as complete in the todo list
def mark_complete(currenttask):
  num = 0
  for task in todo_list:
#Loop will iterate through the todo list 
    if(task == currenttask): 
#statement will compare current tasks with what tasks are in the list
      todo_list_bool[num] = True 
#if the task is in the list, then the task is marked as complete.
    num += 1 
#This will update the num variable

def display_tasks():
  num = 0 # Holds the number of the current iteration
  print("\n===== Current Tasks =====")
  for task in todo_list_bool: #This loop will iterate through todo_list_bool 
    if (task == True):# If true, then todo_list will be updated with complete
      print(todo_list[num] + " - Completed")
      num += 1 # This will update the num variable
    else:
      print(todo_list[num] + " - Not Completed") # If false, then todo_list will be updated with not complete
      num += 1 # This will update the num variable
  time.sleep(3) # This will pause the program for 3 seconds to let the user view the list
##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################



######### Program Starts Here: ###########

while True:
  print("\nOptions:")
  print("1. Add a task")
  print("2. Mark a task as complete")
  print(f"3. display tasks")
  print(f"4. exit")
  choice = input("Enter your choice (1-4):")
  if choice == '1':
    task = input("enter the task:")
    add_task(task)
  elif choice == '2':
    task = input("Enter the task to mark as complete:")
    mark_complete(task)
  elif choice == '3':
    display_tasks()
  elif choice == '4':
    print("Exiting the to-do list.")
    break
  else:
    print("invalid choice.")
