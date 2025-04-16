# 1부터 20 사이의 수 중에서 3의 배수도 아니고 짝수도 아닌 수만 출력하는 프로그램 작성

# while 버전

# while의 조건을 설정 및 출력 할 숫자 저장용 변수 선언
input_number = 1

# 1부터 20 사이의 숫자 반복 출력
while input_number <= 20:
    if input_number % 3 != 0 and input_number % 2 != 0:  # 3의 배수도 아니고 짝수도 아닌 수
        print(input_number)                              # 결과 출력
    input_number += 1                                    # 1씩 증가시켜 while 종료시점 만들기