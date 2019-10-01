n =  input()
num = list(map(int, input().split()))
out = [0] * 23 # 학생이 23명

for i in range(1, 24) : # 23번까지 검사
    out[i - 1] = num.count(i)

for i in out : 
    print(i, end = ' ') # 전체 출력, 리스트 형태로 출력 안되도록
