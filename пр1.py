# задание 1
A = [2, 4, 100, 12, 9, 6]
B = [3, 5, 2, 14, 9, 24]
print(list(map(lambda x, y: x + y, A , B)))
# задание 2
A = [2, 4, 19, 38, 57, 36, 34, 876, 48, 6, 13, 26, 39]
result = list(filter(lambda x: (x % 19 == 0) or (x % 13 == 0), A))
print(result)
# задание 3
from functools import reduce
max_number = reduce(lambda x, y: x if x > y else y, [4, 8, 2, 10, 20, 65, 5])
print(max_number)
