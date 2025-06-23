# 학생들의 이름과 나이를 입력받아 딕셔너리에 저장하고
# 마지막에 전체 학생의 이름과 나이를 출력

# 학생들의 정보를 저장하는 딕셔너리
std_dict = {}

# 학생들의 이름과 나이를 3명 입력 받는다
for i in range(3):
    name = input("이름을 입력하세요: ")     # 학생의 이름을 입력 받음
    age = int(input("나이를 입력하세요: ")) # 학생의 나이를 입력 받음
    
    std_dict[name] = age    # 딕녀너리에 "이름" : 나이 저장

print("[전체 학생 정보]")

# 전체 학생 정보 출력
for key, val in std_dict.items():
    print(f"{key} : {val}살")