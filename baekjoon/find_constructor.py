"""
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다.
따라서 245는 256의 생성자가 된다. 
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오
"""

# N이 M의 생성자
def solution(N):
    # 1 ~ N까지 순회
    for num in range(1, N+1):
        # 정답으로 쓸 num은 따로 선언
        current = num
        # num을 문자형을 변환하여 숫자 하나씩 순회
        for i in str(num):
            current += int(i)
        
        # current가 N과 같다면 num 반환
        if current == N:
            return num
    
    # 생성자가 없을시 0 반환
    return 0

user_input = int(input())
print(solution(user_input))