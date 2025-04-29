# while문을 사용하여 삼각형을 출력
count = 1

while count < 6:            # 카운트가 6이 되면 종료되는 반복문 작성
    for _ in range(count):  # 카운트만큼 반복되는 for문 작성
        print("*", end="")  # 카운트만큼 *을 출력하도록 end="" 
    print()                 # 카운트만큼 *을 출력한 뒤 줄바꿈
            
    count += 1