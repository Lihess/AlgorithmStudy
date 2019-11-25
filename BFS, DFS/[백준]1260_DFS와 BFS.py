N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M) : 
    link = list(map(int, input().split()))
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

def dfs(graph, start) : 
    visited = []
    queue = [start]

    while queue : 
        node = queue.pop(0)

        if node not in visited : 
            visited.append(node)
            queue += set(graph[node]) - set(visited)
    return visited

def bfs(graph, start) : 
    visited = []
    stack = [start]

    while stack : 
        print(stack)
        node = stack.pop()

        if node not in visited : 
            visited.append(node)
            stack += (set(graph[node]) - set(visited))
    return visited

print(*dfs(graph, start))     
print(*bfs(graph, start))            