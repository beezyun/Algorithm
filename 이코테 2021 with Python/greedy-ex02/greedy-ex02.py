# 내 풀이 답안
n, k = map(int, input().split())
count = 0

while (n != 1):
    if (n % k == 0):
        n //= k
    else:
        n -= 1
    count += 1

print(count)

# # 답안 예시
# # N, K를 공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())
# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = (n // k) * k # N이 K로 나누어 떨어지는 N에서 가장 가까운 수 구하기
#     result += (n - target) # N에서 target가 될 때까지 1씩 빼기를 한 번에 카운트

#     # K로 나누기
#     n //= k
#     result += 1

#     # N이 K보다 작을 때(= 더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break

# # 마지막으로 남은 수에 대하여 1씩 빼기를 한 번에
# result += (n - 1)
# print(result)