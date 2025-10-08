# 메모리 효율성을 위해 sys 모듈 사용
import sys

# 사용자에게 수의 갯수를 입력 받음
N = int(sys.stdin.readline())

# [0]으로 이루어진 리스트 생성
count = [0]*10001

# 갯수만큼 반복해서 정수를 입력 받음
for _ in range(N):
    num = int(sys.stdin.readline())
    # 입력한 숫자 = 인덱스의 빈도 수를 저장
    count[num] += 1
    

# 출력
for i in range(1, 10001):
    if count[i] != 0:
        # 그 정수의 빈도수만큼 반복 -> 빈도수만큼 정수 출력
        for _ in range(count[i]):
            # sys는 문자열을 출력하기 때문에 문자열로 변환 필수
            sys.stdout.write(str(i) + "\n")


