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

# # 답안 예시
# # 현재 나이트의 위치 입력 받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
# 	# 이동하고자 하는 위치 확인
# 	next_row = row + step[0]
# 	next_column = column + step[1]
# 	# 해당 위치로 이동이 가능하다면 카운트 증가
# 	if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
# 		result += 1

# print(result)


