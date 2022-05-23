def add(a,b):
    return a+b
def odd(a,b):
    return a-b
def division(a,b):
    return a/b
def mul(a,b):
    return a*b

while True:
    a,b=map(int,input("숫자 두 개를 입력하세요 : ").split())
    print('어떤 연산을 할까요? ')
    symbol=input()
    if(symbol=='+'):
        print(f"{a} + {b} = {add(a,b)}")
    elif(symbol=='-'):
        print(f"{a} - {b} = {odd(a,b)}")
    elif(symbol=='/'):
        print(f"{a} / {b} = {division(a,b)}")
    elif(symbol=='*'):
        print(f"{a} * {b} = {mul(a,b)}")
    else:
        print("더하기 빼기 나누기 곱셈만 지원합니다.")