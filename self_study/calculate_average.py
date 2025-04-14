# 학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램 작성


# 평균 점수 계산하고 학점 등급을 반환하는 함수 작성
def calculate_average(math_score, science_score, english_score):
    total = (math_score + science_score + english_score) / 3
    grade = ""
    
    # 평균 점수에 따라 다음과 같이 출력
    if total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B"
    elif total >= 70:
        grade = "C"
    elif total >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return f"평균 점수는 {total:.2f}점이고, 학점은 {grade}입니다."



math = float(input("수학 점수를 입력하세요 :"))
science = float(input("과학 점수를 입력하세요: "))    # 사용자로부터 수학, 과학, 영어의 점수를 입력
english = float(input("영어 점수를 입력하세요: "))



# 평균 계산 및 학점 등급 출력
# 함수 호출과 결과출력 코드를 작성
print(calculate_average(math, science, english))


