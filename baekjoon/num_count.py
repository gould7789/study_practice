"""
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 
0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다
"""

A = int(input())
B = int(input())
C = int(input())

# 각 숫자들을 카운트 할 딕셔너리 
num_dict = {}

# 딕셔너리에 넣을 0~9 키값 생성 및 초기에는 0으로 밸류값 생성
for num in range(0, 10):
    num_dict[num] = 0

# 반복문 순회를 위해 문자열로 변환
num_list = str(A*B*C)

# 순회하며 딕셔너리에 카운트
for num in num_list:
    count = int(num)
    num_dict[count] += 1

# 밸류값만 최종 출력
for val in num_dict.values():
    print(val)