# 정수 리스트 num_list와 정수 n이 주어질 때, 
# n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성

def solution(num_list, n):
    print(num_list[n-1:])


solution([2, 1, 6], 3)
solution([5, 2, 1, 7, 5], 2)
