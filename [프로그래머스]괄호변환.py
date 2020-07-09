# https://programmers.co.kr/learn/courses/30/lessons/60058
# 문제에 나온 설명만 잘 따라가면 풀 수 있는 문제지만, 문제 이해하는 게 좀 오래걸렸다..


# 균형잡힌 문자열로 자르기 위한 함수
def balanced(p) : 
    balance = 0
    
    for i in range(len(p)) : 
        if p[i] == ')' :
            balance -= 1
        elif p[i] == '(' :
            balance += 1
            
        if balance == 0 :
            return i

# 올바른 문자열인지 환익
def is_right(s) : 
    temp = []
    
    for i in s : 
        if i == '(' : 
            temp.append(i)
        else :
            if len(temp) == 0 :
                return False
            temp.pop()

    if len(temp) != 0 :
        return False

    return True
    
# 재귀적으로 수행될 함수
def solution(p):
    if p == "" or is_right(p) :
        return p
    
    idx = balanced(p) + 1
    # balanced함수를 여러번 호출하면 최대 스택 호출 횟수를 추가하므로 idx 변수 선언
    u,v = p[:idx], p[idx:]

    if is_right(u) :
        return u + solution(v)
    else :
        temp = '(' + solution(v) + ')'
        u = list(u[1:-1])
        
        for i in range(len(u)) : 
            if u[i] == '(' :
                u[i] = ')'
            elif u[i] == ')' :
                u[i] = '('

        return temp + ''.join(u)