# 사용자에게 반복적으로 메뉴를 출력하고,
# 사용자의 선택에따라 합계, 평균, 지수 계산을 수행하는 프로그램을 작성하시오

# 사용자에게 입력 받을 메뉴를 출력한다(반복 출력)
while True:
    print("""----- 메뉴 -----
1. 합계 계산 (정수 두 개 입력)
2. 평균 계산 (실수 세 개 입력)
3. 지수 계산 (밑수 [정수], 지수 [정수] 입력)
4. 종료""")

    # 사용자가 메뉴를 선택
    try:
        user_choice = int(input("메뉴를 선택하세요: "))


        # 1번 메뉴를 선택했을 때
        if user_choice == 1:
            menu1_input1 = int(input("첫 번째 정수를 입력하세요: "))        # 사용자에게 첫 번째 정수 입력 받음
            menu1_input2 = int(input("두 번째 점수를 입력하세요: "))        # 사용자에게 두 번째 정수 입력 받음
            result = menu1_input1 + menu1_input2                          # 두 정수의 합 출력
            print(f"합계: {result}\n")

        # 2번 메뉴를 선택했을 때
        elif user_choice == 2:
            menu_input1 = float(input("첫 번째 실수를 입력하세요: "))      # 사용자에게 첫 번째 실수 입력 받음
            menu_input2 = float(input("두 번째 실수를 입력하세요: "))      # 사용자에게 두 번째 실수 입력 받음
            menu_input3 = float(input("세 번째 실수를 입력하세요: "))      # 사용자에게 세 번째 실수 입력 받음
            result = (menu_input1 + menu_input2 + menu_input3) / 3     # 세 실수의 평균 출력
            print(f"평균: {result:.2f}\n")

        # 3번 메뉴를 선택했을 때
        elif user_choice == 3:
            menu_input1 = int(input("밑수를 입력하세요: "))                # 사용자에게 밑수로 사용할 정수 입력 받음
            menu_input2 = int(input("지수를 입력하세요: "))                # 사용자에게 지수로 사용할 정수 입력 받음
            result = menu_input1 ** menu_input2                          # 지수 계산 결과 출력
            print(f"결과: {result}\n")

        # 4번 메뉴를 선택했을 때
        elif user_choice == 4:                                             
            print("프로그램 종료")                                          # 사용자가 4번 메뉴 선택시 프로그램 종료
            break

        # 사용자가 '1~4' 이외의 메뉴를 선택했을 때
        else:
            print("잘못된 입력입니다.\n")
            
            
    except ValueError:                                                     # 사용자가 숫자 이외의 내용 입력 했을 때
        print("숫자만 입력해주세요.\n")