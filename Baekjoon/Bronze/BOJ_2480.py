# https://www.acmicpc.net/problem/2480
# Bronze 4 주사위 세개

a, b, c = map(int, input().split())
prize = 0

if a == b == c:
    prize = 10000 + (a * 1000)
elif a == b:
    prize = 1000 + (a * 100)
elif b == c:
    prize = 1000 + (b * 100)
elif c == a:
    prize = 1000 + (c * 100)
else:
    prize = max(a, b, c) * 100

print(prize)