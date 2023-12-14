# 내 풀이 답안
str = input()
x = int(str[1])
y = int(ord(str[0])) - 96
result = 0

# 8가지 이동 지점
# LLU, LLD, RRU, RRD
# UUL, UUR, DDL, DDR
dx = [[0, 0, -1], [0, 0, 1], [0, 0, -1], [0, 0, 1],
	  [-1, -1, 0], [-1, -1, 0], [1, 1, 0], [1, 1, 0]]

dy = [[-1, -1, 0], [-1, -1, 0], [1, 1, 0], [1, 1, 0],
	  [0, 0, -1], [0, 0, 1], [0, 0, -1], [0, 0, 1]]

for i in range(len(dy)):
	# x, y 나이트 현재 위치 입력값으로 초기화
	x = int(str[1])
	y = int(ord(str[0])) - 96

	for j in range(len(dy[i])):
		x = x + dx[i][j]
		y = y + dy[i][j]
		# print(x, y)

	if x < 1 or y < 1 or x > 8 or y > 8:
		# print('pass')
		continue
	
	# print('count')
	result += 1

print(result)


