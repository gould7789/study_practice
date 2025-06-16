# 리스트와 타겟 숫자를 배개변수로 받아, 타겟 숫자가 리스트 내에 있는지 여부를 반환하는 함수

def contains(list, target):
    for num in list:
        if target == num:
            return "True"
    
    return "False"

print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))