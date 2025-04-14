"""
이 프로그램은 사용자가 입력한 세 개의 수를 변의 길이로 하는 삼각형이 형성될
수 있는지, 그리고 가능하다면 어떤 유형의 삼각형인지 판별합니다. 삼각형을
판별하기 위한 기준은 다음과 같습니다
"""
# 사각형 판별을 위한 함수 정의
def triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return "입력하신 변의 길이로는 삼각형을 만들 수 없습니다."
    elif a == b == c:
        return "입력하신 변의 길이로는 정삼각형을 만들 수 있습니다."
    elif a == b or a == c or b == c:
        return "입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다."
    else:
        return "입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다."

# 각 4회 실행되는 프로그램 작성
for _ in range(4):
    try:
        side1 = int(input("첫 번째 변의 길이를 입력하세요: "))
        side2 = int(input("두 번째 변의 길이를 입력하세요: "))
        side3 = int(input("세 번째 변의 길이를 입력하세요: "))
        
        result = triangle(side1, side2, side3) # 삼각형을 정의하는 함수 호출출
        print(result)
    except ValueError:
        print("숫자만 입력해주세요.") # 숫자 이외 입력시 프로그램 종료료
        exit()