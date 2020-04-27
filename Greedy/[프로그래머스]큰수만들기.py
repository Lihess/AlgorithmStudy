# https://programmers.co.kr/learn/courses/30/lessons/42883#

def solution(number, k):
    i = 0
    
    while i < len(number) - 1  and k > 0 : 
        if number[i] < number[i + 1] : # 2개의 숫자를 순차적으로 비교해나간다.
            number = number[:i] + number[i + 1 :] 
            k -= 1
            if i != 0 : 
                i -= 1
        else : i += 1
            
    if k != 0: # 만약 K 만큼의 수를 제거하지 못했다면 마저 제거
        number = number[:-k]
        
    return number