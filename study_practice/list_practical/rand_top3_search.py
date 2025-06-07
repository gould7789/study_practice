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


# 사용자로부터 다음 3개를 입력 받는다

# N : 생성할 난수의 개수
N = int(input("난수 개수를 입력하세요: "))
# A : 난수 발생 시작값
A = int(input("시작 범위를 입력하세요: "))
# B : 난수 발생  끝값
B = int(input("끝 범위를 입력하세요: "))

# 빈도수를 저장하는 리스트
word_use_count = []

# A~B 범위의 난수를 N개 생성하여 리스트에 저장한다
rand_list = [random.randint(A, B) for _ in range(N)]    # 랜덤 난수 리스트
num_list = random.sample(range(A, B + 1), B)    # 고유 숫자 리스트

# 빈도 수 리스트 출력
for idx in num_list:
    word_use_count.append(rand_list.count(idx))

print(f"고유 숫자 리스트: {num_list}")
print(f"빈도 수 리스트: {word_use_count}\n")

# 리스트에서 가장 빈도수가 높은 숫자 3개를 찾아 출력
top3 = 0   # 가장 많이 등장한 숫자 카운팅
print("가장 많이 등장한 숫자 Top 3 (동점 포함): ")

while top3 < 3:    # 많이 등장한 숫자 top3가 완성되면 반복 종료
    max_value = max(word_use_count) # 순위 선별을 위해 빈도수 출력
    
    # 빈도수 리스트의 숫자들이 모두 0이 되면 반복 종료
    if max_value == 0:
        break
    
    # 빈도수 리스트만큼 반복
    for num in range(len(word_use_count)):
        if word_use_count[num] == max_value:    # 빈도수 리스트의 숫자와 최고 빈도수가 일치하면
            print(f"{num_list[num]} -> {word_use_count[num]}회")    # 그 숫자와 빈도수 출력
            word_use_count[num] = 0             # 그 숫자를 0으로 만들어 카운팅에서 제외
            
    top3 += 1