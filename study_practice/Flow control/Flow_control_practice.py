# 점수를 입력 받아
# 입력 점수가 0보다 작으면
# "입력 값 오류" 출력 후
# 프로그램 종료

input_number = int(input("점수를 입력해주세요: "))

if input_number < 0:
    print("입력 값 오류\n프로그램 종료")
# 입력 값이 0 이상일 경우 합격 여부 판단
else:
    # if-elif-else
    # 점수에 따라 등급 부여 (90점 이상 A, 80점 이상 B, 70점 이상 C, 그 외 D)
    if input_number == 100:
        print("만점 축하")
    elif input_number >= 95:
        print("우수상")
    elif input_number >= 90:
        print("A등급")
    elif input_number >= 80:
        print("B등급")
    elif input_number >= 70:  
        print("C등급")
    else:
        print("D등급")
        
    # 중첩 if : A등급이면서 동시에 95점 이상이면
    # 우수상 출력
    
    # 추가 조건 : 점수가100이면 "만점 축하" 출력
    
    
    
    