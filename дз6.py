# -*- coding: utf-8 -*-
"""дз6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1KxTEGMgeU3UMm-CxUXOiL4b2ScKVJr
"""

def palindrom(s):
  if s[::-1] == s:
    return True
  else:
    return False

text = input()
print(palindrom(text))

def reg(name, surname, middle_name, age):
    return f"{surname} {name} {middle_name} {age} г.р. зарегистрирован"

name = input()
surname = input()
middle_name = input()
age = int(input())
registration = reg(surname, name, middle_name, age)
print(registration)

def maximum(a, b = 0, c = 0):
    if (a >= b and a >= c):
        return a
    elif (b >= c):
        return b
    else:
        return c