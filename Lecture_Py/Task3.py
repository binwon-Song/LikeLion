name,score=input("Enter the name and score : ").split(" ");score=int(score)
if score in range(90,101):grade='A'
elif score in range(80,90):grade='B'
elif score in range(70,80):grade='C'
elif score in range(60,70):grade='D'
else:grade='F'
print(f"Name : {name} \nScore : {score} \nGrade : {grade}")
