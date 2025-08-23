"""
정수 배열 arr가 주어집니다. 
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, 
arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다
"""

def solution(arr):
    # 횟수 카운팅
    count = 0

    while True:
        new_arr = []    # 비교하기 위해 새로운 리스트 작성

        # 조건에 맞게 리스트에 삽입
        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 != 0:
                new_arr.append(num * 2 +1)
            else:
                new_arr.append(num)
        
        # 현재 리스트와 다음 리스트가 같다면 횟수 리턴
        if arr == new_arr:
            return count
        
        arr = new_arr
        count += 1
                

print(solution([1, 2, 3, 100, 99, 98])) # 5