# You can put if/else statements inside other if/else statements.
# This is known as nesting. e.g.
# if maths_score >= 90:
#     if english_score >= 90:
#         print("You're good at everything")
#     else:
#         print("You're good at maths")
# if english_score >= 90:
#     print("You're good at english)
# In this case only when a student has over 90 on maths
# and english, do they get "You are good at everything".

# Note: You can also have if statements that
# don't have a paired else statement.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("")
    
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age <= 21:
        print("Please pay $12.")
    else:
        print("Please pay $20.")
else:
    print("Sorry you have to grow taller before you can ride.")
    
#Problem 1
# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator
# so that it interprets the BMI values calculated.

# If the bmi is under 18.5 (not including),
# print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including),
# print out "normal weight"

# If the bmi is 25 (including) or over,
# print out "overweight"

# 🚨 Do not modify the values above
# Write your code below 👇
weight = 85
height = 1.85
 
bmi = weight / (height ** 2)
 
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
