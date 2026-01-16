def is_prime(a): # функция отдельно отрабатывает чётные числа

    if a < 2:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for b in range(2, int(a ** 0.5 + 1), 2):
        if a % b == 0:
            return False
    return True


m, n = map(int, input().split()) # нахождение простых чисел на промежутке от m до n с функцией
result = []

for x in range(m, n + 1):
    if is_prime(x):
        result.append(str(x))
if result:
    print(*result)
else:
    print(0)
