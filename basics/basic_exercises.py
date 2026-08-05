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
# Exercise 6: Write a Python program that accepts a sequence of 
# comma-separated numbers from the user and generates a list and a tuple of those numbers.
# --------------------------------------
def exercise_6():
    input_str = input("Give a sequence of numbers in format <NUM, NUM, ...>")
    input_str_list = input_str.split(',')
    input_list = [element.strip() for element in input_str_list]
    input_tuple = tuple(input_list)
    print(input_list)
    print(input_tuple)

# --------------------------------------
# Exercise 7: Write a Python program that accepts a filename from the user and prints the 
# extension of the file.
# --------------------------------------
def exercise_7():
    filename = input("Give a filename:")
    print("File extension: " +  filename.split('.')[-1])

# --------------------------------------
# Exercise 8: Write a Python program to display the first and last colors from 
# the following list:
# color_list = ["Red","Green","White" ,"Black"]
# --------------------------------------
def exercise_8():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0] +' '+ color_list[-1])

# --------------------------------------
# Exercise 9:Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# --------------------------------------
def exercise_9():
    exam_st_date = (11, 12, 2014)
    print("Sample output: The examination will start from: %i / %i / %i" % exam_st_date)



# --------------------------------------
# slaccer-tech exercises

# 15. Sphere Volume Calculator
# Write a Python program to get the volume of a sphere with radius six.

# --------------------------------------

def exercise_15_slaccer():
    import math
    r = 6
    vol_sphere = (4/3) * math.pi * r ** 3
    print("The volume of the spere = ", vol_sphere)
    
# --------------------------------------
# 16. Difference from 17
# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
# --------------------------------------
def exercise_16_slaccer():
    n = int(input("Input a number: "))
    def difference(n):
        if n > 17 : return (n-17)*2
        else : return abs(n-17)
    print(difference(n))


# --------------------------------------
# Testing Area
# --------------------------------------
if __name__ == "__main__":
    print("\nOutput of the Exercise:")
    exercise_16_slaccer()