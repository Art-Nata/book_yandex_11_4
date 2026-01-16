N = 50 # простой алгоритм для нахождения простых чисел от 1 до N
A = [True] * (N + 1)
c = 2

while c * c <= N:
    if A[c]:
        i = c * c
        while i <= N:
            A[i] = False
            i += c
    c += 1

for i in range(2, N + 1):
    if A[i]:
        print(i)