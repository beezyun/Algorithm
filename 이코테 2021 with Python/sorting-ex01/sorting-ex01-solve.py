# 내 풀이 답안
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)
# print(a)
# print(b)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

sum = 0
for i in range(n):
    sum += a[i]

print(sum)