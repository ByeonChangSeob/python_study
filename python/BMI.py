height=float(input("키를 입력하세요: "))/100
weight=float(input("몸무게를 입력하세요: "))
BMI=round(weight/(height**2),1)
print(BMI)
if(BMI<18.5):
    print("저체중 입니다.")
elif(18.5<=BMI<=22.9):
    print("정상 입니다.")
elif(23<=BMI<=24.9):
    print("과체중 입니다.")
elif(BMI>=25):
    print("비만 입니다.")
elif(height<=0 or weight<=0):
    print("정보를 잘못 입력하셨습니다.") 