# 내 풀이 답안
str = input()
result = int(str[0])

for s in str[1:]:
    i = int(s)

    # print(result, end = " ")
    if (result <= 1 or i <= 1):
        result += i
        # print("+", i, end = " ")
    else:
        result *= i
        # print("*", i, end = " ")
    # print(result)

print(result)