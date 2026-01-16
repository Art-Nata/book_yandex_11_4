def is_prime(a):
    if a < 2:
        return  False
    for b in range(2, int(a ** 0.5 + 1)):
        if a % b == 0:
            return False
    return True


m, n = map(int, input().split()) # нахождение простых чисел на промежутке от m до n с функцией
f = False

for a in range(m, n + 1):
    if is_prime(a):
        print(a)
        f = True
if not f:
    print(0)
