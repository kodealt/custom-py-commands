#python commands, by alt (アルト)
#do remember that all of this isnt sorted. i have made sure to include as many as possible, and somewhat modernized or simplified python, so its more like lolcode, but python. you can ctrl / command + f to search for the syntax. idk how to make this into a module :/

#define -  custom{
#print
def say(*args):
	arg = ' '.join(map(str, args))
	print(arg)
	
#length, same

#input
def ask(*args):
	arg = ' '.join(map(str, args))
	input(arg)

#float
def deci(num):
	return float(num)

#str, and int stays the same
#filetypes (open) stays the same
#sort says the same
#min, max, sum, list stays the same

#range
def to(min, max=None, step=1):
    if max is None:
        max = min
        min = 0
	max += 1
    return range(min, max, step)
#list functions (append, shift, insert, remove) stays the same

#(try, except, finally) stays the same
#math operators stay the same
#dict, iter, yield, lambada, with, as, logical ops, module operators stay the same. here is a example of how to use all(that i know) syntaxes in python below, in default python 3.x:

<--------------------------------------
# Comments
# This is a comment  # Single-line comment

"""
This is a multi-line comment
You can write multiple lines
"""

# Output
print("Hello, world!")  # Prints text to the console

# Input
input("Enter your name: ")  # Reads input from the user via the console

# Variables
x = 5  # Assigns a value to a variable

# Data Types
# Integers
x = 5

# Floats
x = 5.5

# Strings
x = "Hello"

# Lists
x = [1, 2, 3]

# Tuples
x = (1, 2, 3)

# Sets
x = {1, 2, 3}

# Dictionaries
x = {"a": 1, "b": 2}

# Booleans
x = True

# None
x = None

# Arithmetic Operators
+  # Addition
-  # Subtraction
*  # Multiplication
/  # Division
%  # Modulus (remainder)
**  # Exponentiation

# Comparison Operators
==  # Equal to
!=  # Not equal to
>  # Greater than
<  # Less than
>=  # Greater than or equal to
<=  # Less than or equal to

# Logical Operators
and  # Logical AND
or  # Logical OR
not  # Logical NOT

# Identity Operators
is  # Returns True if both variables are the same object
is not  # Returns True if both variables are not the same object

# Membership Operators
in  # Returns True if a value is present in a sequence
not in  # Returns True if a value is not present in a sequence

# Conditional Statements
if ...:  # Executes code block if a condition is true
elif ...:  # Additional condition(s) to check if the first condition is false
else:  # Executes if none of the above conditions are true

# Loops
for ... in ...:  # Iterates over elements of a sequence
while ...:  # Executes a block of code as long as a condition is true
break  # Terminates the loop
continue  # Skips the rest of the loop and continues with the next iteration

# Functions
def name(...):  # Defines a function
return ...  # Returns a value from a function

# Lambda Functions
lambda ...: ...  # Creates an anonymous function

# Classes
class ...:  # Defines a class

# Objects
object.method(...)  # Calls a method on an object

# Modules
import module_name  # Imports a module
from module_name import function_name  # Imports a function from a module
import module_name as alias_name  # Imports a module with an alias

# File Operations
open("file.txt", "r")  # Opens a file for reading

# Exception Handling
try:  # Tries a block of code for errors
except ...:  # Handles exceptions that occur in the try block
finally:  # Executes code regardless of whether an exception occurred

# Context Managers
with ... as ...:  # Manages resources (e.g., file handling) using a context manager

# Generators
yield  # Pauses a function's execution and yields a value to its caller

# Decorators
@decorator_name  # Modifies the behavior of a function or method

# String Formatting
f""  # String formatting using f-strings

# Indexing/Slicing
x[0]  # Accesses elements in a sequence by index
x[1:3]  # Slices a sequence

# Range
range(...)  # Generates a sequence of numbers

# Enumerate
enumerate(...)  # Returns an enumerate object containing index-value pairs

