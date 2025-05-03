# continue 하위 문장을 실행하지 않고, 반복문 조건식으로 이동

for value in range(1, 6):
    print(value)
    
    if value == 2:
        continue    # 현 시점에서 실행을 중지하고 반복문의 조건식으로 이동
    
    print("--------")
    
print("End")