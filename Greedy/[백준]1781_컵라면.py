import sys
from queue import PriorityQueue
# 시간 단축을 위해 우선순위 큐를 사용한다.

n = int(sys.stdin.readline()) # input 보다 속도가 빨라~!
num = [] # 컵라면을 받음

for i in range(0, n) : 
    num.append(list(map(int, sys.stdin.readline().split())))
    # n개의 문제를 받음

num.sort(key = lambda num : (num[0], -num[1]))
que = PriorityQueue()

for i in num : 
    deadline = i[0]
    que.put(i[1]) 
    while que.qsize() > deadline : # 데드라인이 더 길다면 제거 
        que.get()

sum_ = 0
while not que.empty() : 
    sum_ += que.get()
        
print(sum_)