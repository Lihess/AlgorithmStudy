n = int(input()) # 입력받을 수 
time = [] # 회의 시간
out = [] # 출력

for i in range(0, n) : 
    time.append(list(map(int, input().split())))
# 회의 시간을 n개 입력받음

time.sort(key = lambda time : (time[1], time[0]))
#lamda : 간단한 함수식
# 우선 끝나는 시간으로 정렬하고, 만약 끝나는 시간이 같다면 시작이 시간이 빠른 순으로 정렬해야 한다.

out.append(time[0]) 
last = time[0]

for i in range(1, n) : 
    if last[1] <= time[i][0] : # 다음에 올 회의의 시작시간이 가장 이르고, last의 종료시간보다는 뒤인
        last = time[i]
        out.append(time[i])

print(len(out))