import random,time

def lotto():
    Lotto_Num=[random.randint(1,45) for i in range(6)]
    Lotto_Num.sort()
    for i in range(6):print(Lotto_Num[i],end=' ')
    print('\n')
    return Lotto_Num

while(True):
    a=input('로또 추첨 하시겠습니까?(y/n) )')    
    if a.lower()=='y':
        for i in range(1,6):
            print(f"{i}.....")
            time.sleep(2)
        lotto()
    else:
        print('잘 가 ~ !')
        break
