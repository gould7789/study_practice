# 사용자 입력을 통해 리스트의 요소를 추가(Create), 조회(Read), 수정(Update), 삭제(Delete) 하는 기능을 구현한다.

# 빈 리스트 생성
items = []

while True:
    # 메뉴 작성
    print("""작업을 선택하세요:
1: 요소 추가 (Create)
2: 요소 조회 (Read)
3: 요소 수정 (Update)
4: 요소 삭제 (Delete)
5: 종료 (Exit)""")
    
    # 사용자에게 메뉴 선택 받음
    menu_choice = int(input("입력: "))
    
    # 사용자로부터 문자열을 입력받아 리스트의 끝에 추가한다
    if menu_choice == 1:
        input_number = int(input("추가할 값을 입력하세요: "))
        items.append(input_number)
        print("추가 완료.")
        print()
    
    # 현재 리스트의 모든 요소를 인덱스와 함께 출력한다
    elif menu_choice == 2:
        for index, value in enumerate(items):
            print(f"{index}: {value}")
        # for index in range(0, len(items)):
        #     print(f"[현재 리스트 내용] \n {index} : {items[index]}")
        print()
    
    # 인덱스와 새로운 값을 입력받아 해당 인덱스의 요소를 수정한다
    # 인덱스가 잘못되었을 경우 안내 메시지를 출력한다
    elif menu_choice == 3:
        input_index = int(input("수정할 인덱스를 입력하세요: "))
        
        if 0 <= input_index < len(items):
            input_number = int(input("새로운 값을 입력하세요: "))
            items[input_index] = input_number
            print("수정 완료.\n")
        else:
            print("유효하지 않은 인덱스입니다.")
    
    # 인덱스를 입력받아 해당 위치의 요소를 삭제한다
    # 인덱스가 잘못되었을 경우 안내 메시지를 출력한다
    elif menu_choice == 4:
        input_index = int(input("삭제할 인덱스를 입력하세요: "))
        
        if 0 <= input_index < len(items):
            del items[input_index]
            print("삭제 완료.\n")
        else:
            print("유효하지 않은 인덱스입니다.")
    
    # 프로그램 종료
    elif menu_choice == 5:
        break
    
    else:
        print("올바른 번호를 입력하세요")