"""
이차원 정수 배열 arr이 매개변수로 주어집니다. 
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 
각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요
"""

def solution(arr):
    # 리스트의 갯수 = 행, 리스트 안의 요소갯수 = 열
    for row in arr:
        # 행과 열의 길이가 같을 때
        if len(arr) == len(row):
            return arr
    
        # 행이 열보다 많으면 각 리스트에 리스트 += [0]*(행 갯수 - 열 갯수)
        elif len(arr) > len(row):
            row += [0]*(len(arr)-len(row))
        
        # 열이 행보다 많으면 aar += ([0]*열 갯수) * (열 갯수 - 행 갯수)
        else:
            arr += [[0]*len(row) for _ in range(len(row)-len(arr))]
        
    return arr

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))