# 논리 연산자 : 진리표를 활용한 연산 실시
# 논리 연산자 종류 : and or not

# and 연산자
# - 이항 연산자
# - 좌항과 우항의 값이 "참"일때만 참,
# - 그 이외에는 모두 거짓

if 3 < 2 and 3 < 3:
    print("T 1")

if 3 > 2 and 3 < 3:
    print("T 2")

if 3 < 2 and 3 >= 3:
    print("T 3")

if 3 > 2 and 3 >= 3:
    print("T 4")