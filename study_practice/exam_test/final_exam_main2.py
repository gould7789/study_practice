# 0부터 100 사이의 난수를 20개 생성하여 하나의 리스트에 저장
# 그 후 5개씩 분할하여 총 4개의 리스트로 복사

import random

# 20개의 난수를 저장하는 리스트
num_list = []
# 슬라이싱 리스트를 저장하는 리스트
s_list = []

# 난수 생성 및 리스트에 저장
for _ in range(20):
    random_value = random.randint(0, 100)
    num_list.append(random_value)

# 난수 리스트를 5개씩 슬라이싱해서 총 4개의 리스트로 저장
count = 0
for _ in range(4):
    slice = num_list[count:count+5]
    s_list.append(slice)
    count += 5


# 메뉴 출력
while True:
    print("""=== 리스트 관리 프로그램 ===
1. 각 리스트 내 데이터 출력
2. 특정 리스트 출력
3. 특정 리스트 삭제
4. 프로그램 종료""")
    
    # 사용자에게 메뉴를 선택 받음
    choice = int(input("메뉴 선택: "))
    
    # 1번 메뉴 선택 = 각 리스트 내 데이터 출력
    if choice == 1:
        count = 1
        for i in s_list:
            print(f"[리스트 {count}]: {i}")
            count += 1
        print()
        
        
    # 2번 메뉴 선택 = 특정 리스트 출력
    elif choice == 2:
        list_option = int(input(f"출력할 리스트 번호(1~{len(s_list)}): "))    # 사용자에게 출력할 리스트 번호를 입력 받음 - 삭제 후 자동으로 리스트 번호 범위가 줄어듬
        
        # 오류 출력
        if list_option > len(s_list) or list_option < 0:
            print("리스트 번호가 범위를 벗어났습니다.\n")
            continue
        
        print(f"[리스트 {list_option}]: {s_list[list_option - 1]}")
        print()
    
    
    # 3번 메뉴 선택 = 특정 리스트 삭제
    elif choice == 3:
        list_option = int(input(f"삭제할 리스트 번호(1~{len(s_list)}): ")) # 사용자에게 삭제할 리스트 번호를 입력 받음 - 삭제 후 자동으로 리스트 번호 범위가 줄어듬
        
        # 오류 출력
        if list_option > len(s_list) or list_option < 0:
            print("리스트 번호가 범위를 벗어났습니다.\n")
            continue
        
        del s_list[list_option - 1]
        print(f"리스트 {list_option}가 삭제되었습니다.")
        print()
    
    # 4번 메뉴 선택 = 프로그램 종료
    elif choice == 4:
        print("프로그램을 종료합니다.")
        break
    
    # 메뉴 번호가 잘못된 경우
    else:
        print("메뉴 안에서 번호를 선택해주세요.")