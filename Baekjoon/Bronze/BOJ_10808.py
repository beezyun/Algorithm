# https://www.acmicpc.net/problem/10808
# Bronze 4 알파벳 개수

word = input()

alphabet = {}
for x in range(ord('a'),  ord('z') + 1):
    alphabet[chr(x)] = 0

for w in word:
    alphabet[w] += 1
print(*alphabet.values())