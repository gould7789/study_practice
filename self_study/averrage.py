# 키보드로부터 3개의 정수를 입력받아 평균을 계산하는 프로그램을 작성한다.
# 사용자로부터 정수 3개를 입력받는다.
# 입력받은 3개의 정수의 평균을 계산하여 출력한다.

# 사용자로부터 세 개의 정수를 입력받는다.
input_number1 = int(input("정수 1 입력: "))
input_number2 = int(input("정수 2 입력: "))
input_number3 = int(input("정수 3 입력: "))
# 세 정수의 합을 구하고 3으로 나누어 평균을 계산한다.
result = round((input_number1 + input_number2 + input_number3) / 3, 2)
# 평균을 출력한다.
print(f"평균: {result}")