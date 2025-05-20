import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 값
x = [val for val in range(0, 21)]
y = [val*2 for val in x]
print(x)
print(y)


# 그래프 종류 선택 
plt.plot(x, y) # 선형 그래프
plt.scatter(x,y, color ="red", marker="*") # 산점도 그래프


# 그래프 꾸미기 
plt.xlabel("x 축")
plt.ylabel("y 축")
plt.title("선형 그래프")
plt.grid(True)
plt.legend()

# 그래프 출력
plt.show()