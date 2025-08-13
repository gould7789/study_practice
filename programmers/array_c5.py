"""
정수 배열 arr와 query가 주어집니다.
query를 순회하면서 다음 작업을 반복합니다.
짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr, query):
    answer = arr
    
    # 인덱스와 그 인덱스의 숫자 순회
    for idx, num in enumerate(query):
        # 짝수 인덱스
        if idx % 2 == 0:
            answer = answer[:num+1]
        # 홀수 인덱스
        else: 
            answer = answer[num:]
    
    return answer

print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))