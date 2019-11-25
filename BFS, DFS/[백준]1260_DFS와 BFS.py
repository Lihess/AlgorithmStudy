N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M) : 
    link = list(map(int, input().split()))
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])
    
for i in range(0, N + 1) : 
    graph[i].sort()

def dfs(graph, start) : 
    visited = []
    queue = [start]

    while queue : 
        node = queue.pop(0)

        if node not in visited : 
            visited.append(node) 
            for n in range(0,len(graph[node])) : 
                if graph[node][n] not in visited : 
                    queue.append(graph[node][n])
    return visited

def bfs(graph, start) : 
    visited = []
    stack = [start]

    while stack : 
        print(stack)
        node = stack.pop()

        if node not in visited : 
            visited.append(node) 
            for n in range(len(graph[node]) - 1, -1, -1) : 
                if graph[node][n] not in visited : 
                    stack.append(graph[node][n] )
    return visited

print(*dfs(graph, start))     
print(*bfs(graph, start))            