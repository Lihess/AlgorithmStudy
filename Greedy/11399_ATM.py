sum = 0 # 시간의 합
n = int(input()) # n명 입력
p = list(map(int, input().split())) # 실제 입려될 작업시간

if len(p) == n : 
    p.sort() # n명이 입력된 경우, 오름차순으로 정렬한다.

for i in range(0, n) :
    for j in range(0, i + 1) : 
        sum += p[j] # 자신보다 처리 시간이 작게 걸리는 사람은 모두 더함

print(sum)

