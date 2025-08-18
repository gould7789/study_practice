""" 
단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
 my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요
"""

def solution(my_string):
    # 공백의 갯수까지 정리하고 싶을 때
    answer = [word for word in my_string.split(" ") if word != ""]
    
    # 단어만 뽑아내고 싶을 때
    answer = my_string.split()
    
    return answer

print(solution(" i    love  you"))
print(solution("    programmers  "))