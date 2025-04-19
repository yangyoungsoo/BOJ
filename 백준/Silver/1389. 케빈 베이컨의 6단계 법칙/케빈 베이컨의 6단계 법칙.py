from collections import deque

N, M = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    visited = [-1] * (N + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    total = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                total += visited[neighbor]
                queue.append(neighbor)

    return total

min_sum = float('inf')
answer = 0

for i in range(1, N + 1):
    s = bfs(i)
    if s < min_sum:
        min_sum = s
        answer = i

print(answer)
