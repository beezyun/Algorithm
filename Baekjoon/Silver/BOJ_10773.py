# https://www.acmicpc.net/problem/10773
# Silver 4 제로

import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))