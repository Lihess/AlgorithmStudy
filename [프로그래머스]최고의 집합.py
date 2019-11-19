# 합 S를 n으로 나누었을 때, 나머지를 어떻게 분배할 건지 잘 생각해야 한다
# 한 원소에 나머지를 모두 몰아주는 것보다, 골고루 나머지를 분산하여 더해주는 것이 곱했을 때 더 큰 값이 나옴
def solution(n, s):
    answer = []
    div, remainder = divmod(s, n) # 몫과 나머지를 구함
    
    if div == 0 : # 몫이 0이라면, 곱이 최대가 될 수 없음
        answer.append(-1)
    else :
        for i in range(0, n - remainder) : 
            answer.append(int(div)) 
        for i in range(0, remainder) :  # 나머지 수만큼 1을 더한 원소를 삽입
            answer.append(int(div) + 1)
    
    return answer