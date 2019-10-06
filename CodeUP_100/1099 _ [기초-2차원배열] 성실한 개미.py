board = []

for i in range(0, 10) : # 입력받은 대로 맵 형성
    board.append(list(map(int,input().split())))

i = 1 # 시작점
j = 1 # 시작점
    
while 1 : 
    if board[i][j] == 0:
        board[i][j] = 9
    elif board[i][j] == 2 : 
        board[i][j] = 9
        break
    else : break
    
    if board[i][j + 1] != 1: # 오른쪽에 0, 2가 올 수 있다는 것을 잘 확인할 것.
        j = j + 1
    else: 
        i = i + 1

for i in range(0, 10) :
    for j in range(0, 10) :
        print(board[i][j], end = ' ')
    print()
