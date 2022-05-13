for i in range(4):
    name,score=input("이름과 점수를 입력하세요 : ").split(" ");score=int(score)
    if score in range(90,101):grade='A'
    elif score in range(80,90):grade='B'
    elif score in range(70,80):grade='C'
    elif score in range(60,70):grade='D'
    else:grade='F'
    print(f"{name}\n{score}\n{name}의 학점 : {grade}")

    
    
