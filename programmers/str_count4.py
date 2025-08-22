"""
문자열 myString과 pat이 주어집니다. 
myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString, pat):
    word = ""
    count = 0

    # vanilla
    for c in myString:
        word += c
        if pat in word:
            count += 1
            word = word[-(len(pat)-1):]

    # 슬라이싱
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            count += 1

    return count

print(solution("banana", "ana"))
print(solution("aaaa", "aa"))