# 도서관에서는 나이에 따라 다양한 이용권을 제공합니다. 사용자의 나이를 입력받아,
# 해당 사용자에게 적합한 도서관 이용권을 판별하는 프로그램을 작성하세요

# 이용권의 종류
"""
- 어린이 이용권: 12세 이하 어린이 대상
- 청소년 이용권: 13세에서 18세 사이의 청소년 대상
- 성인 이용권: 19세 이상 성인 대상
"""

# 사용자가 계속 입력하도록 반복

for _ in range(3):
    age = int(input("사용자의 나이를 입력해주세요: ")) # 사용자의 나이를 입력

    # 입력받은 나이에 따라 이용권 결과 판별 및 출력
    try:
        
        if age <= 12:
            print("어린이 이용권을 사용할 수 있습니다.")
        elif 13 <= age <= 18:
            print("청소년 이용권을 사용할 수 있습니다.")
        else:
            print("성인 이용권을 사용할 수 있습니다.")
    except ValueError:
        print("숫자만 입력해주세요.")
    
print("프로그램을 종료합니다.")