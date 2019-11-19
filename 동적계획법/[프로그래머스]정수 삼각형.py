# 위에서부터 진행하면 고려해야할 것이 많음으로, 아래에서부터 올라간다.

def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1) : # 아래에서부터 진행합니다
        for j in range(0, len(triangle[i])) : 
            triangle[i][j] += max(triangle[i + 1][j],  triangle[i + 1][j + 1]) # 값이 더 큰 걸 합해서 바꿔치기
                
    return triangle[0][0]