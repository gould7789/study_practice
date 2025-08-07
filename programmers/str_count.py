"""
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요
"""

def solution(my_string):
    answer = []
    
    for asc in range(60, 91):
        answer.append(my_string.count(chr(asc)))
    
    for asc in range(97, 123):
        answer.append(my_string.count(chr(asc)))
    
    return answer

print(solution("Programmers"))