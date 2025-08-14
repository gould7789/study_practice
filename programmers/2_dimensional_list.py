"""
정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
"""

# n의 갯수에 맞게 배열을 넣고, n에 맞게 0을 넣은 뒤, 순서에 맞게 1을 넣는다

def solution(n):
    answer = []
    # n개의 리스트 삽입
    for num in range(n):
        input_list = [] # 1차원 리스트 작성

        # 리스트 안의 1 또는 0 삽입
        for _ in range(n):
            input_list.append(0)

        # 인덱스 순서에 맞게 1 삽입
        input_list[num] = 1

        # 완성된 리스트를 최종 결과 리스트에 삽입
        answer.append(input_list)
    

    # 리스트 컴프리핸션
    answer = [[0]*n for _ in range(n)]
    for num in range(n):
        answer[num][num] = 1

    return answer

print(solution(3))  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(solution(6))  # [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
print(solution(1))  # [[1]]