# 사용자 나이대를 영어로 표현하기

# 사용자로부터 나이를 입력받습니다. (정수형으로 가정)
try:
    Age = int(input("나이를 입력하세요: "))

    """
    입력된 나이에 따라 사용자를
    청소년(Teenager), 성인(Adult), 노년(Senior) 중 하나로 분류 합니다.
    """

    # 13세에서 19세 사이는 "Teenager"
    if 13 <= Age <= 19:
        category = "Teenager"
    # 20세에서 64세 사이는 "Adult"
    elif 20 <= Age <= 64:
        category = "Adult"
    # 65세 이상은 "Senior"
    elif 65 <= Age:
        category = "Senior"
        
    print(f"You are in the '{category}' age group.")
except ValueError:
    print("오류! 숫자만 입력하세요.")