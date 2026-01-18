#  Простые числа с простой суммой цифр
from math import isqrt


def is_prime(a):
    return a > 1 and all(a % i != 0 for i in range(2, isqrt(a) + 1))


m, n = map(int, input().split())
prime_numbers = []

for k in range(m, n + 1):
    k_sum = sum([int(a) for a in str(k)])
    if is_prime(k) and is_prime(k_sum):
        prime_numbers.append(k)

print(*prime_numbers if prime_numbers else '0')