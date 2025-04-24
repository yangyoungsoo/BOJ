from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False for _ in range(F+1)]
graph = [0 for _ in range(F+1)]

def bfs(graph, visited, F,S,G,U,D):
    queue = deque([S])
    visited[S] = True

    d = [U,-1*D]

    while queue:
        cx = queue.popleft()
        
        if cx == G:
            return graph[cx]
    
        for i in range(2):
            nx = cx + d[i]

            if 1 <= nx <= F and visited[nx] == False and graph[nx] == 0:
                queue.append(nx)
                visited[nx] = True
                graph[nx] = graph[cx] + 1
    
    return "use the stairs"

print(bfs(graph, visited, F,S,G,U,D))