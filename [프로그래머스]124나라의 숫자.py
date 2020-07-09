# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    
    while n > 0 : 
        r = n % 3
        n = n // 3

        if r == 0 : # 나머지가 0일 경우 n - 1
            n -= 1
            
        answer = {1 : '1', 2 : '2', 0 : '4'}[r] + answer
        # {1 : '1', 2 : '2', 0 : '4'}[r] : 딕셔너리를 이용한 유사 switch문
    return answer

# 다른 사람의 코드
# def change124(n):
#     num = ['1','2','4']
#     answer = ""
# 
# 
#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3
# 
#     return answer
# >> 미리 정의된 list를 활용하여!