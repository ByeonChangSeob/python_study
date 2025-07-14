import random
import time
def LV2(LV,b,limit_time,ranList,a):#첫 번째는 레벨,마지막은 배열 수
    LV=LV+1 #레벨 1단계 상승
    b=0     #배열 프린트 순서 초기화
    limit_time=1.5 #레벨 상승에 따른 time 감소
    ranList=random.sample(myList,a) #한개씩만 고르는 함수 초기화
    return LV,b,limit_time,ranList
def game_over(score):
    print("게임이 끝났습니다.")
    print(f"최종 스코어는 \"{score}\"입니다")
def game_start(score,life,b,a,limit_time): #점수 , 생명 , 배열 순서, 배열 갯수, 제한시간
    if(life>0):
        print(f"스코어:{score}")
        print(f"남은 생명:{life}")
        print(f"문제: \"{ranList[b]}\"")
        time_start=time.time()
        answer=input("제공하는 단어와 똑같이 쓰세요:")
        time_stop=time.time()
        time_res=time_stop-time_start
        if(time_res<=limit_time):
            if(ranList[b]==answer):
                print("정답입니다")
                b=b+1
                score+=1
            else:
                print("틀렸습니다 (life-1)")
                life=life-1
                b=b+1
        else:
            print("제한시간이 초과 되었습니다 (life-1)")
            life=life-1
            b=b+1
    return score,life,b
LV=1 #현재 레벨
score=0
life=3
limit_time=10
myList=[("포도"),("딸기"),"마라탕",("사랑"),("우리"),
        ("오렌지"),("바나나"),("동해물과"),("오류"),("파이썬"),("어렵다"),("화이팅"),
        ("집"),("집가자"),("10분휴식"),("물"),("핫식스"),("점심시간"),("고양이"),("밥먹자"),("꿇궭퀽"),("밗샅탕")]
a=len(myList) #배열의 총 갯수
b=0 #랜덤 배열의 순서
ranList=random.sample(myList,a)
input("게임을 시작하려면 아무 값이나 입력하세요!")
print((f"레벨 {LV} !!!"))
while(1):
    if(life>0):
        if(b!=a):
            score,life,b=game_start(score,life,b,a,limit_time) #LV 1 시작, 클리어 이후 LV 2 시작
        else:
            print("1단계 클리어!!")
            input("다음 단계로 갈려면 아무 값이나 입력하세요")
            LV,b,limit_time,ranList=LV2(LV,b,limit_time,ranList,a) #레벨 2로 가기 위한 세팅 함수 변수를 이용해서 함수를 더 만들어 두면 변수의 값에 따라 레벨 조절 가능
            print((f"레벨 {LV} !!!"))
    else:
        game_over(score) #게임오버 print 함수 활용
        break