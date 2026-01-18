# простые числа Софи Жермен
from math import isqrt


def is_prime(a):
    return a > 1 and all(a % i != 0 for i in range(2, isqrt(a) + 1))


m, n = map(int, input().split())
jermen_prime = []

for k in range(m, n + 1):
    if is_prime(k) and is_prime(2 * k + 1):
            jermen_prime.append(k)

print(*jermen_prime if jermen_prime else 0)
