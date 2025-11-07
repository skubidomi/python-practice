"""
BASIC EXERCISES
Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""

import sys
import time
from datetime import datetime
import math

# --------------------------------------
# Exercise 1: Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like 
# a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
#
#Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are
# --------------------------------------
def exercise_1():
    sample = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
# --------------------------------------
# Exercise 2: Write a Python program to find out what version of Python you are using
# --------------------------------------
def exercise_2():
    print(sys.version)
    print("Python " + str(sys.version_info.major) +'.'+ str(sys.version_info.minor) +'.'+ str(sys.version_info.micro))
     
# --------------------------------------
# Exercise 3: Write a Python program to display the current date and time
# --------------------------------------
def exercise_3():
    print(datetime.now())
                
# --------------------------------------
# Exercise 4: Write a Python program that calculates the area of a circle based on the radius entered by the user. 
# --------------------------------------
def exercise_4():
    r_string = input("Give the radius and press 'ENTER'\nr: ")
    r = float(r_string)
    a = r*r*math.pi
    print("Area: " + str(a))
# --------------------------------------
# Exercise 5: Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 
# --------------------------------------
def exercise_5():
    name = input("Give a first and last name in format <FIRST_NAME><SPACE><LAST_NAME> :\n") #not exactly the task but it is more complicated
    name_splits = name.split(' ')
    if len(name_splits) != 2:
        print("The given name cannot be separated into 2 parts")
    else:
        first_name = name_splits[0]
        last_name = name_splits[1]
        print(last_name+" "+first_name)

# --------------------------------------
# Testing Area
# --------------------------------------
if __name__ == "__main__":
    print("\nOutput of the Exercise:")
    exercise_5()