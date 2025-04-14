# or 연산자
# - 이항 연산자
# - 좌항과 우항 값 중 하나라도 "참"이면 참
# - 그 외에는 모두 거짓

if 3 < 2 or 3 < 3:
    print("T 1")

if 3 > 2 or 3 < 3:
    print("T 2")
    
if 3 > 2 or 3 >= 3:
    print("T 3")
    
if 3 > 2 or 3 >= 3:
    print("T 4")