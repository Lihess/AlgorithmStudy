a = input()
sum = 0

for i in range(0,int(a)) : 
    sum += i
    if sum >= int(a) : 
        print(i)
        break
