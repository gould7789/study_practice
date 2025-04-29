# 숫자 맞추기 게임

# while문과 break문을 사용하여 1부터 100 사이의 숫자를 맞추는 게임 작성
# 사용자가 숫자를 맞출 때까지 반복하고, 맞추면 반복을 종료
# 정답 숫자는 랜덤 함수를 이용하여 1에서 100사이 임의 정수 선택

import random

value_number = random.randint(1, 100)   # 1부터 100 사이의 숫자 중 랜덤으로 정답 설정

while True:
    user_input = int(input("1부터 100사이의 숫자를 맞춰보세요: "))  # 사용자에게 정답을 입력 받음
    
    if user_input == value_number:      # 입력한 답이 정답과 일치하면 프로그램 종료
        print("정답입니다!")
        break
    
    elif 101 > user_input > value_number:   # 입력한 답이 정답보다 클 경우 "더 작은 숫자입니다" 힌트 출력
        print("더 작은 숫자입니다.")
        
    elif 0 < user_input < value_number:     # 입력한 답이 정답보다 작을 경우 "더 큰 숫자입니다" 힌트 출력
        print("더 큰 숫자입니다.")
        
    else:                                   # 입력한 답이 범위에서 벗어났으면 오류 메세지 출력
        print("1 ~ 100사이의 숫자만 입력해주세요.")