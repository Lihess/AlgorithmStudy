from queue import PriorityQueue

n = int(input())
num = []
out = []
sum_ = 0

for i in range(0, n) : 
    num.append(list(map(int, input().split())))
    # n개의 문제를 받음

num.sort(key = lambda num : (num[0], -num[1]))
que = PriorityQueue()

for i in num : 
    que.put((-i[1], i[0]))

while not que.empty() :
    x = que.get()

    j_n = int(out.count(x[1]))
    j = 0
    while j <= j_n :
        if ((x[1] - j) > 0) :
            overlapping = out.count(x[1] - j)
        else : break

        if overlapping == 0 :
            out.append(x[1] - j)
            sum_ += abs(x[0])
            break
        else :  
            j += 1
        
print(sum_)