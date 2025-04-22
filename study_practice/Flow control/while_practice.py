"""
동작 절차
1. while의 조건식이 “참”인 동안 while 블록 내 코드 실행
2. 일반적으로 반복 횟수가 일정하게 정해지지 않을 경우 사용
"""

flag = True
while flag :
    value = int(input("양의 정수를 입력하세요: "))
    
    if value > 0:
        print("입력 값 : ", value)
    else:
        flag = False            # 조건식이 False가 되는 조건을 잘 정해야 함
                                # 조건이 잘 못될 경우 무한루프