
# 사용자로부터 메뉴 번호를 입력받아 해당 도형의 면적을 계산하는 프로그램을 작성한다.
# 사용자에게 다음과 같은 메뉴를 보여준다
    # 원의 면적 계산
    # 삼각형의 면적 계산
    # 사각형의 면적 계산
    
# 사용자가 선택한 메뉴 번호에 따라 필요한값을 입력받고 면적을 계산한다.
# if, elif else 문만을 사용하여 조건을 분기한다.

# 원의 면적 = 3.14 * (r ** 2)
# 삼각형의 면적 = (밑변 * 높이) / 2
# 사각형의 면적 = (밑변 * 높이)

def get_dimen_radius():
    r = int(input("반지름을 입력하세요: "))
    return 3.14 * (r ** 2)

def get_dimen_triangle():
    bottom = int(input("밑변을 입력하세요: "))
    height = int(input("높이를 입력하세요: "))
    return (bottom * height) / 2

def get_dimen_rect():
    bottom = int(input("밑변을 입력하세요: "))
    height = int(input("높이를 입력하세요: "))
    return (bottom * height)

print("""[도형 면적 계산기]
    1. 원의 면적 계산
    2. 삼각형의 면적 계산
    3. 사각형의 면적 계산
      """)


choice = int(input("메뉴를 선택하세요: "))

result = ""
if choice == 1:
    result = f"원의 면적은 {get_dimen_radius()}입니다."
    
elif choice == 2:
    result = f"삼각형의 면적은 {get_dimen_triangle()}입니다."
    
elif choice == 3:
    result = f"사각형의 면적은 {get_dimen_rect()}입니다."
else:
    result = "잘못된 입력입니다"
    
print(result)