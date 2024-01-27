# https://www.acmicpc.net/problem/1330
# Bronze 5 두 수 비교하기

a, b = map(int, input().split())

if a > b : print(">")
elif a < b : print("<")
else : print("==") # a = b
