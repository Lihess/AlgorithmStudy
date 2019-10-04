a = input()
a = int(a)

for i in range(1, a + 1) :
    if i % 3 == 0 : print('X', end =' ') 
    else : print(i, end = ' ')
