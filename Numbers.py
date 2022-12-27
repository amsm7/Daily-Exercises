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
""" 2.
A program that will swap between 2 numbers, 
without a third number.
"""

def swap_numbers(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return f"num1 new value is {num1} and num2 new value is {num2}."

---------------------------------------------------
""" 3.
A program that will swap between 2 numbers, 
with a third number.
"""

def swap_numbers2(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp

    return f"num1 new value is {num1} and num2 new value is {num2}."

---------------------------------------------------
""" 4.
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
        for val in range(3, (num + 1)//2, 2):
            if num % val == 0:
                return False
        return True
    
---------------------------------------------------
""" 5.
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
""" 6.
Write a program that will check if a given number is palindorm or not.
 """

def reverse_int(num):
    pal_num = num
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
    return pal_num == reversed_num

 ---------------------------------------------------  
""" 7.
Write a program that will check if a given number is armstrong number or not.
Armstrong number is number which is equal to the sum of his digits raised to the power of three.
For example: 371 , 153.  153 : 1^3 = 1, 5^3 = 125, 3^3 = 27. 1+125+27 = 153
"""

def check_if_arm(num):
    check_arm = 0
    check_num = num

    while num != 0:
        check_arm += (num % 10) ** 3
        num = num // 10

    return check_num == check_arm

 ---------------------------------------------------  
""" 8.
Write a program that prints a fibonacci series according a given length number.
"""

def check_fib(num):
    val_1 = 0
    val_2 = 1
    total = 0

    for i in range(0, num):
        if i <=1:
            total = i
        else:
            total = val_1 + val_2
            val_1 = val_2
            val_2 = total
        print(total)
        
---------------------------------------------------  
""" 9.
Write a program that checks if a given number is binary or not.
"""

def check_if_binary(num):
    while not(1 >= num >= 0):
        if (num % 10 != 1) and (num % 10 != 0):
            return False
        num = num // 10
    return True 

---------------------------------------------------  
""" 10.
Write a program that checks if a given number is perfect or not.

* Perfect number is a number that equals to the sum of all of it's factors.
  The number and it's factors should be all positive numbers.
"""

def perfect_number(num):
    total = 0
    if num < 0:
        return False
    for val in range(1, ((num + 2) // 2)):
        if num % val == 0:
            total += val

    return total == num

---------------------------------------------------  
""" 11.
Write a program that finds the average of given numbers.
"""

def calc_avg(*args):
    total = sum([val for val in args])
    print(total)
    print(len(args))d
    return total / len(args)

---------------------------------------------------  
""" 12.
Write a program that calculates the factorial of a given number.
"""

def factorial(num):
    total = 1
    for val in range(1, num+1):
        total *= val
    return total

