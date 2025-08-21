"""
정수가 있을 때, 짝수라면 반으로 나누고, 
홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다.
정수들이 담긴 리스트 num_list가 주어질 때, 
num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요
"""

def solution(num_list):
    # 연산 횟수를 카운팅
    count = 0

    for num in num_list:
        while True:
            # 숫자가 1일 때 카운팅
            if num == 1:
                break

            # 숫자가 홀수일 때 -1을 함
            elif num % 2 != 0:
                num -= 1
            
            # 짝수일 때는 반으로 나눔
            else:
                num //= 2
                count += 1
            
        # 홀수일 때 1을 빼고 2로 나눈다는 것  = 몫을 구하겠다는 뜻이므로 이 풀이도 가능    
        # while != 1:
            # num //= 2
            # count += 1

    return count

print(solution([12, 4, 15, 1, 14]))