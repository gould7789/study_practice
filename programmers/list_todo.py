"""
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 
각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요
"""

def solution(todo_list, finished):
    answer = {}
    result = []
    for key, val in zip(todo_list, finished):
        answer[key] = val
    
    for key in answer.keys():
        if answer[key] == True:
            continue
        else:
            result.append(key)
    
    # 컴프리핸션 버전
    total = [x for idx, x in enumerate(todo_list) if not finished[idx]]
    
    return result, total


print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]))