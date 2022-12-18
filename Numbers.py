""" 1.
A program that accepts three number
and returns the largest number among them.
"""

def bigger_number(num1, num2, num3):
    max_int = num1
    if num2 >= num1:
        max_int = num2
    if num3 >= max_int:
        max_int = num3

    return max_int
---------------------------------------------------
"""2.
A program that will swap between 2 numbers, 
without a third number.
"""

def swap_numbers(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return f"num1 new value is {num1} and num2 new value is {num2}."
---------------------------------------------------
"""3.
A program that will swap between 2 numbers, 
with a third number.
"""

def swap_numbers2(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp

    return f"num1 new value is {num1} and num2 new value is {num2}."
---------------------------------------------------
"""4.
Write a program that receives a number and determines
 whether it is a prime number or not.
 """

import  math
def check_if_prime(num):
    if num < 2:
        print("Smaller than 2.")
        print("Not prime.")
        return False
    elif (num % 2 == 0) and (num != 2):
        print("Even number that isn't equal to 2.")
        print("Not prime.")
        return False
    elif 2 <= num <= 3:
        print("2 or 3.")
        print("Prime!")
        return True
    else:
        num_sqrt = math.floor(math.sqrt(num))
        for val in range(3, num_sqrt + 1, 2):
            if num % val == 0:
                print("Not prime.")
                return False

        print("Prime !")
        return True
        
