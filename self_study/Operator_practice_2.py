# 몫(//), 나머지(%) 연산자
# // : 나누기 연산 후 몫 값만 변환

result_1 = 3 // 2
result_2 = 3 / 2

# 출력 값 :   1       1.5
print(result_1, result_2)

# % : 나누기 연산후 나머지 값 반환 -> Modulor 연산자
# 출력 값 : 0 1 2 0 1 2
for divisor in range(6):
    print(divisor % 3)
    
# 나머지 연산은 특정 패턴을 찾기 위해 빈번하게 사용
# 예) 특정 반복문 내에서3번째 반복마다 특정 명령어 실행    
count = 0

for dan in range(2, 10):
    for num in range(1, 10):
        print(dan, "X", num, "=", (dan*num))
        
       
    count += 1
    
    if count % 1 == 0:
        print("=================")