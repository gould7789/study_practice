"""
n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, 
arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.

0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
"""

def solution(arr):
    # 확인 하는 과정 중 일치하지 않는 부분이 있다면 0을 리턴
    for num1 in range(len(arr)):
        for num2 in range(len(arr)):
            if arr[num1][num2] != arr[num2][num1]:
                return 0

    # 모든 확인이 끝난 후 = 모두 일치함 1을 리턴
    return 1

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))   # 1
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))  # 0