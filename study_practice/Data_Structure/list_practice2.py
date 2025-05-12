# 리스트의 순서 유지 예제
numbers = [4, 1, 3, 2]
print(f"원래 순서: {numbers}")

# 리스트 가변성 예제 - 요소 추가 및 삭제
numbers.append(5)   # 요소 5 추가
print(f"요소 추가 후: {numbers}")

numbers.remove(2)   # 요소 2 삭제
print(f"요소 삭제 후: {numbers}")

# 리스트 타입 다양성 예제
mixed_list = [1, "apple", 3.14, [2, 4, 6], True]
print(f"혼합 데이터 타입 리스트: {mixed_list}")

# 리스트 컴프리헨션(list comprehension) 예제

# 0부터 9까지의 숫자의 제곱으로 리스트 생성
squares = [x**2 for x in range(10)]
print(f"리스트 컴프리헨션: {squares}")