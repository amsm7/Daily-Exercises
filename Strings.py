
""" 1.
A program that removes given character from a given string.
"""

def remove_character(my_str, my_char):
    new_str = my_str.replace(my_char, '')
    return new_str

---------------------------------------------------
""" 2.
A program that will count the # of occurrences of a given
char on a given string.
"""

def count_char(my_str, my_char):
    cnt = my_str.count(my_char)
    return f"'{my_char}' has {cnt} occurrences in '{my_str}'."

---------------------------------------------------
""" 3.
A program that will check if 2 given strings are 'Anagram'.
"""

def check_anagram(str1, str2):
    new_str1 = str1.lower().replace("", " ")
    new_str1 = new_str1.split()
    new_str1 = ''.join(sorted(new_str1))

    new_str2 = str2.lower().replace("", " ")
    new_str2 = new_str2.split()
    new_str2 = ''.join(sorted(new_str2))

    return new_str1 == new_str2

---------------------------------------------------
""" 4.
"""
