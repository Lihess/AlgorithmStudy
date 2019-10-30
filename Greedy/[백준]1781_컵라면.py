from queue import PriorityQueue

n = int(input())
num = []
out = []
sum = 0

for i in range(0, n) : 
    num.append(list(map(int, input().split())))
    # n개의 문제를 받음

num.sort(key = lambda num : (num[0], -num[1]))
que = PriorityQueue()

for i in num : 
    que.put((i[0], -i[1]))


