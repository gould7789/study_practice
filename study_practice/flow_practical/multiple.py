# 1에서 1000 사이의 정수 중 3의 배수 합 구하기

# while문을 사용하여 1~1000까지의 정수 중 3의 배수의 총합을 구하라

count = 0       # while 종료 조건인 카운트 변수 선언
total = 0       # 3의 배수들의 합을 저장할 변수 선언

while count < 1001:     # 1000까지 반복할 while문 작성
    if count % 3 == 0:  # 3의 배수
        total += count  # 3의 배수의 합
    count += 1
    
print(f"1~1000 사이 정수 중 3의 배수의 총 합은 : {total}")  