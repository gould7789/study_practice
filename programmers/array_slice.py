"""
정수 배열 arr가 주어집니다. 
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.
"""

def solution(arr):
    # 배열을 순회하며 2를 만나면 인덱스를 저장
    idx_2 = [idx for idx, num in enumerate(arr) if num == 2]
    
    # 인덱스를 이용하여 arr리스트를 슬라이싱
    return arr[idx_2[0]:(idx_2[-1]+1)] if idx_2 else [-1]

print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))