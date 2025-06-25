# 학생들의 이름과 각 과목의 성적을 저장하는 딕셔너리를 만들고
# 이름을 입력받아서 해당 학생의 총점과 평균을 출력

# 학생들의 이름과 성적을 저장하는 딕셔너리
std_dict = {}

# 학생들의 이름 및 성적 저장
for _ in range(2):
    name = input("이름 입력: ")
    kor = int(input("국어 점수: "))
    eng = int(input("영어 점수: "))
    math = int(input("수학 점수: "))
    
    # 각 학생별 성적 저장
    std_dict[name] = {
        "국어" : kor,
        "영어" : eng,
        "수학" : math
    }
    print()

# 사용자에게 학생 이름을 입력 받음
students = input("\n검색할 학생 이름 입력: ")


if students in std_dict:
    print(f"[{students}의 성적]")
    score = std_dict[students]      # 해당 학생의 성적
    total = sum(score.values())     # 총점
    avg = total / len(score)        # 평균
    
    # 최종 출력
    print(f"총점: {total}점")
    print(f"평균: {avg:.1f}점")

else:
    print("해당 학생 없음")