# https://www.acmicpc.net/problem/2577
# Bronze 2 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

alphabet = {}
for i in range(10):
    alphabet[i] = 0

x = a * b * c
x = str(x)

for n in x:
    alphabet[int(n)] += 1
print(*alphabet.values(), sep = "\n")