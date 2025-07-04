hour=int(input("시간을 입력하세요 :"))
minute=int(input("분을 입력하세요 :"))
time_sec_sum=0
minute_to_hour=0
minute_1=0

if(minute>=60) :
    minute_to_hour=minute//60
    minute_1=(minute%60)
    print(hour*3600+minute_to_hour*3600+minute_1*60)
else :
    print(hour*3600+minute*60)