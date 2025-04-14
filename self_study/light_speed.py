"""
사용자로부터 거리를 입력받아
빛이 해당 거리를 여행하는 데 걸리는 시간을
계산하는프로그램을 작성
"""

# 빛의 속도
speed_of_light = 299792

# 사용자로부터 거리를 킬로미터 단위로 입력
distance = float(input("여행 할 거리를 킬로미터(km) 단위로 입력하세요: "))

# 빛이 해당 거리까지 걸리는 시간 계산 및 출력
time = distance / speed_of_light

print("빛이", distance, "킬로미터를 여행하는 데 걸리는 시간은", time, "초입니다.")