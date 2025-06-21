# 가변 인자와 키워드 인자를 활용한 다중 계산 함수 구현

def calculate(*args, **kwargs):
    if args and kwargs:
        keys = kwargs.keys()
    
        # 허용되지 않은 키워드가 포함된 경우 None 반환
        for key in keys:
            if key != "avg" and key != "sum" and key != "max" and key != "min":
                return
        
        # sum = 합계 계산
        if "sum" in keys and kwargs["sum"] == True:
            total = 0
            for num in args:
                total += num
            kwargs["sum"] = total
        
        # avg = 평균값 계산
        if "avg" in keys and kwargs["avg"] == True:
            total = 0
            for num in args:
                total += num
            total = total / len(args)
            kwargs["avg"] = total
        
        # max = 최댓값 계산
        if "max" in keys and kwargs["max"] == True:
            max_num = args[0]
            
            for num in args:
                if num > max_num:
                    max_num = num
                kwargs["max"] = max_num
        
        # min = 최솟값 계산
        if "min" in keys and kwargs["min"] == True:
            min_num = args[0]
            
            for num in args:
                if num < min_num:
                    min_num = num
                kwargs["min"] = min_num
        
        return kwargs

    # args, kwargs 둘 중 하나도 들어오지 않았으면 None 반환
    else:
        return

print(calculate(10, 20, 30, avg=True))
print(calculate(1, 2, 3, sum=True, max=True))
print(calculate(100, 50, 200, min=True, max=True, avg=True))

print(calculate(avg=True))
print(calculate(1, 2, 3))
print(calculate(1, 2, 3, total=True))