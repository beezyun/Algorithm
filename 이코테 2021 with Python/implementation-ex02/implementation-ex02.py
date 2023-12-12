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

# 답안 예시
