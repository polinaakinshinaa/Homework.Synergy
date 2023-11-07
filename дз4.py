# задание 1
s = "Death there mirth way the noisy merit"
print(s)
A = s.split()
print(A[::-1])
# задание 2
s = "In the hole in the ground there lived a hobbit"
print(s[0::2])
# задание 3
s = "3 5 -7 -13 43 8 0 -13 8 -1 2"
print(s)
A = s.split()
n = int(input())
for i in range(len(A)) :
      A[i] = int(A[i]) ** n
print(A)
# задание 4
s = str(input())
s.replace(s, 2 * s)
# задание 5
x = str(input())
y = str(input())
countx = len(x)
county = len(y)
print("x:", countx, "y:", county)
# задание 6 
s = "When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!"
result = ""
ids1 = s.find("(") 
while ids1 != -1:  
    ids2 = s.find(")", ids1)
    if ids2 != -1: 
        result += s[ids1 + 1: ids2]
    else: 
        break
    ids1 = s.find("(", ids2)
print(result) 
