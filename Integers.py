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

"""2.A program that will swap between 2 numbers, 
without a third number.
"""


def swap_numbers(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return f"num1 new value is {num1}, num2 new value is {num2}."

