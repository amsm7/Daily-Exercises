""" 1.
A program that accepts three integers
and returns the largest number among them.
"""

def bigger_integer(num1, num2, num3):
    max_int = num1
    if num2 >= num1:
        max_int = num2
    if num3 >= max_int:
        max_int = num3

    return max_int

