"""
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 
이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오
"""

# 각 변수에 정수 입력
c, d, e, f, g, a, b, C = [num for num in range(1, 9)]
# 비교를 위해 리스트로 변환
num_list = [c, d, e, f, g, a, b, C]

# 사용자 입력
sound_list = list(map(int, input().split()))

# 최종 출력을 위한 변수
result = ""

# 순서대로 입력
if sound_list == num_list[:8]:
    result = "ascending"
# 반대로 입력
elif sound_list == num_list[::-1]:
    result = "descending"
# 그 외
else:
    result = "mixed"
    
# 최종출력
print(result)