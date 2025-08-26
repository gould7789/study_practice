"""
0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다. 
등수가 높은 3명을 선발해야 하지만, 
개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 
전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다. 
전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 
10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요
"""


def solution(rank, attendance):
    # # 참석 가능한 학생들의 순위를 저장하는 리스트
    # std_rank = []
    
    # for idx, num in enumerate(rank):
    #     # 참석 가능한 학생
    #     if attendance[idx] == True:
    #         std_rank.append(num)
    
    # # 학생들을 성적순으로 정렬
    # fin_rank = sorted(std_rank)
    
    # a, b, c = [rank.index((fin_rank[n])) for n in range(3)]
    
    # return (10000*a) + (100*b) + c
    
    # -------------------------------
    # 튜플 형식
    std_rank = []
    
    for idx, num in enumerate(attendance):
        if num:
            std_rank.append((rank[idx], idx))
        
    std_rank.sort()
    
    return (10000*std_rank[0][1]) + (100*std_rank[1][1]) + std_rank[2][1]

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))
print(solution([1, 2, 3], [True, True, True]))
print(solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]))