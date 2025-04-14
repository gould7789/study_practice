# 구구단 프로그램: 2단부터 9단까지의 구구단을 출력합니다.

for factor in range(2, 10): # 2부터 9까지 곱해질 단 숫자 출력
    for multipli in range(1, 10): # 1부터 9까지 곱할 숫자 출력
        print(factor, "X", multipli, "=", factor * multipli)
    print("------------") # 단이 바뀌면 구분선 출력