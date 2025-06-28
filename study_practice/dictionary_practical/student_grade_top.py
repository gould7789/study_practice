# 여러 학생의 이름과 과목별 점수를 저장하고
# 전체 학생 중 가장 평균 점수가 높은 학생을 찾아 출력하는 프로그램 작성

# 학생의 이름과 성적들을 입력하는 딕셔너리
scores = {}

# 사용자에게 총 몇명의 학생을 입력할 것인지 입력 받음
user_input = int(input("몇 명의 학생을 입력하시겠습니까: "))

# 학생의 수만큼 반복
for _ in range(user_input):
    name = input("이름을 입력하세요: ")
    kor = int(input("국어 성적 입력: "))
    eng = int(input("영어 성적 입력: "))
    math = int(input("수학 성적 입력: "))

    # 각 학생별 성적 저장
    scores[name] = {
        "국어" : kor,
        "영어" : eng,
        "수학" : math
    }
    print()


max_std = ""    # 평균이 가장 높은 학생
max_avg = -1    # 평균이 가장 높은 학생의 평균 점수

# 딕셔너리에서 학생이름 : 과목별 점수 분배
for key, value in scores.items():
    # 각 학생마다 평균값 계산 
    avg = sum(value.values()) / len(value)
    
    # 학생마다 비교해서 가장 높은 평균을 가진 학생과 그 평균값
    if avg > max_avg:
        max_avg = avg
        max_std = key

# 최종 출력
print("[최고 평균 점수 학생]")
print(f"{max_std} - 평균: {max_avg:.2f}점")