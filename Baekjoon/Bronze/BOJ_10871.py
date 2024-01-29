# https://www.acmicpc.net/problem/10871
# Bronze 5 X보다 작은 수

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if x > i:
        print(i, end = " ")