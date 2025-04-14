# 사용자로부터 정수와 실수를 각각 하나씩 입력받아 두 수의 차를 계산하고, 결과값과 그 자료형을 출력한다
# 사용자로부터 첫 번째 수는 정수로, 두 번째 수는 실수로 입력받는다.
# 두 수의 차(뺄셈)를 계산하여 출력한다.
# 결과값의 자료형을 함께 출력한다.
# 왜 결과값의 자료형이 float이 되는지 확인하고 이해한다

# 사용자로부터 '정수'를 입력 받음
input_number1 = int(input("정수를 입력하세요: "))
# 사용자로부터 '실수'를 입력 받음
input_number2 = float(input("실수를 입력하세요: "))

# 두 수의 차를 계산 input_number1 - input_number2
result = input_number1 - input_number2

# 결과값을 자료형과 함께 출력
print(f"차이: {result}\n자료형: {type(result)}")