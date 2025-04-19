from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline

def bfs(graph, virus, comb, N, M):
    temp = copy.deepcopy(graph)

    for i, j in comb:
        temp[i][j] = 1

    queue = deque(virus)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2 
                queue.append((nx, ny))

    cnt = sum(row.count(0) for row in temp)
    return cnt

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

can_build = []
virus = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            can_build.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

result = []
for comb in combinations(can_build, 3):
    result.append(bfs(graph, virus, comb, N, M))

print(max(result))