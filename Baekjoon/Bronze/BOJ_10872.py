# https://www.acmicpc.net/problem/10872
# Bronze 5 팩토리얼

n = int(input())

result = 1
for i in range(1, n + 1):
    result *= i

print(result)
