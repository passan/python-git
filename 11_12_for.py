days = ["월", "화", "수", "목", "금"]

for day in days:
    print(f"{day}요일입니다.")

print("주말입니다.")


num = 0

for i in range(0,11):
    print(i)
    num = num + i

print(num)


for j in range(2,10):
    
    for h in range(1,10):
        result = j * h
        # print(f"{j} * {h} = {result}")
        print(f"{j} * {h} = {j * h}")