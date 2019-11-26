# x, y의 좌표를 잘 구분할 것
# 원래는 for문이 위에서 아래로, 왼쪽에서 오른쪽으로 향하기 때문에 우, 하만 점검하면 된다고 생각했으나
#   1 
# 1 1 1
#   1    와 같은 경우, 올바르게 수행되지 않음!

import sys
sys.setrecursionlimit(1000000) # 스택 제한을 없애기 위함

def dfs(x, y) : # 깊이 우선 탐색으로 구현
    land[y][x] = 0 # 방문한 곳은 0으로 하여, 다시 탐색하지 않도록
    
    for k in range(4) : 
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < M and 0 <= ny < N and land[ny][nx] == 1) :
            dfs(nx, ny)

test = int(input())

for _ in range(test) :
    M, N , K = map(int, input().split())
    land = [[0] * M for _ in range(N)]

    for _ in range(K) : 
        x, y = map(int, input().split())
        land[y][x] = 1

    dx = [1, -1, 0, 0] # 4가지의 경우의 수
    dy = [0, 0, 1, -1]

    num = 0
    for y in range(N) :
        for x in range(M) : 
            if land[y][x] == 1 :  
                dfs(x, y)
                num += 1
    print(num)