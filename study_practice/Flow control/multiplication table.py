# 구구단 작성


num = 0

# 2, 4, 6, 8 짝수 단을 작성
for num in range(2, 10):
    for dan in range(1, 10):
        if num % 2 == 0:
            print(f"{num} X {dan} = {num * dan}")
            
    if num % 2 == 0:
        print("=================")