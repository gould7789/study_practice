def solution(names):
    answer = []
    for idx in range(0, len(names), 5):
        answer.append(names[idx])
    
    # 컴프리핸션 버전
    result = [names[name] for name in range(0, len(names), 5)]
    return result # or names[::5]


print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))