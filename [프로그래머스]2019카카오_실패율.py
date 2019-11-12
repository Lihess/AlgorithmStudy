def solution(N, stages):
    num = [] # 해당 스테이지에 머물러있는 사람의 수
    result = [] # 결과
    
    for i in range(1, N + 2) :
        num.append(stages.count(i)) # 머물러있는 사람을 저장
    
    for i in range(0, N) : 
        n = sum(num[i : N + 1]) # 해당  스테이지에 도달한 사람의 수
        if n > 0 : 
            fail = num[i] / n
            result.append([fail, i+1])
        else : result.append([0, i+1]) # n이 0이라면 실패율 0
            
    result.sort(key = lambda result : (-result[0], result[1])) # 실패율을 내림차순으로 정렬
    
    for i in range(0, N) : # 스테이지 번호만 뽑아냄
        result[i] = result[i][1]
        
    return result


#    denominator = len(stages)
#    for stage in range(1, N+1):
#        if denominator != 0:
#            count = stages.count(stage)
#            result[stage] = count / denominator
#            denominator -= count
# > 이처럼 전체 사람에서 앞 스테이징 머물러있는 사람을 빼는 방법도 좋은듯. 간단하다!