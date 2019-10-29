def solution(n, lost, reserve):
    answer = n - len(lost)
        
    i = 0 # while 문을 위해 
    while i < len(reserve) : # for문을 할 경우, 삭제된 원소때문에 인덱스가 이상하게 된다.
        if reserve[i] in lost : 
            answer += 1
            lost.remove(reserve[i]) # lost도 삭제해서 아예 다음에 검사 안하도록
            reserve.remove(reserve[i]) # 삭제할경우 i 증가안함
        else : i += 1 # i 증가
          
    for i in lost : 
        for j in reserve : 
            if (j == i + 1) or (j == i - 1) : # 앞 뒤 사람에게 빌릴 수 있는가?
                answer += 1
                reserve.remove(j)
                break
            
    return answer