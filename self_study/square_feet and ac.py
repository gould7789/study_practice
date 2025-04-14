# 사용자가 제곱미터(m²) 단위로 입력한 토지의 면적을 평방피트(ft²)와 에이커(ac)
# 단위로 변환해주는 프로그램을 작성하세요. 변환 공식은 다음과 같습니다
# – 1제곱미터 (m²) = 10.7639 평방피트 (ft²)
# – 1에이커 (ac) = 4046.86 제곱미터 (m²)



# 공식을 사용하여 면적을 평방피트(ft²)와 에이커(ac)로 변환
# 두 개의 함수를 정의하여 각 단위로의 변환을 담당


# convert_to_square_feet: 제곱미터를 평방피트로 변환
def convert_to_square_feet(square_meters):
    return f"{square_meters} 제곱미터는 {square_meters * 10.7639} 평방비트입니다."
    
# convert_to_acres: 제곱미터를 에이커로 변환 
def convert_to_acres(square_meters):
    return f"{square_meters} 제곱미터는 {square_meters / 4046.86} 에이커입니다."
   
# 사용자로부터 토지의 면적을 제곱미터(m²) 단위로 입력
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

# 변환된 면적을 평방피트와 에이커 단위로 출력
if square_meters > 0:
    print(f"{convert_to_square_feet(square_meters)}\n{convert_to_acres(square_meters)}")
else:
    print("잘못된 입력입니다.")







