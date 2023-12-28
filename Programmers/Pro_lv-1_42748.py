# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# Lv.1 K번째수

def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i = commands[x][0] - 1
        j = commands[x][1] - 1
        k = commands[x][2] - 1
        tmpArr = array[i:j + 1]
        tmpArr.sort()
        # print(tmpArr)
        answer.append(tmpArr[k])
    # print(answer)
    return answer