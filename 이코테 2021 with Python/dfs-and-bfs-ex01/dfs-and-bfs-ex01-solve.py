# 내 풀이 답안
# DFS
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False for col in range(m)] for row in range(n)]
count = 0;

def dfs(graph, a, b, visited):
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return
    
    if graph[a][b] == 0 and visited[a][b] == False:
        visited[a][b] = True
        dfs(graph, a - 1, b, visited) # 상
        dfs(graph, a + 1, b, visited) # 하
        dfs(graph, a, b - 1, visited) # 좌
        dfs(graph, a, b + 1, visited) # 우
        return True
    
    return False

for i in range(n):
    for j in range(m):
        if dfs(graph, i, j, visited) == True:
            # print(i, j)
            count += 1
print(count)