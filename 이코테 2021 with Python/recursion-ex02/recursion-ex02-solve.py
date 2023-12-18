# 내 풀이 답안
def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

print(gcd(100, 24)) # 4
print(gcd(192, 162)) # 6
print(gcd(78696, 19332)) # 36