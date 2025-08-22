"""
문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 
가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요
"""

def solution(strArr):
    # vanilla
    word_count = {}

    for word in strArr:
        if len(word) not in word_count:
            word_count[len(word)] = 1
        else:
            word_count[len(word)] += 1

    # get 버전
    another = {}

    for i in strArr:
        # 딕셔너리에 그 요소가 이미 있을시 기존 요소에 +1
        # 딕셔너리에 그 요소가 아직 없을시 새롭게 만들며 0+1
        another[len(i)] = another.get(len(i), 0) + 1

    return max(word_count.values()), max(another.values())

print(solution(["a","bc","d","efg","hi"]))