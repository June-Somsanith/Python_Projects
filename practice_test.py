# %%
# 34.1 Assign variables, mathematical operations

# Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site.
# Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:
# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles

# output: Distance: total_miles_traveled miles



# %%
# 34.2 Assign variables, modulus operator (%)

# Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.

# output: Tons: value_1
# Pounds: value_2
# Ounces: value_3



# %%
# 34.3 Formatted output of data type

# Create a solution that accepts an integer input representing the index value for any of hte five elements in the following list:
# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
#Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.

# output: Element index_value: data_type



# %%
# 34.4 Data types in formulas

# Create a solution that accepts any three integer inputs represnting the base (b1, b2) and height (h) measurements of a trapezoid in meters.
# Output the exact area of hte trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the base height measurement.

# Trapezoid Area Formula:
# A = [(b1 + b2) / 2] * h

# ouput: Trapezoid area: area_value square meters



# %%
# 34.5 Data type conversions

# Create a solution that accepts five integer inputs. Output the sum of the five inputs 3 times, converting the inputs to the requested data type prior to finding the sum.
# First output: sum of five inputs maintained as integer values
# Second output: sum of five inputs converted to float values
# Third output: sum of five inputs converted to string values (concatenate)

# Integer: integer_sum_value
# Float: float_sum_value
# String: string_sum_value

# %%
# 33.6 Phone Number Breakdown

# Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212
# Hint: use % to get the desired rightmost digits
# Hint: use // to shift right by the desired amount

phone_number = int(input())

# %%
# 34.7 Comparison operations with Boolean Values

# Create a solution that accepts an integer input to compare against the following list:

# predef_list = [4, -27, 15, 33, -10]

# Greater Than Max? Boolean_value



# %%
# 34.8 Try Block with Exception Errors

# Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
# Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# %%
# 34.9 Branching conditional logic
# Create a solution that accepts an integer input representing water temperature in degrees fahrenheit.
# Output a description of the water state based on the following scale:

# If the temperature is below 33° F, the water is “Frozen”.
# If the water is between 33° F and 80° F (including 33), the water is “Cold”.
# If the water is between 80° F and 115° F (including 80), the water is "Warm".
# If the water is between 115° F and 211° (including 115) F, the water is “Hot".
# If the water is greater than or equal to 212° F, the water is “Boiling”.
# Additionally, output a safety comment only during the following circumstances:

# If the water is exactly 212° F, the safety comment is "Caution: Hot!"
# If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
# The solution output should be in the format
# water_state
# optional_safety_comment

# %%
# 34.10 Dictionary Key Search

# Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent number of string inputs represnting the stock selecitons.
# Output the total cost of the purchased shares of stock to two decimal places.

stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

# %%
# 34.11 Dictionary conditional logic

# Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. 
# The following dictionary "purchase" lists available items as the key with the cost per item as the value.
# purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
# Additionally,

# If fewer than ten items are purchased, the price is the full cost per item.
# If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
# If twenty-one or more items are purchased, the purchase gets a 10% discount.
# Output the chosen item and total cost of the purchase to two decimal places.
# item_purchased $total_purchase_cost

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}


# %%
# 34.13 Manipulate CSV Files

# Creat a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values.
# Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified field.
# Output the file contents as two dictionaries

# %%
# 34.14 Math Module
# Create a solution that accepts an integer input. Import the built-in module "math" and use its factorial() method to calculate the factorial of the integer input.
# Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.

# factorial_value
# Boolean_value

#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100


# %%
# 34.15 Import custom module

# Create a solution that accpets an integer input representing the age of a pig.
# Import the existing module "pigAge" and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig.
# A year in a pig's life is equivalent to five years in a human's life. Output the human equivalent age of a pig.
# input_pig_age is converted_pig_age in human years




