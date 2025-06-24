# 3명의 학생 이름과 국어 점수를 입력받아 딕셔너리에 저장하고
# 사용자가 이름을 입력하면 해당 학생의 점수를 출력하는 프로그램

# 학생의 정보를 저장할 딕셔너리
std_dict = {}

# 학생들의 이름과 점수를 3명 입력 받는다
for i in range(3):
    name = input("이름을 입력하세요: ")     # 학생의 이름을 입력 받음
    grade = int(input("국어 점수를 입력하세요: ")) # 학생의 점수를 입력 받음
    
    std_dict[name] = grade    # 딕녀너리에 "이름" : 점수 저장

# 학생 검색 기능
search = input("검색할 학생 이름을 입력하세요: ")

if search in std_dict:
    print(f"{search}의 점수는 {std_dict[search]}입니다.")
else:
    print("해당 학생은 등록되어 있지 않습니다.")