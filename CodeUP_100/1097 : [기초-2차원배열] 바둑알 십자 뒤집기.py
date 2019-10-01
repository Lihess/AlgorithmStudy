board = []

for i in range(0, 19) : # 19 x 19 바둑판
    board.append(list(map(int, input().split()))) 

n = input()

for m in range(0, int(n)) : # n번 반복
    x, y = map(int, input().split()) # x, y 좌표 받기
    for i in range(0, 19) : board[x - 1][i] = int(not bool(board[x - 1][i])) # 반전!
    for j in range(0, 19) : board[j][y - 1] = int(not bool(board[j][y - 1]))

for i in range(0, 19) :
    for j in range(0, 19) : 
         print(board[i][j], end = ' ')
    print()
