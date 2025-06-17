# 세 개의 숫자를 매개변수로 받아 가장 큰 수를 반환하는 함수를 작성

# max() 버전
def max_of_three(a, b, c):
    print(max(a, b, c))

max_of_three(10, 20, 15)

# vanilla 버전
def max_of_three(a, b, c):
    max_num = a
    
    if b > a:
        print(b)
        return
    elif c > a:
        print(c)
        return
    else:
        print(max_num)
        return

max_of_three(10, 20, 15)

# sortde 버전
def max_of_three(a, b, c):
    num_list = sorted([a, b, c])
    print(num_list[-1])

max_of_three(10, 20, 15)