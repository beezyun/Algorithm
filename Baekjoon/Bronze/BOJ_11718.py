# https://www.acmicpc.net/problem/11718
# Bronze 5 그대로 출력하기

# answer 1
while True:
    try:
        print(input())
    except EOFError:
        break

# answer 2
# import sys
# word = sys.stdin.readlines()
# print(word.rstrip())