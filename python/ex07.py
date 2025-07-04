from math import sqrt
a=int(input("첫 번째 좌표의 x 값을 입력하세요 :"))
b=int(input("첫 번째 좌표의 y 값을 입력하세요 :"))
c=int(input("두 번째 좌표의 x 값을 입력하세요 :"))
d=int(input("두 번째 좌표의 y 값을 입력하세요 :"))
x=a-c
y=b-d

print("두 점 사이의 거리는",round(sqrt(x**2+y**2),2),"입니다.")