from random import randint
user=input("가위 바위 보 중 하나를 입력하세요")
com=randint(1,3)
temp=0
if(com==1):
    temp="가위"
elif(com==2):
    temp="바위"
else:
    temp="보"
print(f"사용자:{user} 컴퓨터:{temp}")
if(user==temp):
    print("무승부")
elif(user=="가위" and temp=="바위"):
    print("패")
elif(user=="가위" and temp=="보"):
    print("승")
elif(user=="바위" and temp=="가위"):
    print("승")
elif(user=="바위" and temp=="보"):
    print("패")
elif(user=="보" and temp=="가위"):
    print("패")
elif(user=="보" and temp=="바위"):
    print("승")
else:
    print("가위 바위 보 정보가 올바르지 않습니다.")