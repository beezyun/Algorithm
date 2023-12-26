# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# Lv.2 타겟 넘버

count = 0

def solution(numbers, target):
    global count
    dfs(numbers, 0, target, 0)
    
    return count

def dfs(numbers, idx, target, total):
    global count
    
    if idx == len(numbers):
        if total == target:
            count += 1
        return
    
    dfs(numbers, idx + 1, target, total + numbers[idx])
    dfs(numbers, idx + 1, target, total - numbers[idx])