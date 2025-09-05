import math

# 사용자가 입력 할 정수의 갯수
user_input = int(input())
# 사용자가 정수 입력 및 리스트 변환
num_list = list(map(int, input().split()))
# 소수 갯수 카운팅
count = 0

# 그 결과 1과 본인 외 나눠지는 숫자가 없으면 소수 판정 
for num in num_list:
    # 0 or 1은 소수가 아니므로 제외
    if num <= 1:
        continue
    
    # 1부터 n의 제곱근+1까지 확인하면서 n을 나눈다
    for i in range(2, int((math.sqrt(num))+1)):
        # 본이 이외에 나눠지는 숫자가 있다면 반복 중지
        if num % i == 0:
            break
    
    # 나눠지는 숫자가 없이 이 코드까지 왔다면 count+1
    else:
        count += 1
            
print(count)