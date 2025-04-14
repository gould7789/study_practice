# 비교 연산자 : 좌항과 우항의 값을 비교
# 비교 연산자 종류 : >, >=, <, <=, ==, !=

print(3 > 4)         # false
print(2 > 2)         # false
print(2.0 >= 2)      # true
print(3 < 4)         # true
print(4 <= 4)        # true
print(1 == 1)        # true
print(1 != 2)        # true
print(True != False) # true


# 문자열 비교는 유니코드에 따라서 결정 됨
#     97    99
print("a" > "c")     # false

# 유니코드 출력 및 확인이 필요한 경우 print(ord("a")) 등으로 확인

print(2 < 3.0)       # true
print("2" == 2)      # false
print(3.0 != 4)      # true


#### 비교 연산자의 결과 값은 항상 Boolean형 ####

