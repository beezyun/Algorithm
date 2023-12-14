# 내 풀이 답안
input = input()
str = []
num = 0

for i in input:
    if i >= 'A' and i <= 'Z':
        # print(i)
        str.append(i)
    else:
        num += int(i)

str.sort()
for s in str:
    print(s, end = "")
if num != 0:
    print(num)