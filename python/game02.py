import random
import time
def hint_fun(back):
    count=len(my_List[ran_num1][1])
    for i in range(count):
        if(wrong==i):
            return i+1
#a,b=random.choice(my_List) a랑 b에 각자 front 와 back 값 저장
my_List=[("가는말이 고와야","오는말이 곱다"),("돌다리도","두드려 보고 건너라"),("하늘이 무너져도","솟아날 구멍이 있다"),("등잔 밑이", "어둡다"),("세살 버릇","여든까지 간다"),("티끌 모아", "태산"),("울며", "겨자 먹기"),("국물도","없다"),("친구따라","강남간다"),("낫 놓고","기역자도 모른다")]
score=0
wrong=0
a=0
hint=0
while(a<5):
    if(wrong==0):
        ran_num1=random.randint(0,9)
        len_ran_num=len(my_List[ran_num1][1])
        print(f"속담: \"{my_List[ran_num1][0]}___\"")
        answer = input("뒷부분을 입력하세요: ").strip()
    else:
        answer = input("뒷부분을 입력하세요: ").strip()
    if(my_List[ran_num1][1]==answer):
        print("정답입니다!")
        wrong=0
        score+=1
        a=a+1
    elif wrong<len_ran_num-1: #ex) 안녕하세요 ->wrong 0~4 len 5이기 때문에 num -1
        print(f"틀렸습니다! 힌트는 : \"{my_List[ran_num1][1][:hint_fun(0)]}\"입니다. 다시 한 번 입력하세요\n")
        wrong=wrong+1
    else:
        print(f"틀렸습니다! 정답은 : \"{my_List[ran_num1][1]}\"입니다\n")
        wrong=0
        a=a+1
print("스코어는",score,"점 입니다.")