# 정수가 담긴 리스트 num_list가 주어질 때, 
# 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 
# 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요

def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        total = 1
        for n in num_list:
            total *= n
        answer = total
    
    return answer

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))