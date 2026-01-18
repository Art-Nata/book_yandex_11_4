# простые числа с чётной суммой цифр
from math import isqrt


m, n = map(int, input().split())

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, isqrt(x) + 1))
result = [str(x) for x in range(m, n + 1) if is_prime(x) and sum(int(a) for a in str(x)) % 2 == 0]

print(*result if result else 0)
