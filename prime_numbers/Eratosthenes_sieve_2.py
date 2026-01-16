m, n = map(int, input().split()) # нахождение простых чисел на промежутке от m до n
f = False


for a in range(m, n + 1):
    if a < 2:
        continue
    p = True
    for b in range(2, int(a ** 0.5 + 1)):
        if a % b == 0:
            p = False
            break
    if p:
        print(a)
        f = True
if not f:
    print(0)