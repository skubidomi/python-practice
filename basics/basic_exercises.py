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

# --------------------------------------
#  1. Formatted Twinkle Poem
# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
# --------------------------------------
def exercise_1_slaccer():
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# --------------------------------------
# 2. Python Version Checker
# Write a Python program to find out what version of Python you are using.
# --------------------------------------
def exercise_2_slaccer():
    import sys
    import platform
    print("Python verzió: ", platform.python_version())

# --------------------------------------
# 3. Current DateTime Display
# Write a Python program to display the current date and time.
# Sample Output : Current date and time : 2014-07-05 14:34:14
# --------------------------------------
def exercise_3_slaccer():
    print("Current date and time: ",datetime.now())

# --------------------------------------
# 4. Circle Area Calculator
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# --------------------------------------
def exercise_4_slaccer():
    from math import pi
    r=float(input("Input the radius of the circle: "))
    area=pi*r**2
    print("The area of the circle with radius " + str(r) + " is: " + f"{area:.5f}")

# --------------------------------------
# 5. Reverse Full Name
# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# --------------------------------------
def exercise_5_slaccer():
    firstname = input("Input your first name: ")
    lastname = input("Input your last name: ")
    print("Reverse full name: " , lastname , firstname)

# --------------------------------------
# 6. List and Tuple Generator
# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# --------------------------------------
def exercise_6_slaccer():
    sample_data = input("Input some comma-separated numbers: ")
    data_list = sample_data.split(",")
    data_tuple = tuple(data_list)
    #print("data_list_data_type: ", type(data_list))
    #print("data_tuple_data_type: ", type(data_tuple))
    print("List : ", data_list)
    print("Tuple : ", data_tuple)

# --------------------------------------
# 7. File Extension Extractor
# Write a Python program that accepts a filename from the user and prints the extension of the file.
# --------------------------------------
def exercise_7_slaccer():
    filename = input('Input the Filename with extension: ')
    file_extension = filename.split('.', -1)
    print('The extension of the file is : ' , file_extension [-1])

# --------------------------------------
# 8. First and Last Colors
# Write a Python program to display the first and last colors from the following list.
# --------------------------------------
def exercise_8_slaccer():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0], color_list[-1])

# --------------------------------------
# 9. Exam Schedule Formatter
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# --------------------------------------
def exercise_9_slaccer():
    exam_st_date = (22, 7, 2026)
    #print(type(exam_st_date))
    print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")

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
    def difference(n):
        if n > 17 : return (n-17)*2
        else : return abs(n-17)

    n = int(input("Input a number: "))
    print(difference(n))


# --------------------------------------
# Testing Area
# --------------------------------------
if __name__ == "__main__":
    print("\nOutput of the Exercise:")
    exercise_9_slaccer()