# https://www.acmicpc.net/problem/5397
# Silver 2 키로거

import sys

n = int(sys.stdin.readline())
passwords = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    left_stack = []
    right_stack = []

    for w in word:
        if w == '<':
            if left_stack: # left_stack 이 비어있지 않으면
                right_stack.append(left_stack.pop())
        elif w == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif w == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(w)
    password = ''.join(left_stack + right_stack[::-1])
    passwords.append(password)

for password in passwords:
    print(password)