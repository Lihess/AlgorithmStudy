w, h = map(int, input().split())
board = [[0] * h for i in range(w)]
# 평소에 배열을 미리 생성할때 [0] * h 이런 방식으로 해서 [[0] * h] * w 이런 방식으로 배열을 생성하려고 함
# 근데 이상하게 결과값에 계속 내가 1로 지정하지 않은거도 1로 나옴
# 이를 저런 식으로 변경하니 잘 되었다!!
# 아마 n 차원 배열에서는 저게 잘 안되는 듯하다..
n = int(input())

for i in range(0, n) : 
    l, d, x, y = map(int, input().split())

    for j in range(0, l) : 
        if d == 0 : board[x - 1][y - 1 + j] = 1
        elif d == 1 : board[x - 1 + j][y - 1] = 1
        
for i in range(0, w) :
    for j in range(0, h) :
        print(board[i][j], end = ' ')
    print()
