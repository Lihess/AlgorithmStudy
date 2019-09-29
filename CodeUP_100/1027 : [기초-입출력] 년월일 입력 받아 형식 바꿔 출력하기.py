y, m, d = input().split('.') # .으로 구분하여 받고

print('%02d' % int(d), end = '-') # - 형식으로 출력, 02로 하면 앞에 0이 채워지고 2로 하면 안 채워짐
print('%02d' % int(m), end = '-')
print('%04d' % int(y), end = '')
