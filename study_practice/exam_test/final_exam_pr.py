# 학생의 성적을 입력, 출력, 조회 , 삭제하는 메뉴 기반 프로그램 작성
# 각 학생은 학번을 기준으로 저장되며, 이름 ,국어, 영어, 수학 성적의 합계와 평균도 함께 저장

# 학생의 학번을 기준으로 저장하는 딕셔너리
std_dict = {}

# 메뉴 출력
while True:
    print("""
===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료""")
    menu_choice = int(input("메뉴 선택 (1~5): "))   # 사용자에게 메뉴를 입력 받음

    # 학생 성적 입력
    if menu_choice == 1:
        std_num = int(input("학번 입력: "))
        # 오류
        if std_num in std_dict:
            print("이미 등록된 학번입니다.")
            continue
        
        name = input("이름 입력: ")
        kor = int(input("국어 성적 입력: "))
        eng = int(input("영어 성적 입력: "))
        math = int(input("수학 성적 입력: "))
        total = kor + eng + math
        avg = total / 3
        
        # 학생 정보를 저장할 딕셔너리
        # std_num : {"목록" : 사용자 입력값} =  key : value로 std_dict에 저장됨
        std_dict[std_num] = {
            "학번" : std_num,
            "이름" : name,
            "국어" : kor,
            "영어" : eng,
            "수학" : math,
            "합계" : total,
            "평균" : avg
        }
        print("성적이 저장되었습니다.")

    # 학생 성적 출력
    elif menu_choice == 2:
        #오류
        if not std_dict:
            print("저장된 학생 정보가 없습니다.")
            continue
        
        print("[전체 학생 성적]")
        count = 0
        for key, val in std_dict.items():   # 학번 : {정보 목록 : 정보}
            if count == 0:
                for key_2 in val.keys():    # 정보 목록 : 정보 -> 정보 목록 출력
                    print(f"{key_2}", end="\t")
                print()
                count += 1                  # 항목은 한 번만 출력되도록
            
            for val_2 in val.values():  # 정보 목록 : 정보 -> 정보 출력
                print(f"{val_2}", end="\t")
            print()
        
                
    # 학생 성적 확인
    elif menu_choice == 3:
        grade = int(input("조회할 학번 입력: "))
        
        # 오류
        if grade not in std_dict:
            print("해당 학번의 학생 정보가 없습니다.")
            continue
        
        print("\n[학생 정보]")
        student = std_dict[grade]           # 학번 조회
        for key, val in student.items():
            print(f"{key}: {val}")
        

    # 학생 성적 삭제
    elif menu_choice == 4:
        grade = int(input("삭제할 학번 입력: "))
        
        # 오류
        if grade not in std_dict:
            print("해당 학번의 학생 정보가 없습니다.")
            continue
        
        # 삭제
        del std_dict[grade]
        print("학생 정보가 삭제되었습니다.")
        
    # 종료
    elif menu_choice == 5:
        print("프로그램을 종료합니다.")
        break  
    
    # 사용자가 잘못된 입력값을 넣었을 때 오류
    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 선택하세요.")