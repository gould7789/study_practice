# 1~100 사이 정수 중 7의 배수이면서, 11의 배수인 수중 제 일 작은 값을 출력하라

for input_value in range(1, 101):
    if input_value % 7 == 0 and input_value % 11 == 0:
        print(f"7과 11의 최소공배수는 : {input_value}")
        break