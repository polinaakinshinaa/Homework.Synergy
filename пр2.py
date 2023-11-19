# задание 1
def maximum_number(n):
    if len(n) == 1:
        return n[0]
    else:
        max_rest = maximum_number(n[1:])
        if n[0] > max_rest:
            return n[0]
        else:
            return max_rest

n = [3, 8, 1, 10, 5]
m_n = maximum_number(n)
print(m_n)
