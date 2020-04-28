# https://www.acmicpc.net/problem/2217

n = int(input()) # 로프의 갯수
rope = []

for i in range(n) :  # 각 로프의 최대 중량
    rope.append(int(input()))

rope.sort()
max = rope[0] * n # 정렬 후, 가장 가벼운 로프를 기준으로 max 지정

# 로프를 하나씩 적게 사용하면서 최대중량의 무게를 찾아나감
for i in range(1, n) : 
    if max < rope[i] * (n - i) :
        max = rope[i] * (n - i)

print(max)