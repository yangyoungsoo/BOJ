from collections import deque
import sys

input = sys.stdin.readline

def bfs(building, start, end, L, R, C):
    dz = [0, 0, 0, 0, -1, 1]
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]

    queue = deque()
    queue.append((*start, 0))
    visited[start[0]][start[1]][start[2]] = True

    while queue:
        z, x, y, dist = queue.popleft()
        if (z, x, y) == end:
            return f"Escaped in {dist} minute(s)."
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny, dist + 1))
    return "Trapped!"

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = end = None

    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input().strip())
            for c in range(C):
                if row[c] == 'S':
                    start = (l, r, c)
                elif row[c] == 'E':
                    end = (l, r, c)
            floor.append(row)
        building.append(floor)
        input() 

    print(bfs(building, start, end, L, R, C))
