# задание №1
summ = 0
n = int(input())
while(n > 0):
    x = n % 10
    n = n//10
    summ = summ + x
print(summ)
# задание №2
fact = 1
n = int(input())
while (n > 1):
    fact = fact * n
    n = n - 1
print(fact)
# задание №3
n = int(input())
for i in range(7, n):
    if i % 7 == 0:
     print(i + 7)
