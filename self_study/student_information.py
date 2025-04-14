# 학생 정보를 저장할 리스트
students = []

# 학생 정보를 입력하는 함수
def input_student():
    student_id = int(input("학번을 입력하세요: "))
    name = input("이름을 입력하세요: ")
    kor = int(input("국어 성적을 입력하세요: "))
    eng = int(input("영어 성적을 입력하세요: "))
    math = int(input("수학 성적을 입력하세요: "))

    # 총점 및 평균 계산
    total = kor + eng + math
    avg = round(total / 3, 2)

    # 딕셔너리 형태로 저장
    student = {
        "학번": student_id,
        "이름": name,
        "국어": kor,
        "영어": eng,
        "수학": math,
        "총점": total,
        "평균": avg
    }

    students.append(student)
    print(f"{name} 학생의 성적이 저장되었습니다.\n")

# 입력된 학생 정보를 출력하는 함수 (입력 순서대로)
def print_students():
    if not students:
        print("입력된 학생 정보가 없습니다.\n")
        return

    print("\n학생 성적 목록:")
    print(f"{'학번':<8}{'이름':<8}{'국어':<6}{'영어':<6}{'수학':<6}{'총점':<6}{'평균':<6}")
    print("=" * 50)

    total_avg = 0
    for student in students:
        print(f"{student['학번']:<8}{student['이름']:<8}{student['국어']:<6}{student['영어']:<6}{student['수학']:<6}{student['총점']:<6}{student['평균']:<6}")
        total_avg += student["평균"]

    total_avg = round(total_avg / len(students), 2)
    print(f"\n현재 입력된 데이터 개수: {len(students)}")
    print(f"전체 학생 평균 값: {total_avg}\n")

# 메인 메뉴 실행 함수
def main():
    while True:
        print("1. 학생 성적 입력")
        print("2. 학생 목록 출력 (입력 순)")
        print("3. 프로그램 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            input_student()
        elif choice == "2":
            print_students()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.\n")

# 프로그램 실행
if __name__ == "__main__":
    main()