"""
*
**
***
****
*****
"""
# 1번 연습
row = 5

for i in range(1, row + 1):
    print("*" * i)

"""
    *
   **
  ***
 ****
*****
"""
# 2번 연습
for i in range(1, row + 1):
    print(" " * (row - i) + "*" * i)

"""
    *
   ***
  *****
 *******
*********
"""
# 3번 연습
for i in range(1, row + 1):
    print(" " * (row - i) + "*" * (2 * i - 1))

"""
*********
 *******
  *****
   ***
    *
"""
# 4번 연습
for i in range(1, row + 1):
    print(" " * (i - 1) + "*" * (2 * (row - i) + 1))