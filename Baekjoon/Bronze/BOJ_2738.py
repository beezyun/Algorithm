# https://www.acmicpc.net/problem/2738
# Bronze 5 행렬 덧셈

n, m = map(int, input().split())
a = []
b = []

# 행렬 a 입력
for i in range(n):
    a.append(list(map(int, input().split())))

# 행렬 b 입력
for i in range(n):
    b.append(list(map(int, input().split())))

# 행렬 a, b의 합 출력
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = " ")
    print()