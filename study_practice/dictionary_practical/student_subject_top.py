# 학생들의 이름과 과목별 점수를 저장
# 각 과목마다 가장 높은 점수를 받은 학생과 점수를 출력

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

# 최고 점수자와 과목별 최고 점수 저장
top = {
    "국어" : {"이름" : "", "점수" : -1},
    "영어" : {"이름" : "", "점수" : -1},
    "수학" : {"이름" : "", "점수" : -1}
}

# 최대 점수자와 과목별 최고 점수 판별
for key, val in scores.items():     # 학생 정보에서 이름(key) : {과목 : 점수}(val)
    for subject, score in val.items():  # 과목(subject) : 점수(score)
        
        # 각 학생의 점수가 현재 가지고 있는 최고 점수보다 높다면
        if score > top[subject]["점수"]:
            top[subject]["이름"] = key
            top[subject]["점수"] = score

# 최종 출력
print("[과목별 최고 점수자]\n")

for key, val in top.items():
    print(f"{key}: {val["이름"]} ({val["점수"]}점)")