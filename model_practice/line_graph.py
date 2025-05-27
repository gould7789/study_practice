import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 데이터 준비
# 2차원 선형
x = [val for val in range(-10, 11)]
# y = [val**2 for val in x]
y1 = [2*val for val in x]
y2 = [4*val for val in x]
y3 = [8*val for val in x]

# 그래프
plt.plot(x, y1, label = "2x", color = "black")
plt.plot(x, y2, label = "4x", marker = "o")
plt.plot(x, y3, label = "8x", marker = "x")


# # 선 그래프
# plt.plot(x, y)
# # plt.plot(x, x)

# # 산점도 그래프
# plt.scatter(x, y, color = "red", label = "scatter")
# plt.bar(x, y, label = "bar")   # 바 그래프

# 그래프 꾸미기
plt.legend()
plt.title("A 그래프")
plt.xlabel("x 축")
plt.ylabel("y 축")
plt.grid(True)

# 그래프 출력
plt.show()