def plot(*args):# 함수로 받는 모든 변수들을 패킹
    last_index = len(args) - 1
    msg = "[ "
    
    for idx, val in enumerate(args):
        msg += str(val) + ", " if idx != last_index else str(val)
    msg += " ]"
        
    print(msg)
    # print(len(args), args)
    
# 함수 호출
plot(1)
plot(1, 2)
plot(1, 2, "hello")


def prt_elements(a, b, c, *d, e = 1000):
    print(a, b, c, d, e)
    
prt_elements(1, 2, 3)