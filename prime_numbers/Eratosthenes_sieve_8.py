# простые числа с возрастающими цифрами в числе
from math import isqrt


def is_prime(a):
    return a > 1 and all(a % i != 0 for i in range(2, isqrt(a) + 1))


m, n = map(int, input().split())
prime_w = []

for k in range(m, n + 1):
    s = str(k)
    s1 = ''.join(sorted([i for i in s]))
    if s == s1:
        if is_prime(k):
            prime_w.append(str(k))

print(prime_w if prime_w else 0)
