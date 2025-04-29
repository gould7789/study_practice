# 별 다이아몬드 출력

# 높이가 5인 다이아몬드 형태의 별을 출력

row = 5

for row_num in range(1, row + 1):               # 1부터 5까지 반복
    
    for _ in range(row - row_num):              # 반복 할수록 공백 감소
        print(" ", end="")
        
    for _ in range(row_num * 2 - 1):            # 반복 할수록 별 갯수 증가
        print("*", end="")
        
    print()
    

for row_num2 in range(1, row):                  # 1부터 4까지 반복
    
    for _ in range(row_num2):                   # 반복 할수록 공백 증가
        print(" ", end="")
        
    for _ in range(2 * (row - row_num2) - 1):   # 반복 할수록 별 갯수 감소
        print("*", end="")
        
    print()