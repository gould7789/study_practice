"""
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요
"""
# vanilla
def solution(my_string, overwrite_string, s):
    answer = ""
    word = "".join(my_string)
    str_list = list(word)
    
    for num in range(s, len(overwrite_string) + s):
        str_list[num] = overwrite_string[num - s]
    
    for i in str_list:
        answer += i
    
    return answer


# 슬라이싱 버전
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

print(solution("He11oWor1d", "lloWorl", 2))     # "HelloWorld"
print(solution("Program29b8UYP", "merS123", 7)) # ProgrammerS123     