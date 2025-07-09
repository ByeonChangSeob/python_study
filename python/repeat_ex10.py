a=int(input("1^2 부터 n^2 까지 합 할 수를 입력하시오"))
b=1
c=0
while(1):
    if(b<=a):
        c=c+b**2
        b+=1
    else:
        print("합은",c,"입니다")
        break