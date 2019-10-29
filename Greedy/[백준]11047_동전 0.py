n, k = map(int, input().split()) # 동전의 종류와 금액 입력
a = [] # 각 동전의 가치
num = 0 # 동전의 갯수

for i in range(0, n) : # 가치를 입력받음
    a.append(int(input()))

a.sort(reverse=True)
# 내림차순으로 정렬함으로써, 가치가 큰 화폐를 먼저 점검한다.
# 가치가 큰 화폐를 먼저 사용할 수록 최종적으로 사용되는 화례의 갯수는 감소!

for i in a : 
    div = int(k / i)
    if div > 0 : # 몫이 0보다 크다면, 해당 화폐가 사용가능하므로
        num += div
        k -= div * i

print(num)