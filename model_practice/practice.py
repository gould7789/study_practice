import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 준비
x = [val for val in range(-10, 11)]
y1 = [2*val for val in x]
y2 = [4*val for val in x]
y3 = [8*val for val in x]

# 선 그래프
plt.plot(x, y1, label = "2x")
plt.plot(x, y2, label = "4x")
plt.plot(x, y3, label = "8x")

# 그래프 꾸미기
plt.legend()
plt.title("그래프")
plt.xlabel("x 축")
plt.ylabel("y 축")
plt.grid(True)

# 그래프 출력
plt.show()