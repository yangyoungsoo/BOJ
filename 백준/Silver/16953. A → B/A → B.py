from collections import deque

A, B = map(int, input().split())

def bfs(A, B):
    queue = deque([(A, 1)])
    visited = set()
    visited.add(A)

    while queue:
        x, count = queue.popleft()

        if x == B:
            return count

        nx1 = x * 2
        nx2 = x * 10 + 1

        if nx1 <= B and nx1 not in visited:
            visited.add(nx1)
            queue.append((nx1, count + 1))

        if nx2 <= B and nx2 not in visited:
            visited.add(nx2)
            queue.append((nx2, count + 1))

    return -1

print(bfs(A, B))
