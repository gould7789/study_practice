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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     for key, value in kwargs.items():
#         if value == False:
#             continue
        
#         # abs : True일 경우 모든 숫자를 절댓값으로 변환
#         if key == "abs":
#             abs_number = [abs(x) for x in args]
            
#         elif key == "only_even":
#             only_total = 0
#             for num in abs_number:
#                 if num % 2 == 0:
#                     only_total += num
#             print(f"합계는 {only_total}입니다.")

#         elif key == "unique":
#             unique_total = set(args)
#             unique_total = sum(unique_total)
#             print(f"합계는 {unique_total}입니다.")
            
#         else:
#             arg_total = sum(args)
#             print(f"합계는 {arg_total}입니다.")
        
        
# add_numbers(1, -2, 2, -3)
# add_numbers(1, -2, 2, -3, abs=True, only_even=True)
# add_numbers(1, 2, 2, 3, 3, 4, 5, unique=True)