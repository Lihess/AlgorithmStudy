# 일단, 문자열을 입력받고 출력하는 것이 아닌 한 숫자를 입력받아서 입력받은 숫자를 판단해서 중단하고 싶었다.
# 그래서 생각한게 input().split()[0]. 아무리 입력해도 맨앞에 1글자만 입력하면 출력하도록 함

while 1 :
    a = input().split()[0]
    
    if a == '0' : break
    print(a)
