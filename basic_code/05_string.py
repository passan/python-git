name = "apple"
job = "pm"
age = 15

print("안녕 내 이름은 " + name + '야.' + ' 직업은 ' + job + '나이는 ' + str(age) + '야')
print("안녕 내 이름은 %s 야 그리고 직업은 %s 야 나이는 %s" %(name, job, age))
print("안녕 내 이름은 {0} 야 그리고 직업은 {0} 야 나이는 {0}" .format(name, job, age))
print(f"안녕 내 이름은 {name} 야 그리고 직업은 {job} 야 나이는 {age}")