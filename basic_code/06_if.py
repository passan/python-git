"""만약 오늘 == 월요일 :
    출근한다.
만약 오늘== 일요일 :
    더잔다."""

today = "일요일"

if today == "월요일":
    print("출근해야지")
elif today == "일요일":
    print("오늘은 쉬는날~")        

if today == "일요일":
    print("오늘은 쉬는날~")



pizza = True
humburger = True

if pizza  and humburger:
    print("야호 피자랑 햄버거다")
elif humburger:
    print("와 햄버거다")
else:
    print("아 배고파")
