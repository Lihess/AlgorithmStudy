n =  input()
point = []

for i in range(0, int(n)) : 
    point.append(list(map(int, input().split()))) # 2차 리스트 형태로 받아서 저장
    
for i in range(1, 20) : 
    for j in range(1, 20) : 
        if point.count([i, j]) != 0 : print(1, end = ' ') # 해당 리스트를 찾을 수 있다면 1 출력
        else : print(0, end = ' ') # 아니면 0 출력
    print() # 개행
