# 1. 문제 개요
# 사용자로부터 메뉴 번호를 입력받아 
# 해당 도형의 면적을 계산하는 프로그램을 작성한다.

# 2. 문제 설명
# 사용자에게 다음과 같은 메뉴를 보여준다:
#  1. 원의 면적 계산
#  2. 삼각형의 면적 계산
#  3. 사각형의 면적 계산

# 사용자가 선택한 메뉴 번호에 따라 
# 필요한 값을 입력받고 면적을 계산한다.
# if, elif, else 문만을 사용하여 조건을 분기한다.

# 원의 면적 = π × 반지름² (π는 3.14로 고정)
# 삼각형의 면적 = (밑변 × 높이) ÷ 2
# 사각형의 면적 = 가로 × 세로


# 원 면적 함수 작성
def cir():
    cir_input = int(input("반지름을 입력하세요: "))  
    return 3.14 * cir_input**2      # 원의 면적 = π × 반지름² (π는 3.14로 고정)
# 삼각형 면적 함수 작성
def tri():
    tri_input1 = int(input("밑변을 입력하세요: ")) 
    tri_input2 = int(input("높이를 입력하세요: "))
    return (tri_input1 * tri_input2) / 2     # 삼각형의 면적 = (밑변 × 높이) ÷ 2
# 사각형 면적 함수 작성
def squ():
    squ_input1 = int(input("가로를 입력하세요: "))
    squ_input2 = int(input("세로를 입력하세요: "))
    return squ_input1 * squ_input2
# 메뉴 출력
print(""" 
1. 원의 면적 계산
2. 삼각형의 면적 계산
3. 사각형의 면적 계산""")

# 사용자에게 메뉴 입력 받음
choice = int(input("메뉴를 선택하세요: "))

result = ""

# 원 면적 계산
if choice == 1:
    result = f"원의 면적은 {cir()}입니다."
# 삼각형 면적 계산
elif choice == 2:
    result = f"삼각형의 면적은 {tri()}입니다."
# 사각형 면적 계산
elif choice == 3:
    result = f"사각형의 면적은 {squ()}입니다."
else:
    result = "잘못된 선택입니다."
    
print(result)