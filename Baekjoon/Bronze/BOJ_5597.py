# https://www.acmicpc.net/problem/5597
# Bronze 5 과제 안 내신 분..?

arr = [i for i in range(1, 31)]

for _ in range(28):
    n = int(input())
    arr.remove(n)

for x in arr:
    print(x)
