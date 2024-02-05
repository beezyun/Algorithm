# https://www.acmicpc.net/problem/1475
# Silver 5 방 번호

room = input()
check = [0 for i in range(10)]

for r in room:
    num = int(r)
    if num == 6 or num == 9:
        if check[6] <= check[9]:
            check[6] += 1
        else:
            check[9] += 1
    else:
        check[num] += 1

# print(check)
print(max(check))