a=int(input("첫번째 정수를 입력하세요"))
b=int(input("두번째 정수를 입력하세요"))
c=int(input("세번째 정수를 입력하세요"))
temp=0
if(a<b and a<c):
    temp=a
    print(temp)
elif(b<a and b<c):
    temp=b
    print(temp)
elif(c<a and c<b):
    temp=c
    print(temp)
elif(c==a==b):
    print("똑같은 값이 3개입니다")
    temp=a
    print(temp)
    