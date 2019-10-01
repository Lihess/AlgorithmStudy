a = input()
a = int(a, 16)

for i in range(1, 16) :  
    print("%X*%X=%X" % (a, i, (a * i))) # hex()와 같이 하면 0x56 와 같은 형태로 출력됨.
