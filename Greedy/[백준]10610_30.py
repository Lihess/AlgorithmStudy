# https://www.acmicpc.net/problem/10610

number = list(map(int, input()))
number.sort(reverse=True) # 입력받은 숫자를 내림차순으로 정렬

if number[len(number) - 1] == 0 and sum(number) % 3 == 0: 
    # 3의 배수는 모든 자리수의 합이 3의 배수라는 속성을 이용
    print(''.join(list(map(str, number))))
else :
    print("-1")