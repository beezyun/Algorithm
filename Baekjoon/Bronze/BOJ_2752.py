# https://www.acmicpc.net/problem/2752
# Bronze 4 세수정렬

arr = list(map(int, input().split()))
arr.sort()

for a in arr:
    print(a, end = " ")