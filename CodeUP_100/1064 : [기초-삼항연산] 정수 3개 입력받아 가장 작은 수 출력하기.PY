a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((c if b > c else b) # 참이라면
      if (a > b) else    # 처음 비교
      (c if (a > c) else a)) # 거짓이라면 
## 너무 더럽다고 생각..
