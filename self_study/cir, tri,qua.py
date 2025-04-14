# 1. 문제 개요
# 사용자로부터 메뉴 번호를 입력받아
# 해당 도형의 면적을 계산하는 프로그램을 만든다

# 2. 문제 설명
# 사용자에게 다음과 같은 메뉴를 보여준다.
# 1. 원의 면적 계산
# 2. 삼각형의 면적 계산
# 3. 사각형의 면적 계산

# 사용자가 선택한 메뉴 번호에 따라 
# 필요한 값을 입력받고 면적을 계산한다.
# if, elif, else 문만을 사용하여 조건을 분기한다.

# 원의 면적 = π × 반지름² (π는 3.14로 고정)
# 삼각형의 면적 = (밑변 × 높이) ÷ 2
# 사각형의 면적 = 가로 × 세로

# 메뉴 출력
print("""[도형 면적 계산기]
1. 원
2. 삼각형
3. 사각형""")

# 사용자에게 메뉴 번호 입력 받음
choice = int(input("메뉴를 선택하세요: "))

# 사용자가 선택한 번호에 따른 도형 면적 계산 

# 원 면적 계산
if choice == 1:
    cir_input = int(input("반지름을 입력하세요: "))
    result_cir = 3.14 * cir_input**2 # 원의 면적 = π × 반지름² (π는 3.14로 고정)
    print(result_cir)
# 삼각형 면적 계산
elif choice == 2:
    tri_input_1 = int(input("밑변을 입력하세요: "))
    tri_input_2 = int(input("높이를 입력하세요: "))
    result_tri = (tri_input_1 * tri_input_2) / 2 # 삼각형의 면적 = (밑변 × 높이) ÷ 2
    print(result_tri)
# 사각형 면적 계산 
elif choice == 3:
    squ_input_1 = int(input("가로를 입력하세요: "))
    squ_input_2 = int(input("세로를 입력하세요: "))
    result_squ = squ_input_1 * squ_input_2 # 사각형의 면적 = 가로 × 세로
    print(result_squ)
else:
    print("잘못된 선택입니다.")