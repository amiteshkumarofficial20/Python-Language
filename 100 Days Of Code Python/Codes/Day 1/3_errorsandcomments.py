# =========================================================
# PYTHON ERRORS AND COMMENTS - COMPLETE NOTES
# =========================================================


# ---------------------------------------------------------
# 1. ERRORS IN PYTHON
# ---------------------------------------------------------
# An error is a problem in a program that stops execution
# or produces incorrect output.

# Types of Errors in Python:
# 1. Syntax Error
# 2. Runtime Error (Exceptions)
# 3. Logical Error



# =========================================================
# 2. SYNTAX ERROR
# =========================================================
# Occurs when Python grammar rules are broken.
# The interpreter cannot understand the code.

# Example
# print("Hello"

# Causes:
# - Missing brackets
# - Missing colon :
# - Incorrect indentation
# - Spelling mistakes in keywords

# Example
# if x > 10
#     print("Hello")



# =========================================================
# 3. RUNTIME ERRORS (EXCEPTIONS)
# =========================================================
# Runtime errors occur while the program is running.


# ---------------------------------------------------------
# NameError
# ---------------------------------------------------------
# Occurs when a variable is used before it is defined.

# Example
# print(age)



# ---------------------------------------------------------
# TypeError
# ---------------------------------------------------------
# Occurs when an operation is performed on incompatible data types.

# Example
# print("Age: " + 20)



# ---------------------------------------------------------
# ValueError
# ---------------------------------------------------------
# Occurs when a function receives the correct type but invalid value.

# Example
# int("hello")



# ---------------------------------------------------------
# ZeroDivisionError
# ---------------------------------------------------------
# Occurs when dividing a number by zero.

# Example
# print(10 / 0)



# ---------------------------------------------------------
# IndexError
# ---------------------------------------------------------
# Occurs when accessing an index that does not exist in a list.

# Example
# numbers = [1,2,3]
# print(numbers[5])



# ---------------------------------------------------------
# KeyError
# ---------------------------------------------------------
# Occurs when accessing a key that does not exist in a dictionary.

# Example
# data = {"name": "Amit"}
# print(data["age"])



# ---------------------------------------------------------
# AttributeError
# ---------------------------------------------------------
# Occurs when an object does not have the attribute or method used.

# Example
# x = 10
# x.append(5)



# ---------------------------------------------------------
# ImportError
# ---------------------------------------------------------
# Occurs when Python cannot import a module.

# Example
# import nonexistingmodule



# ---------------------------------------------------------
# ModuleNotFoundError
# ---------------------------------------------------------
# Occurs when the module cannot be found.

# Example
# import random123



# ---------------------------------------------------------
# IndentationError
# ---------------------------------------------------------
# Occurs when indentation is incorrect.

# Example
# if True:
# print("Hello")



# ---------------------------------------------------------
# FileNotFoundError
# ---------------------------------------------------------
# Occurs when trying to open a file that does not exist.

# Example
# open("data.txt")



# ---------------------------------------------------------
# OverflowError
# ---------------------------------------------------------
# Occurs when a calculation exceeds the maximum limit.

# Example
# import math
# math.exp(1000)



# ---------------------------------------------------------
# MemoryError
# ---------------------------------------------------------
# Occurs when the program runs out of memory.



# ---------------------------------------------------------
# RecursionError
# ---------------------------------------------------------
# Occurs when maximum recursion depth is exceeded.



# =========================================================
# 4. LOGICAL ERROR
# =========================================================
# Logical errors occur when the program runs successfully
# but produces incorrect results.

# Example
# a = 10
# b = 5
# print(a - b)
# If the programmer wanted addition, the output will be wrong.



# =========================================================
# COMMENTS IN PYTHON
# =========================================================


# ---------------------------------------------------------
# 1. SINGLE LINE COMMENT
# ---------------------------------------------------------
# Single line comments start with #

# Example
# print("Hello")



# ---------------------------------------------------------
# 2. INLINE COMMENT
# ---------------------------------------------------------
# Inline comments are written on the same line as code.

# Example
# x = 10  # storing value in x



# ---------------------------------------------------------
# 3. MULTI-LINE COMMENT
# ---------------------------------------------------------
# Python uses triple quotes for multi-line comments.

'''
This is a
multi line
comment
'''

"""
This is also
a multi line
comment
"""