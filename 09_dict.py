user = {}

print(user)

user = {"이름" : "홍길동", "job" : "PM", "나이" : "20"}

print(user)

print(user["이름"])

user["size"] =190

print(user)

del user["나이"]

print(user)

keys_list = user.keys()
print(type(keys_list))
keys_list = list(keys_list) #key 값 리스트로 변환

print(keys_list)
print(type(keys_list))

value_list = user.values()
print(type(value_list))
value_list = list(value_list) #value 값 리스트로 변환

print(value_list)
print(type(value_list))

item_list = user.items()
print(item_list)
print(type(item_list))

item_list = list(item_list)#item 값 리스트로 변환
print(type(item_list))

