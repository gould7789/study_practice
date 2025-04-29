# 1부터 20까지의 정수 중 짝수의 합계 계산

# continue문 연습 (홀수 합계 건너뛰기)
# for문과 continue문을 사용하여 1부터 20까지의 숫자 중 홀수를 건너뛰고 짝수의 합계를 계산하라
total = 0

for num in range(1, 21):            # 1부터 20까지 반복
    if num % 2 != 0:                # 홀수일 경우 continue로 건너뛰기
        continue
    
    total += num                    # 짝수들의 합

print(f"1부터 20까지의 짝수 합계 (홀수 건너뜀): {total}")