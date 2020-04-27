# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    name = list(map(lambda x : min(ord(x) - 65, 26 - (ord(x) - 65)), name))
    # 주어진 이름을 아스크코드를 이용하여 A에서부터 최소 이동횟수로 변환
    # 해당 알파벳이 A에보다 Z에 더 가까이 있는 알파벳이라면 "26 - x"로 하여 이동횟수를 계산함
    i = 0

    while True : 
        answer += name[i]
        name[i] = 0
        
        if sum(name) == 0 :
        # A가 아닌 모든 알파벳을 검사한 경우 
            break
        
        left, right = (1, 1)
        
        # 왼쪽, 오른쪽 중 A가 아닌 다른 알파벳을 만나기까지의 거리 계산
        while name[i - left] == 0 :
            left += 1
        while name[i + right] == 0 :
            right += 1
        
        # 왼쪽, 오른쪽 중 짧은 거리인 방향을 기준으로 answer과 i의 값 갱신
        answer += left if left < right else right
        i += -left if left < right else right
  
    return answer