a, b, c = map(int, input().split())
day = 1

while 1 :
    if (day % a == 0) & (day % b == 0) & (day % c == 0) : break;
    else : day += 1
print(day)
