'''

Python Lab 4 - Lists in Python (Work in teams of 2-3)

Description: Using Lists in Python (and past topics like looping, strings, etc.) to understand and practice. Also to tell stories!

Developer Name: Nathan Illescas 

Date: 10/31/2023

'''
##########################################
# IMPORTS:
#   modules needed for program
##########################################
import time #for sleep




##########################################
# FUNCTIONS:
#   functions useful to main program
##########################################
def print_typewriter(text):
  for char in text:
    print(char, end='', flush= True)
    time.sleep(.2)
    
  

  '''
  Given some text, prints each character one at a time,
  with a small pause in between (like if someone were
  typing on a typewriter).
  '''
  #code here!

def print_story(lines):
  for story in lines:
    print("\n")
    print_typewriter(story)
    print("\n")
  '''
  Given a list of lines, prints each line like a typewriter
  on its own line and one at a time.
  '''
  #code here!

##########################################
# MAIN PROGRAM:
#   beginning of running program
##########################################
title = "The Boy Who Lived"
story = ["The boy found out his parents are dead and he has powers.", "The boy went to school and became a powerful wizard.", "The boy lived a happy life after killing his enemy."]

print_typewriter(title.center(50))
print() #print blank line
print_story(story)
print() #print blank line
print_typewriter("F I N".center(50))


print_typewriter("The Boy Who Lived")
story_text = ["The boy found out his parents are dead and he has powers.", "The boy went to school and became a powerful wizard.", "The boy lived a happy life after killing his enemy."]
print_story(story_text)