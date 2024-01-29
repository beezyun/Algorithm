# https://www.acmicpc.net/problem/9086
# Bronze 5 문자열

n = int(input())
word = []

for _ in range(n):
    word.append(input())

for w in word:
     print(w[0] + w[len(w) - 1])