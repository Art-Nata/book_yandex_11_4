# не решено
#  Простые числа с простой суммой цифр
from math import isqrt


def is_prime(a):
    return a > 1 and all(a % i != 0 for i in range(2, isqrt(a) + 1))


u, v = map(int, input().split())
l = int(input())
prime_numbers_l = []

for k in range(u, v + 1):

    for i in range(2, k // l + 1):
        s = []
        for t in range(l):
            if is_prime(k + i * t):
                s.append(str(k + i * t))
        if len(s) == l:
            prime_numbers_l.append(' '.join(s))

print(*prime_numbers_l if prime_numbers_l else '0')