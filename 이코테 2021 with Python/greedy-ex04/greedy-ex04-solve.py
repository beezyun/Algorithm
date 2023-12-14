# 내 풀이 답안
num = int(input())
fear = list(map(int, input().split()))

group = 0
member = 0

# 공포도를 내림차순으로 정렬
fear.sort()

for i in fear:
    member += 1
    if member >= i:
        group += 1
        member = 0

print(group)