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

# # 답안 예시
# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
    
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)