# https://www.acmicpc.net/problem/2475
# Bronze 5 검증수

def check(arr):
    result = 0;

    for a in arr:
        result += pow(a, 2)
    result %= 10

    return result

serial = map(int, input().split())
print(check(serial))