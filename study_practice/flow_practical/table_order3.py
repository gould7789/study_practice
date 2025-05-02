# 다른 옵션
"""
1. 테두리
2. 왼쪽-> 오른쪽 대각선
3. 오른쪽 -> 왼쪽 대각선
4. 양방향 대각선
"""

row = 3
col = 3
for row_num in range(row):
    for col_num in range(col):
        # if row_num == col_num:
        #     print("*", end="")
        # else:
        #     print(" ", end="")
        print("*" if row_num == col_num else " ", end= "")
    print()