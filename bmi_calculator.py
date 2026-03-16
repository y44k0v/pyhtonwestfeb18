"""
Welcome to the Body Mass Index (BMI) Calculator project!

Your task is to implement a function called 'calculate_bmi' that takes
a person's weight in kilograms and height in meters as input, and
returns their BMI.

Here's the formula you'll need:
BMI = weight (kg) / (height (m) * height (m))

Let's break it down:
1.  **weight (kg):** This is the person's weight in kilograms.
2.  **height (m):** This is the person's height in meters.
3.  **height (m) * height (m):** This means height squared.

Your 'calculate_bmi' function should:
-   Accept two arguments: `weight_kg` (a float or int) and `height_m` (a float or int).
-   Return the calculated BMI as a float.
-   Consider edge cases: What if height is zero or negative? How should your function handle that?
    (Hint: You might want to return a specific value or raise an error for invalid inputs.)

Good luck!
"""

def calculate_bmi(weight_kg, height_m):
    if height_m <= 0 or weight_kg < 0:
        return None
    
    bmi = weight_kg / (height_m ** 2)
    
    return bmi