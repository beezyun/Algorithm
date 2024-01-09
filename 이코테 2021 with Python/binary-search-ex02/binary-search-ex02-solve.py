# 내 풀이 답안
def return_left_index(array, start, end, value):
    while start < end:
        mid = (start + end) // 2

        if array[mid] >= value:
            end = mid
        else: # array[mid] < value:
            start = mid + 1;
    
    return end

def return_right_index(array, start, end, value):
    while start < end:
        mid = (start + end) // 2

        if array[mid] > value:
            end = mid
        else: # array[mid] <= value:
            start = mid + 1;
    
    return end

def countValue(array, value):
    right_index = return_right_index(array, 0, n - 1, value)
    left_index = return_left_index(array, 0, n - 1, value)
    
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

if countValue(array, x) == None:
    print(-1)
else:
    print(countValue(array, x))