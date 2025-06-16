# 학생의 이름과 여러 과목의 점수를 입력받아, 총 점수를 계산하는 함수 작성

def student_score(name, **scores):
    print(f"{name}의 성적:")
    
    total = 0
    for key, value in scores.items():
        print(f" -{key}: {value}점")
        total += value 
    
    print(f"총점: {total}점")

student_score("근욱", math=90, english=85, science=88)
