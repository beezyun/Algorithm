# https://www.acmicpc.net/problem/2744
# Bronze 5 대소문자 바꾸기

str = input()
result = ""

for s in str:
    if s.isupper():
        result += s.lower()
    else: # s.islower():
        result += s.upper()

print(result)