# 메인 메뉴 출력
def menu_print():
    print("-----------------")
    print("1. 2단 구구단 출력")
    print("2. 4단 구구단 출력")
    print("3. 프로그램 종료")
    print("-----------------")
    
# 사용자가 종료 할 때까지 프로그램 반복
while True:
    menu_print()
    
    inputValue = int(input("메뉴를 선택 해주세요: ")) # 사용자에게 메뉴 입력 받음
    
    # 사용자가 1번 메뉴 선택시 2단 구구단 출력
    if inputValue == 1:
        for num in range(1, 10):
            print(f"2 x {num} = {2 * num}")
    
    # 사용자가 2번 메뉴 선택시 4단 구구단 출력        
    elif inputValue == 2:
        num = 1
        while num <= 9:
            print(f"4 x {num} = {4 * num}")
            num += 1
    
    # 사용자가 3번 메뉴 선택시 프로그램 종료        
    elif inputValue == 3:
        break
    
    # 1~3 이외의 메뉴 입력시 오류 메시지 출력
    else:
        print("1~3 사이의 값을 입력 해주세요")
