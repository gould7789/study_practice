"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
"""

def solution(arr, queries):
    result = [] # 최종 결과값 저장
    for n1, n2, n3 in queries:  # n1 = 시작 범위, n2 = 끝 범위, n3 = 비교 숫자
        s_list = arr[n1:n2+1]   # 범위에 따라 슬라이싱 하여 비교
        min_list = []           # n3보다 큰 숫자들을 저장하고 그 중에서 가장 작은 숫자를 판별하기 위한 리스트
        
        # 슬라이싱한 리스트의 숫자들 중 n3보다 큰 숫자들은 min_list에 저장
        for num in s_list:
            if num > n3:
                min_list.append(num)        
                
        # min_list가 비어있으면 -1 추가        
        if len(min_list) == 0:
            result.append(-1)
        # min_list에 숫자가 있다면 그 중에서 가장 작은 숫자를 결과값 리스트에 추가
        else:
            result.append(min(min_list))
                
    return result

print(solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]]))