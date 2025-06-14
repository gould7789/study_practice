# 사용자로부터 난수 생성 개수와 범위를 입력받아 리스트에 난수를 저장하고
# 가장 자주 등장한 숫자 3개를 출력하는 프로그램을 작성

"""
문제 설명
    ▶ 사용자로부터 다음 3개의 입력을 받는다
        - N: 생성할 난수의 개수
        - A: 난수 발생 시작값
        - B: 난수 발생 끝값
    ▶ A ~ B 범위의 난수를 N개 생성하여 리스트에 저장한다.
    ▶ 리스트에서 가장 빈도수가 높은 숫자 3개를 찾아 출력하라.
        -  동점으로 인해 3개가 넘는 경우에는 모두 출력하라
    ▶ 출력은 숫자와 발생 횟수와 함께 출력하라.
"""

import random

# 사용자에게 난수의 개수를 입력 받음
N = int(input("난수 개수를 입력하세요: "))

# 난수의 시작 범위
A = int(input("시작 범위를 입력하세요: "))

# 난수의 끝 범위
B = int(input("끝 범위를 입력하세요: "))

# 난수 출력
rand_num = [random.randint(A, B) for _ in range(N)]

# 고유 숫자 리스트 출력
unique_num = random.sample(range(A, B + 1), B)
print(f"고유 숫자 리스트: {unique_num}")

# 각 숫자마다 나온 빈도 수 출력
index_num = [rand_num.count(idx) for idx in unique_num]
print(f"빈도 수 리스트: {index_num}")

# 가장 많이 등장한 숫자 top3(동점 포함)
top3 = 0    # 3등이 나올 때까지 카운팅
print("\n가장 많이 등장한 숫자 TOP 3 (동점 포함): ")

# 3위까지 순위가 매겨지면 반복 종료
while top3 < 3:
    max_num = max(index_num)    # 가장 높은 빈도 수 출력
    
    if max_num == 0:            # 모든 빈도 수가 0이 되면 반복 종료
        break
    
    # 난수의 범위만큼 반복
    for num in range(len(unique_num)):
        if index_num[num] == max_num:   # 특정 인덱스의 빈도 수와 최고 빈도 수가 같으면
            print(f"{unique_num[num]} -> {index_num[num]}회")   # 특정 인덱스 자리의 숫자와 등장 횟수 출력
            index_num[num] = 0           # 다음 반복에 그 숫자가 출력되지 않도록 인덱스 0으로 업데이트
    
    # 3위까지만 출력되도록 카운팅        
    top3 += 1 