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
        return False
    elif (num % 2 == 0) and (num != 2):
        return False
    elif 2 <= num <= 3:
        return True
    else:
        num_sqrt = math.floor(math.sqrt(num))
        for val in range(3, num_sqrt + 1, 2):
            if num % val == 0:
                return False
        return True
---------------------------------------------------
"""5.
Write a program that will reverse the order of a given integer.
 """

def reverse_int(num):
    check_num = num
    num_len = 0
    reversed_num = 0
    while check_num != 0:
        num_len += 1
        check_num = check_num // 10
    while num != 0:
        reversed_num += (num % 10) * (10 ** (num_len - 1))
        num = num // 10
        num_len -= 1
    return reversed_num
 ---------------------------------------------------  
