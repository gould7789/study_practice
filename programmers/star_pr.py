"""
직사각형 형태의 그림 파일이 있고, 
이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 
이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요
"""

def solution(picture, k):
    answer = []
    
    for row in picture:
        # 가로
        extand_row =  "".join(x * k for x in row)   # 문자열 순회를 통해 문자 하나당 k번씩 출력
        
        # 세로
        for _ in range(k):
            answer.append(extand_row)
            
    # replace 버전
    answer_2 = []
    
    # replace 함수를 통해 각 문자를 k번 곱한 것으로 변경
    for i in range(len(picture)):
        for _ in range(k):
            answer_2.append(picture[i].replace(".", "."*k).replace("x", "x"*k))
        
    return  "\n".join(answer_2)

print(solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2))
print(solution(["x.x", ".x.", "x.x"], 3))