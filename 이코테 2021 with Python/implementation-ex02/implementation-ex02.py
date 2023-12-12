# 내 풀이 답안
n = int(input())
hour = 0
minute = 0
second = 0
result = 0

for i in range((n * 3600) + (59 * 60) + 59):
	h = str(hour)
	m = str(minute)
	s = str(second)
	
	if ('3' in h) or ('3' in m) or ('3' in s):
		result += 1
		
	second += 1
	
	if second == 60:
		second = 0
		minute += 1
	if minute == 60:
		minute = 0
		hour += 1

print(result)

# # 답안 예시
# # H 입력 받기
# h = int(input())

# count = 0

# # i: 시, j: 분, k: 초
# for i in range (h + 1):
# 	for j in range(60):
# 		for k in range(60):
# 			# 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
# 			if '3' in str(i) + str(j) + str(k):
# 				count += 1

# print(count)