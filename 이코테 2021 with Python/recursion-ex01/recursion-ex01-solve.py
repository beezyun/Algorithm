# 내 풀이 답안
def factorial(n):
	# print('*', n)
	if n <= 1:
		return 1
    
	return factorial(n - 1) * n

print(factorial(int(input())))