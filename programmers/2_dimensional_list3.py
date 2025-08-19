"""
2차원 정수 배열 board와 정수 k가 주어집니다.

i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요
"""

def solution(board, k):
    answer = 0
    
    for num in range(len(board)):
        for num2 in range(len(board[num])):
            if (num+num2) <= k:
                answer += board[num][num2]
    
    return answer

print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))