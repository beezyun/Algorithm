# 내 풀이 답안
n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
h = max(rice_cakes) - 1

for i in range(h, 0, -1):
    tmp = [
        r - i if r >= i else 0
        for r in rice_cakes
    ]
    # print("h : ", i, tmp)
    
    if sum(tmp) >= m:
        print(i)
        break