# 파이썬의 리스트(list)를 사용하여 쇼핑 품목을 관리하는 프로그램을 작성하시오.

"""
요구 사항 (순차적으로 코드 작성)
    1.   shopping_list라는 이름의 빈 리스트를 생성
    2.   다음 품목들을 쇼핑 리스트에 추가하시오: 'milk', 'bread', 'eggs', 'apple'.
    3.   print 함수를 사용하여 현재 쇼핑 리스트의 내용을 출력합니다.
    4.   쇼핑을 시작하기 전에 'toilet paper'가 빠져 있는 것을 발견하고 리스트의 맨 앞에 추가합니다.
    5.   이번에는 'orange juice'를 리스트의 두 번째 위치에 추가하세요.
    6.   마지막으로, 'chicken', 'rice'를 리스트에 추가해야 하는데, 이 두 품목을 한 번의 연산으로 리스트에 추가하세요. (extend()함수 또는 ‘+’ 연산 사용)
    7.   각 단계 후에 쇼핑 리스트를 출력하여, 추가된 품목들을 확인할 수 있게 합니다
"""

# 빈 리스트 생성
shopping_list = []

# 품목들을 리스트에 추가
for char in ("milk", "bread", "eggs", "apple"):    # append는 하나만 추가 가능하므로 반복문으로 한 번에 작성
    shopping_list.append(char)
# shopping_list.extend(["milk", "bread", "eggs", "apple"]) extend를 쓰면 한 번에 해결 가능
print(f"현재 쇼핑 리스트: {shopping_list}")

# toilet paper를 맨 앞에 추가
shopping_list.insert(0, "toilet paper")

# orange juice를 리스트의 두 번재 위치에 추가
shopping_list.insert(1, "orange juice")

# chiken, rice를 리스트에 추가 - extend를 활용하여 한 번에 추가
shopping_list.extend(["chiken", "rice"])
print(f"최종 쇼핑 리스트: {shopping_list}")

# 슬라이싱 예제
print(shopping_list[2:5])
