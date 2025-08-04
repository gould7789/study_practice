"""
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요
"""

def solution(my_string, queries):
    # 인덱스로 조절하기 위해 리스트로 변환
    s_list = list(my_string)
    
    # 인덱스 좌변 슬라이싱으로 뒤집기
    for n1, n2 in queries:
        s_list[n1:n2+1] = s_list[n1:n2+1][::-1]
    
    # 최종 출력을 위해 문자열로 변환
    answer = ''.join(s_list)
    return answer

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))