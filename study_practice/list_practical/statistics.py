# 주어진 수치 데이터(리스트)를 기반으로 편차, 분산, 표준편차를 직접 계산하는 프로그램 작성

"""
▶ 사용자로부터 리스트의 개수를 입력받는다.
▶ 입력받은 개수는 반드시 5 이상 20 이하여야 하며, 범위를 벗어날 경우 에러 메시지를 출력하고 종료한다.
▶ 리스트의 길이만큼 1~100 사이의 정수 난수를 생성해 리스트를 구성한다.
▶ 리스트에 포함된 수를 이용해 다음 값을 직접 계산한다
"""
import random
import math



# 사용자로부터 리스트의 개수 입력
user_input = int(input("리스트 개수를 입력하세요 (5~20): "))

# 범위 내의 숫자 입력시
if 5 <= user_input <= 20:
    # 리스트의 길이만큼 1~100 사이의 난수를 생성
    rand_list = [random.randint(1, 100) for _ in range(user_input)]
    
    # 평균 : 모든 값을 더해서 개수로 나눈 값
    total = 0
    for num in rand_list:
        total += num
    mean = total / user_input
    
    # 편차 : 각 수가 평균과 얼마나 차이나는지 나타내는 값
    deviation = []
    for num in rand_list:
        deviation.append(num - mean)    # 편차 = 각값 - 평균
        
    # 분산 : 편차들을 제곱해서 평균 낸 것
    total = 0
    for num in deviation:
        total += num ** 2               # 편차들을 제곱해서 값을 더함
    variance = total / user_input       # 모든 편차 제곱의 합 /  데이터 개수
    
    # 표준편차 : 분산의 제곱근을 씌운 값
    standard_deviation = math.sqrt(variance)

    # 최종 출력
    print(f"""생성된 리스트 : {rand_list}
평균 : {round(mean, 2)}
편차 : {[round(deviation_list, 2) for deviation_list in deviation]}
분산 : {round(variance, 2)}
표준편차 : {round(standard_deviation, 2)}""")

# 범위 외의 숫자를 입력시 오류 메시지 출력
else:
    print("오류: 리스트 개수는 5 이상 20 이하여야 합니다.")