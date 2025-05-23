# iteration : 순회
bar = [10, 20, 30, 40, 50]

for index in range(len(bar)):
    print(bar[index])


for val in bar:
    print(val)


bar = "h1rr2t"

for val in bar:
    print(f"{val}, {val.isdigit()}")

# # 인덱스와 밸류값을 같이 출력할 때
# for index, val in enumerate(bar):
#     print(f"{index} : {val}")
    


# # 멀티플 어사이먼트
# pos, kin = 2, 3
# print(pos, kin)

# # [Unpacking]
# pos, kin, sol = [2, 3, 4]
# print(pos, kin, sol)

