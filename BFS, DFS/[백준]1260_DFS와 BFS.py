N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 미리 행렬의 구조를 만들어 놓음

for i in range(M) : 
    link = list(map(int, input().split()))
    # 인접행렬이 아닌, 각 노드와 인접한 노드의 인덱스를 저장하는 방식
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])
    
for i in range(0, N + 1) : 
    graph[i].sort() # 작은 숫자의 노드가 우선되도록

def dfs(graph, start) : 
    visited = []
    queue = [start]

    while queue : # 큐가 비었다면
        node = queue.pop(0) # 선입선출

        if node not in visited : 
            visited.append(node) 
            for n in range(0,len(graph[node])) : 
                if graph[node][n] not in visited : # 인접한 노드가 방문한 노드가 아니라면
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

print(*dfs(graph, start)) # 리스트를 [] 기호 없이 출력
print(*bfs(graph, start))            