# задание 1
n = int(input())
s = {}
for _ in range(n):
    r = input()
    if r in s:
        s[r] += 1
    else:
       s[r] = 1
x = 0
for value in s.values():
    if value > 1:
        x += 1
print(x)
# задание 2
def capitalize_text(text):
    result = ""
    capitalize_next = True
    for char in text:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char
        else:
            result += char
            if char in [".", "!", "?"]:
                capitalize_next = True
            elif char == " ":
                capitalize_next = True
    return result

input_text = input()
output_text = capitalize_text(input_text)
print(output_text)

# задание 3
def is_anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    count_str1 = {}
    count_str2 = {}

    for char in str1:
        if char in count_str1:
            count_str1[char] += 1
        else:
            count_str1[char] = 1

    for char in str2:
        if char in count_str2:
            count_str2[char] += 1
        else:
            count_str2[char] = 1
    return count_str1 == count_str2

input_str1 = input("Введите первую строку: ")
input_str2 = input("Введите вторую строку: ")

if is_anagram(input_str1, input_str2):
    print("Эти строки являются анаграммами!")
else:
    print("Эти строки не являются анаграммами.")
    
# задание 4
def find_students_solving_all(subject1, subject2, subject3):

    a_students = set(subject1.split())
    g_students = set(subject2.split())
    t_students = set(subject3.split())

    all_solving_students = a_students & g_students & t_students

    if all_solving_students:
        print(" ".join(sorted(all_solving_students)))
    else:
        print("Все три задачи никто не решил")

a_input = input("Фамилии учеников, решивших задачу по алгебре: ")
g_input = input("Фамилии учеников, решивших задачу по геометрии: ")
t_input = input("Фамилии учеников, решивших задачу по тригонометрии: ")

find_students_solving_all(a_input, g_input, t_input)
