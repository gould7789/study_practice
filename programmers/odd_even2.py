"""
정수가 담긴 리스트 num_list가 주어집니다. 
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    odd_list = ""   # 홀수
    even_list = ""  # 짝수
    
    for num in num_list:
        if num % 2 == 0:
            even_list += str(num)
        else:
            odd_list += str(num)
    
    # 최종 합계
    answer = int(odd_list) + int(even_list)
    return answer

print(solution([3, 4, 5, 2, 1]))    # 393
print(solution([5, 7, 8, 3]))       # 581