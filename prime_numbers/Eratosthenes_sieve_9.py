# Смежные простые числа-близнецы
from math import isqrt


def is_prime(a):
    return a > 1 and all(a % i != 0 for i in range(2, isqrt(a) + 1))


m, n = map(int, input().split())
gemini_numbers = []

for k in range(m, n + 1):
    if k + 2 <= n and is_prime(k) and is_prime(k + 2):
        gemini_numbers.append((k, k + 2))

print(*gemini_numbers if gemini_numbers else '0')