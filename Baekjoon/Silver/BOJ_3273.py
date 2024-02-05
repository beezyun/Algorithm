# https://www.acmicpc.net/problem/3273
# Silver 3 두 수의 합

import sys

size = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

count = 0
left = 0
right = size - 1

seq.sort()
# print(seq)
while left < right:
    tmp = seq[left] + seq[right]
    if tmp == x:
        count += 1
        left += 1
    elif tmp < x:
        left += 1
    else: # tmp > x
        right -= 1

print(count)