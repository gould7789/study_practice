count = 0
for t in range(3):                  # 3x2x4 매트릭스가 3개가 생김
    for i in range(4):              # 3x2 매트릭스가 4개가 생김
        for j in range(3):          # j, p를 묶어서 이해하며 쉬움
            for p in range(2):      # j는 행, p는 열    그러므로 3x2 매트릭스 생성
                count += 1
                print(f"{count}", end= ",")

"""
이 코드는 3x2 매트릭스를 기준으로 반복문을 돌리는 구조,
그걸 4번 반복하고, 또 그걸 3번 반복한 형태.
최종 출력은 0, 1을 72번 반복 출력하는 구조.
"""
