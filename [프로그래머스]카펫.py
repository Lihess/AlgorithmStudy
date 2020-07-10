#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):    
    for i in range(yellow, 0, -1) : 
        if 2 * ((yellow / i) + i) + 4 == brown : 
        # 갈색이 테두리 1줄만 칠해져 있으므로, yellow를 통해 갈색 유추 가능@
            return [i + 2, (brown + yellow) // (i + 2)]