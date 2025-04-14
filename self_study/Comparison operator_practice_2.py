record = 70

# 주어진 점수에 대해 A ~ F 등급으로 출력 프로그램
# if ~ elif ~ else 문 활용

if record >= 90:        # 90 이상
    print("A")
elif record >= 80:      # 80 이상 and 90 미만
    print("B")
elif record >= 70:      # 70 이상 and 80 미만
    print("C")
elif record >= 60:      # 60 이상 and 70 미만
    print("D")
else:                   # 60 미만
    print("F")
    
# if는 한 개의 조건을 순차적으로 비교하면서 출력