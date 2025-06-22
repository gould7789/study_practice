# 빙고 게임 프로그램 작성
import random

# 사용자로부터 크기 N을 입력받는다. N은 3 이상 6 이하의 정수여야 한다.
while True:
    N = int(input("빙고 보드의 사이즈를 입력해주세요: "))
    if 3 <= N <= 6:
        break
    else:
        print("3~6 사이의 숫자를 입력해주세요.")

bingo_number = []

while True:
    rand_num = random.randint(1, 36)
    
    if rand_num in bingo_number:
        continue
    else:
        bingo_number.append(rand_num)
    
    if len(bingo_number) == N**2:
        break

count = 0
check_list = ["*" for _ in range(N)]

while True:
    enter = input("Press Enter to generate a random number: ")
    rand_num = random.randint(1, 36)
    count += 1
    bingo_count = 0
    print(f"Random Number {count}: {rand_num}")
    
    for col in range(1, (N**2) + 1):
        if bingo_number[col - 1] == rand_num:
            bingo_number[col - 1] = "*"
        print(bingo_number[col - 1], end=" ")
        if col % N == 0:
            print()
    
    for width in range(0, N**2, N):
        if bingo_number[width : width + N] == check_list:
            bingo_count += 1
        
    for height in range(N):
        if bingo_number[height::N] == check_list:
            bingo_count += 1
    
    if bingo_number[::N + 1] == check_list:
        bingo_count += 1
    
    if bingo_number[N-1:N**2 - N + 1:N - 1] == check_list:
        bingo_count +=1
    
    print(bingo_count)
    
    if bingo_count >= 2:
        break