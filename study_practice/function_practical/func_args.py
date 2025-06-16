# 가변 개수의 숫자를 매개변수로 받아 입력
# 입력 값의 개수, 합계, 평균을 반환하는 함수 작성

def calculate_average(*args):
    count = len(args)
    total = sum(args)
    average = total / count if count > 0 else 0
    
    print(f"입력 개수: {count}")
    print(f"총합: {total}")
    print(f"평균: {average:.2f}")
    
    return count, total, average

n, s, avg = calculate_average(70, 80, 90)
n, s, avg = calculate_average(70, 80, 90, 100, 200)