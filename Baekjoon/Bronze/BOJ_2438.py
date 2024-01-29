# https://www.acmicpc.net/problem/2438
# Bronze 5 별 찍기 - 1

n = int(input())

for i in range(1, n + 1):
    for _ in range(i):
        print("*", end="")
    print()