# 반복 할 횟수
r = int(input())

for _ in range(r):
    # 값 두개를 입력 받아 각각 정수형, 변수형으로 변환 시켜주기
    input_value = input().split()

    # 정수형 변환
    int_value = int(input_value[0])
    # 문자형 변환
    str_value = input_value[1]
    
    # 반복 출력
    for word in str_value:
        print(int_value*word, end="")
        print()