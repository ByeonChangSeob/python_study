num=int(input("100000에서 999999사이의 숫자를 입력하세요: "))
num_6=num//100000
num_5=num//10000%10
num_4=num//1000%10
num_3=num//100%10
num_2=num//10%10
num_1=num%10
if(num>=100000 and num<1000000):
    print("쉼표 표함 숫자는",num_6,num_5,num_4,",",num_3,num_2,num_1)
    print("쉼표 표함 숫자는 {}{}{},{}{}{}".format(num_6,num_5,num_4,num_3,num_2,num_1))
else :
    print("숫자를 잘못 입력하셨습니다.")
#1000의 몫과 나머지를 이용해서 코드 간소화 가능