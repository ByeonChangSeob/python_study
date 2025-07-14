import random
import time
score=0
life=3
limit_time=10
myList=["포도","딸기","마라탕","사랑","우리",
        "오렌지","바나나","동해물과","오류","파이썬","어렵다","화이팅",
        "집","집가자","10분휴식","물","핫식스","점심시간","고양이","밥먹자","꿇궭퀽","밗샅탕"]
#ranList=random.choice(myList)
#print(ranList) 랜덤으로 나오는지 출력 확인
a=len(myList) #list 갯수
ranList=random.sample(myList,a) #1번씩만 출력되는 코드
input("게임을 시작하려면 아무 값이나 입력하세요!")
for i in range(a):
    if(life>0):
        print(f"스코어:{score}")
        print(f"남은 생명:{life}")
        print(f"문제: \"{ranList[i]}\"")
        time_start=time.time()
        answer=input("제공하는 단어와 똑같이 쓰세요:")
        time_stop=time.time()
        time_res=time_stop-time_start
        if(time_res<limit_time):
            if(ranList[i]==answer):
                print("정답입니다")
                score+=1
            else:
                print("틀렸습니다 (life-1)")
                life=life-1
        else:
            print("제한시간이 초과 되었습니다 (life-1)")
            life=life-1
    else:
        print("게임이 끝났습니다.") #life가 0이 될 시
        print(f"최종 스코어는 \"{score}\"입니다")
        break
    print("게임이 끝났습니다") #for문이 끝났을 시
    print(f"최종 스코어는 \"{score}\"입니다")
