from collections import deque

M, N, H = map(int, input().split())

graph = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    graph.append(layer)

starts = []
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1:
                starts.append((k, i, j))

def bfs(graph, starts, H, N, M):
    queue = deque(starts)
    days = [[[-1] * M for _ in range(N)] for _ in range(H)]

    for z, x, y in starts:
        days[z][x][y] = 0

    dx = [0, 0, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [-1, 1, 0, 0, 0, 0]

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if graph[nz][nx][ny] == 0 and days[nz][nx][ny] == -1:
                    graph[nz][nx][ny] = 1
                    days[nz][nx][ny] = days[z][x][y] + 1
                    queue.append((nz, nx, ny))

    max_days = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if graph[k][i][j] == 0 and days[k][i][j] == -1:
                    return -1
                max_days = max(max_days, days[k][i][j])

    return max_days

print(bfs(graph, starts, H, N, M))
