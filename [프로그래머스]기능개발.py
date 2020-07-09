# https://programmers.co.kr/learn/courses/30/lessons/42586
import math
import collections

def solution(progresses, speeds):
    day = [] # 소요되는 날짜
    
    for i in range(len(progresses)) : 
        day.append(math.ceil((100 - progresses[i]) / speeds[i])) # 올림을 이용하여 소요되는 날짜를 구함
        
        if i > 0 and day[i - 1] > day[i] : 
        # 만약 이전 기능보다 일찍 개발되어도 배포는 동일한 날짜에 되므로, 이전 기능의 날짜와 통일
            day[i] = day[i - 1]
            
    return list(collections.Counter(day).values()) 
    # collections.Counter은 해당 리스트의 모든 요소의 빈도수를 측정.
    # 이를 이용하여 같은 배포되는 기능의 갯수를 추출함