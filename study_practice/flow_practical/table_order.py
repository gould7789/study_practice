# 사용자로부터 테이블 개수 T
# 각 테이블의 행 수 M
# 열 수 N을 입력 받아 *로 구성된 MxN 테이블을 T개 출력하라

input_t = int(input("테이블 개수 입력: "))
input_m = int(input("행 수 입력: "))
input_n = int(input("열 수 입력: "))

for _ in range(input_t):
    for _ in range(input_m):
        print("*" * input_n)
        
    print()