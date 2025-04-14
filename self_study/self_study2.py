"""
이 프로그램은 사용자가 입력한 세 개의 수를 변의 길이로 하는 삼각형이 형성될
수 있는지, 그리고 가능하다면 어떤 유형의 삼각형인지 판별합니다. 삼각형을
판별하기 위한 기준은 다음과 같습니다
"""


# 각각 4회 실행됨
for _ in range(4):
    try:
        # 삼각형의 각 변의 길이 입력 받기
        side1 = int(input("첫 번째 변의 길이를 입력하세요: "))
        side2 = int(input("두 번째 변의 길이를 입력하세요: "))
        side3 = int(input("세 번째 변의 길이를 입력하세요: "))

        # 각 변의 조건 별로 삼각형 구분
        tri_1 = side1 == side2 == side3 # 정삼각형
        tri_2 = side1 == side2 or side1 == side3 or side2 == side3 # 이등변삼각형
        tri_3 = side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1 # 삼각형 x
        
        if tri_3:
            print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
        elif tri_1:
            print("입력하신 변의 길이로는 정삼각형을 만들 수 없습니다.")
        elif tri_2:
            print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")
        else:
            print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")
            
                
    except ValueError:
        print("숫자만 입력해주세요.")