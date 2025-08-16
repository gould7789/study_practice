"""
문자열 배열 strArr가 주어집니다. 
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 
남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요
"""

def solution(strArr):
    answer = []
    # "ad"를 포함하고 있는지 확인
    for word in strArr:
        if "ad" not in word:
            answer.append(word)

    # 리스트 컴프리핸션
    answer = [word for word in strArr if "ad" not in word]

    return answer

print(solution(["and","notad","abcd"]))
print(solution(["there","are","no","a","ds"]))