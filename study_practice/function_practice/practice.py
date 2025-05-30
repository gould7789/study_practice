# 함수 정의 
# -> 자기만의 함수를 만들고 싶을 때

def bar(word): # parametor(매개변수) -> word 
    print(f"hello world {word}")
    
bar("안녕") # argument(인자값) -> "안녕"

def get_input_num():
    msg = "정수를 입력하세요: "
    input_value = int(input(msg))
    
    if input_value < 0:
        print("0과 양의 정수만 입력하세요")
        return
    
    return input_value

# value = get_input_num()
# print(value, type(value))

values = [get_input_num() for _ in range(3)]
print(values)