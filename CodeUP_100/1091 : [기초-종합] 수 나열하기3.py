a, m, d, n = map(int, input().split())
out = a;

for i in range(1, n) : 
    out = out * m + d

print(out)
