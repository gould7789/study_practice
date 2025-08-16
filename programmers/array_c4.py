"""
정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요
"""

# 리스트 컴프리핸션을 이용
def solution(arr, n):
    # 배열의 길이가 홀수 일 때
    if len(arr) % 2 != 0:
        return [num + n if idx % 2 == 0 else num for idx, num in enumerate(arr)]

    # 배열의 길이가 짝수 일 때 
    else:
        return [num + n if idx % 2 != 0 else num for idx, num in enumerate(arr)]

print(solution([49, 12, 100, 276, 33], 27))
print(solution([444, 555, 666, 777], 100))