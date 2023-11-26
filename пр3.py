# задание 1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = int(input())
num2 = int(input())

result = lcm(num1, num2)
print(result)
# задание 2
def find_prime_numbers(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, n + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number * number, n + 1, number):
                is_prime[multiple] = False
    return primes
n = int(input())
prime_numbers = find_prime_numbers(n)
print(prime_numbers)
# задание 3
n = int(input())
for i in range(1,n):
    if n % i == 0:
     print(i)
