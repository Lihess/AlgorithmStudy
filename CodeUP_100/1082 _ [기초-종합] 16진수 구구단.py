a = input()
a = int(a, 16)

for i in range(1, 16) : 
    print("%X*%X=%X" % (a, i, (a * i))) # 이렇게 해야 AD 와 같이 출력됨