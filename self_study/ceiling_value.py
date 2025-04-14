"""
사용자로부터 세 개의 정수 숫자를 입력받고
이 중 가장 큰 숫자를 찾아 출력하는프로그램을 작성하세요
"""

# 사용자로부터 세 개의 정수 숫자를 입력받습니다
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

max_value = max(num1, num2, num3)

print(f"가장 큰 숫자는 {max_value}입니다.")