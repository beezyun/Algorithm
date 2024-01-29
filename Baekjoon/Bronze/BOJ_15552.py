# https://www.acmicpc.net/problem/15552
# Bronze 4 빠른 A+B

import sys

n = int(input())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)