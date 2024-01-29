# https://www.acmicpc.net/problem/10950
# Bronze 5 A+B - 3

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)