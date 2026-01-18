# простые числа палиндромы
from math import isqrt


m, n = map(int, input().split())
palindrom_prime = []

for k in range(m, n):
    s = str(k)
    if s == s[::-1]:
        if all(k % i != 0 for i in range(2, isqrt(k) + 1)):
            palindrom_prime.append(s)

print(*palindrom_prime if palindrom_prime else 0)
