# Basic Operators
# Learn to use the basic mathematical operators, +, -, *, /, // and **
#when we use / by default its type is float in python that is known as implicit typecasting
#int/int = float int / float = float & vice-versa
#but when we use // then it will give us a int result by default

# Priority is -> PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# 1. What is the output of this code?
# print(3 * 3 + 3 / 3 - 3)

# 2. Change the code so it outputs 3?
# print(3 * 3 + 3 / 3 - 3)
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# PEMDASLR Order LR MEANS LEFT TO RIGHT
# ()
# **  
# * OR /
# + OR -

# Outputs 7
print(3 * 3 + 3 / 3 - 3)

# Outputs 3
print(3 * 3 + 3 / 3 - 7) #done 7 instead of 3

# BMI Calculator
# The body mass index (BMI) is a measure used in medicine
# to see if someone is underweight or overweight. 
# This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the
# person's height squared.
# Convert this sentence into code
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight)/(height * height)

print(bmi)
