# 여러 개의 정수와 함께 다양한 옵션을 입력 받아, 조건에 따라 합계를 계산하는 함수를 작성

"""
함수 요구사항
•  정수 목록은 *args로 전달됨
•  다음 키워드 인자 옵션을 **kwargs로 전달하며, 생략 시 디폴트는 False
•  abs: True일 경우 모든 숫자를 절댓값으로 변환
•  only_even: True일 경우 짝수만 합산
•  unique: True일 경우 중복을 제거하고 합산
•  이외의 키워드 인자가 입력되면 None을 반환하고 아무 계산도 하지 않음
•  최종 합계는 print()로 출력
"""

# get 사용 버전
def add_numbers(*args, **kwargs):
    key_dict = {"abs", "only_even", "unique"}   # 키의 값을 비교할 딕셔너리의 키값들
    
    # 키워드 인자의 키값이 키값 목록에 없을 경우 none 반환
    for key in kwargs.keys():
        if key not in key_dict:
            print("None")
            return
    
    number = list(args)
    
    # *인자 옵션에 따른 계산
    
    if kwargs.get("abs", False):
        number = [abs(x) for x in args]
    
    if kwargs.get("only_even", False):
        number = [x for x in number if x % 2 == 0]
    
    if kwargs.get("unique", False):
        number = [x for x in set(number)]
        
    
    result = sum(number)
    print(f"합계는 {result}입니다.")


add_numbers(1, -2, 2, -3)
add_numbers(1, -2, 2, -3, abs=True, only_even=True)
add_numbers(1, 2, 2, 3, 3, 4, 5, unique=True)
add_numbers(1, 2, 3, round=True)


# vanilla 버전
def add_numbers(*args, **kwargs):
    option = {"abs", "only_even", "unique"}
    
    for key in kwargs.keys():
        if key not in option:
            return None
    
    num_list = list(args)
    
    # 사용자가 abs 옵션을 지정했을 때 
    if "abs" in kwargs and kwargs["abs"] == True:
        for idx, num in enumerate(num_list):
            if num < 0:
                num_list[idx] = -num
        
    # 사용자가 only_even 옵션을 지정했을 때
    if "only_even" in kwargs and kwargs["only_even"] == True:
        num_list = [num for num in num_list if num % 2 == 0]
        
    # 사용자가 unique 옵션을 지정했을 때
    if "unique" in kwargs and kwargs["unique"] == True:
        unique_list = []
        for num in num_list:
            if num not in unique_list:
                unique_list.append(num)
        num_list = unique_list
        
        
    # 총 합계 계산
    total = 0
    for num in num_list:
        total += num
    
    print(f"합계는 {total}입니다.")

add_numbers(1, -2, 2, -3)
add_numbers(1, -2, 2, -3, abs=True, only_even=True)
add_numbers(1, 2, 2, 3, 3, 4, 5, unique=True)