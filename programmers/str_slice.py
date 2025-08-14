def solution(n_str):
    # answer = list(n_str)
    # count = True
    
    # while count:
    #     if answer[0] == '0':
    #         del answer[0]
    #     else:
    #         count = False
    #         return ''.join(answer)
        
    for idx in range(len(n_str)):
        if n_str[idx] != "0":
            return n_str[idx:]

print(solution("0010"))     # 10
print(solution("854020"))   # 854020