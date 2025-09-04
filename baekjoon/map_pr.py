while True:
    a, b, c = map(int, input().split())
    num_list = [a, b, c]
    total = sorted(num_list)
    
    result = ""
    
    if a == 0 and b == 0 and c == 0:
        break
    elif (total[0]**2) + (total[1]**2) == (total[2]**2):
        result = "right"
    else:
        result = "wrong"
    
    print(result)