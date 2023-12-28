# 내 풀이 답안
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False for col in range(m)] for row in range(n)]
distance = 0

def bfs(graph, x, y, visited, distance):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    
    if graph[x][y] == 1 and visited[x][y] == False:
        visited[x][y] = True
        graph[x][y] += distance
        distance += 1

        bfs(graph, x - 1, y, visited, distance) # 상
        bfs(graph, x + 1, y, visited, distance) # 하
        bfs(graph, x, y - 1, visited, distance) # 좌
        bfs(graph, x, y + 1, visited, distance) # 우

bfs(graph, 0, 0, visited, distance)
print(graph[n - 1][m - 1])
# for i in range(n):
#     print(graph[i])