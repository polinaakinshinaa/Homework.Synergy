# задание 1 
def palindrom(s):
  if s[::-1] == s:
    return True
  else:
    return False

text = input()
print(palindrom(text))
# задание 2
def reg(name, surname, middle_name, age):
    return f"{surname} {name} {middle_name} {age} г.р. зарегистрирован"

name = input()
surname = input()
middle_name = input()
age = int(input())
registration = reg(surname, name, middle_name, age)
print(registration)
# задание 3
def maximum(a, b = 0, c = 0):
    if (a >= b and a >= c):
        return a
    elif (b >= c):
        return b
    else:
        return c
