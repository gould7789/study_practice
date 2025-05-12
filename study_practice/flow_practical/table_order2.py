# 1 버전과 동일하게 T, M, N을 입력받고, 출력 옵션을 선택하여 출력
# 랜덤 함수 사용
import random

input_t = int(input("테이블 개수 입력: "))  # 사용자에게서 출력할 테이블 갯수를 입력 받음
input_m = int(input("행 수 입력: "))        # 사용자에게서 출력할 행의 갯수를 입력 받음
input_n = int(input("열 수 입력: "))        # 사용자에게서 출력할 열의 갯수를 입력 받음

# 메뉴 출력
print("""출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1~100 사이 랜덤 값 출력""")

# 사용자가 메뉴 입력
menu = int(input("옵션 (1 또는 2): "))
print()

# 1번 메뉴를 선택했을 때 순자 숫자 출력 : 1부터 시작하여 열 방향으로 증가
if menu == 1:
    for t in range(1, input_t + 1):
        print(f"테이블 {t}")
        count = 0
        
        for _ in range(input_m):
            for _ in range(input_n):
                count += 1
                print(count, end="\t")
            print()
        print()

# 2번 메뉴를 선택했을 때 랜덤 숫자 출력: 1~100 사이 난수 채우기
elif menu == 2:
    num_list = list(range(1, 101))              # 중복 제거를 위해 1~100까지 리스트 생성
    for t in range(1, input_t + 1):
        print(f"테이블 {t}")
        
        for _ in range(input_m):
            for _ in range(input_n):
                rand_num = random.randint(0, len(num_list) - 1)     # 리스트의 인덱스 랜덤 숫자 출력
                fin_num = num_list.pop(rand_num)                    # pop을 사용해서 출력 된 숫자 출력 후 제거
                print(fin_num, end=" ")
                # rand_num = random.choice(num_list)     # 리스트에서 랜덤으로 인덱스 출력
                # print(rand_num, end=" ")
                # num_list.remove(rand_num)              # 출력된 값은 리스트에서 제거 -> 중복 출력 제거
            print()
        print()