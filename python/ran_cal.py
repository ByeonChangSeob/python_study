from random import randint
num1=randint(1,20)
num2=randint(1,20)
max_num=max(num1,num2)
min_num=min(num1,num2)
a=randint(1,4)
cal=0
ans=0
if(a==1):
    cal=num1+num2 #+연산
elif(a==2):
    cal=max_num-min_num #-연산
elif(a==3):
    cal=num1*num2 #x연산
else:
    cal=max_num//min_num
if(a==2):
    ans=int(input(f"{max_num} - {min_num}? ="))
elif(a==4):
    ans=int(input(f"{max_num} / {min_num}?(몫 만 입력하기) ="))
elif(a==1):
    ans=int(input(f"{num1} + {num2}? ="))
else:
    ans=int(input(f"{max_num} * {min_num}? ="))

if(ans==cal):
    print("정답입니다!")
else:
    print("틀렸습니다!")