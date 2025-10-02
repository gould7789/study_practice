"""
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)**2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {}
    
    # 각 숫자 별로 나온 횟수 딕셔너리 형태로 저장
    for num in dice:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # 인덱스로 조절하기 위해 리스트 형태로 저장
    items = list(counts.items())
    
    # 4개 모두 같은 숫자
    if len(items) == 1:
        return 1111 * items[0][0]
    
    # 3+1 or 2+2
    elif len(items) == 2:
        # 3+1
        if items[0][1] == 3 or items[1][1] == 3:
            p = items[0][0] if items[0][1] == 3 else items[1][0]
            q = items[1][0] if items[0][1] == 3 else items[0][0]
            return (10 * p + q)**2
        # 2+2
        else:
            p, q = items[0][0], items[1][0]
            return (p + q) * abs(p - q)
    
    # 2+1+1
    elif len(items) == 3:
        total = 1
        for num, cnt in counts.items():
            if cnt == 1:
                total *= num
        return total
    
    # 모든 수가 다름
    else:
        return min(dice)

print(solution(2, 2, 2, 2))     # 2222      / 1111 x 2
print(solution(4, 1, 4, 4))     # 1681      / (10 x 4 + 1)**2
print(solution(6, 3, 3, 6))     # 27        / (6 + 3) x |6 - 3|
print(solution(2, 5, 2, 6))     # 30        / 5 x 6
print(solution(6, 4, 2, 5))     # 2         / 가장 작은 수 2