# Zip
zip(...)  # Combines elements from multiple iterables into tuples

# Map
map(function, iterable)  # Applies a function to all the items in an input list

# Filter
filter(function, iterable)  # Constructs an iterator from elements of an iterable for which a function returns true

# List Comprehensions
[expression for item in iterable if condition]  # Creates a new list based on existing iterables

# Set Comprehensions
{expression for item in iterable if condition}  # Creates a new set based on existing iterables

# Dictionary Comprehensions
{key_expression: value_expression for item in iterable if condition}  # Creates a new dictionary based on existing iterables

# Bitwise Operators
&  # Bitwise AND
|  # Bitwise OR
^  # Bitwise XOR
~  # Bitwise NOT
<<  # Left shift
>>  # Right shift

# Augmented Assignment Operators
+=  # Adds the right operand to the left operand and assigns the result to the left operand
-=  # Subtracts the right operand from the left operand and assigns the result to the left operand
*=  # Multiplies the right operand with the left operand and assigns the result to the left operand
/=  # Divides the left operand by the right operand and assigns the result to the left operand
%=  # Performs modulus on the left operand with the right operand and assigns the result to the left operand
**=  # Performs exponentiation on the left operand with the right operand and assigns the result to the left operand
//=  # Performs floor division on the left operand with the right operand and assigns the result to the left operand
&=  # Performs bitwise AND on the left operand with the right operand and assigns the result to the left operand
|=  # Performs bitwise OR on the left operand with the right operand and assigns the result to the left operand
^=  # Performs bitwise XOR on the left operand with the right operand and assigns the result to the left operand
<<=  # Performs left shift on the left operand with the right operand and assigns the result to the left operand
>>=  # Performs right shift on the left operand with the right operand and assigns the result to the left operand

# String Methods
.upper()  # Converts the string to uppercase
.lower()  # Converts the string to lowercase
.capitalize()  # Capitalizes the first character of the string
.title()  # Converts the first character of each word to uppercase
.strip()  # Removes leading and trailing whitespace from the string
.split()  # Splits the string into a list of substrings based on a delimiter
.join()  # Joins elements of an iterable (e.g., list) into a string using a delimiter
.format()  # Formats the string
.startswith()  # Checks if the string starts with a specified prefix
.endswith()  # Checks if the string ends with a specified suffix

# List Methods
.append()  # Adds an element to the end of the list
.extend()  # Extends the list by appending elements from another list
.insert()  # Inserts an element at a specified position in the list
.remove()  # Removes the first occurrence of a specified value from the list
.pop()  # Removes and returns the element at the specified position in the list
.index()  # Returns the index of the first occurrence of a specified value in the list
.count()  # Returns the number of occurrences of a specified value in the list
.sort()  # Sorts the list
.reverse()  # Reverses the elements of the list

# Dictionary Methods
.keys()  # Returns a view object of all keys in the dictionary
.values()  # Returns a view object of all values in the dictionary
.items()  # Returns a view object of all key-value pairs in the dictionary
.get()  # Returns the value associated with a specified key
.pop()  # Removes and returns the value associated with a specified key
.popitem()  # Removes and returns a key-value pair from the dictionary
.update()  # Updates the dictionary with key-value pairs from another dictionary

# Set Methods
.add()  # Adds an element to the set
.remove()  # Removes a specified element from the set
.discard()  # Removes a specified element from the set if it is present
.pop()  # Removes and returns an arbitrary element from the set
.clear()  # Removes all elements from the set
.union()  # Returns a new set containing all unique elements from two or more sets
.intersection()  # Returns a new set containing elements that are common to two or more sets
.difference()  # Returns a new set containing elements that are present in the first set but not in the second set
.symmetric_difference()  # Returns a new set containing elements that are present in either set, but not in both

---------------------------------------------------------------------------------------------------------------->


#alt~ 二千二十四 //alt out
