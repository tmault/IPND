# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# Add your own code and notes here


# Lessons 2.2: Variables Quix

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0 
cycles_per_second = 2700000000.0
distance_travelled = speed_of_light / cycles_per_second # This gives the distance that light travels in one processer cylce in meters
print distance_travelled 


# Lesson 2.2.: Spirit Age

# Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive.


age = 21
days_in_year = 365
days_alive = age * days_in_year
print days_alive