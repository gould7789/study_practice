# 다른 옵션
"""
1. 왼쪽-> 오른쪽 대각선
2. 오른쪽 -> 왼쪽 대각선
3. 테두리
4. 양방향 대각선
"""

"""
*  
 *
  *
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
    
    
"""
  *
 *
*
"""
for row_num in range(row):
    for col_num in range(col):
        if row_num + col_num == col - 1:
            print("*", end="")
        else:
            print(" ", end="")
        
    print()

"""
***
* *
***
"""
for row_num in range(row):
    for col_num in range(col):
        if row_num == 0 or row_num == 2:
            print("*", end="")
        elif col_num == 0 or col_num == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()