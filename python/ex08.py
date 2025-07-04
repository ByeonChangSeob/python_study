num=int(input("네자리 정수를 입력하세요. :"))
num_1=num//1000
num_2=num//100%10
num_3=num//10%10
num_4=num%10
print("각 자리수의 합은",num_1+num_2+num_3+num_4,"입니다.")