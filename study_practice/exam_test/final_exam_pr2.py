# 주사위 던지기 결과의 빈도를 분석하고, 히스토그램을 통해 결과를 시각화 하는 프로그램을 작성
import random

# 주사위 숫자별 나온 횟수를 카운팅 하는 딕셔너리
dice = {}

while True:
    # 사용자로부터 주사위를 던질 횟수를 입력받는다
    user_input = int(input("주사위를 던질 횟수를 입력해주세요(100 ~ 1,000,000): "))
    if 100 <= user_input <= 1000000:
        
        # 사용자가 입력한 횟수만큼 주사위를 던지고 나온 숫자를 카운팅
        for _ in range(user_input):
            num = random.randint(1, 6)
            if num in dice:             # 딕셔너리안에 그 숫자가 있으면 +1 카운팅
                dice[num] += 1
            else:                       # 숫자가 최초로 나오면 딕셔너리에 1 카운팅 하며 업데이트
                dice[num] = 1
        
        # 최댓값 구하기
        max_num = -1
        for key, value in dice.items():
            if value > max_num:
                max_num = value         # 값을 순회하며 가장 높은 값 찾아내기
        
        # 결과 시각화
        print("Dice Roll Frequency Histogram:")
        for i in range(1, 7):
            count = dice[i]     # 각 주사위 값을 밸류값 = 나온 횟수
            star_count = "*" * int(((count / max_num) * 10))    # 최대치에 대한 상대적인 비율
            percent = (count / user_input) * 100                # 확률
            
            # 최종 출력
            print(f"{i}: {star_count:<10} ({count} times, {percent:.2f}%)")
        break
    
    else:
        print("범위 사이의 숫자를 입력해주세요.")