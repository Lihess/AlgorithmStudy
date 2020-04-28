# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3
# 프림 알고리즘을 기반으로 해결함

def solution(n, costs):
    costs.sort(key = lambda costs: costs[2]) # 처음 연결할 섬들을 지정하기 위해서

    # 간선의 비용이 가장 적은 두개의 섬을 처음 연결
    # set을 이용하여 중복이 발생하지 않도록 함
    visited = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    
    while len(visited) != n :
        minCost = 10000
        num = 0
        
        for i in range(len(costs)) : 
            if costs[i][0] in visited or costs[i][1] in visited : # 반드시 한 섬은 이전에 연결된 섬이여야 함
                if costs[i][0] in visited and costs[i][1] in visited : # 만약 이미 연결된 섬이라면 넘어감
                    continue
                if minCost > costs[i][2] : # 새롭게 연결될 섬들 중 비용이 가장 작은 경우를 찾아서 연결
                    minCost = costs[i][2]
                    num = i

        answer += minCost
        visited.update([costs[num][0], costs[num][1]])
        costs.pop(num) # costs 내에서의 검색의 시간을 줄이기 위해서
        
    return answer