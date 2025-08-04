"""
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_strings, parts):
    answer = ''
    
    # zip을 사용하여 두 리스트를 순서대로 짝지은 뒤 언팩킹
    for str, (n1, n2) in zip(my_strings, parts):
        answer += str[n1:n2+1]
    
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))