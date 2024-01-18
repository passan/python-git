
# for i in range(1, 12):
#     if i % 2 == 0:
#         print(f"{i}는 짝수입니다.")
#     else:
#         print(f"{i}는 홀수입니다.")



for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}는 3과 5의 배수입니다. ")
    elif i % 3 == 0:
        print(f"{i}는 3의 배수입니다. ")
    elif i % 5 == 0:
        print(f"{i}는 5의 배수입니다. ")
    # else:
    #     print(f"{i}는 5의 바수입니다.")