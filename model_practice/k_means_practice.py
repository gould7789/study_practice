import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. CSV 파일에서 데이터 로드
#       - old_faithful_geyser.csv: 간헐천의 분출 시간과 대기 시간 데이터(2차원)
#       - skiprows=1: 첫 줄은 헤더이므로 건너뜀
data = np.loadtxt("old_faithful_geyser.csv", delimiter=",", skiprows=1)

# 2. 비지도 학습을 위해 전체 데이터를 그대로 사용 (X: (N, 2) 형태)
#       - 열 0: 분출 시간 (eruption duration)
#       - 열 1: 다음 분출까지의 대기 시간 (waiting time)
X = data

# 3. K-means 클러스터링 수행 (클러스터 개수 K=2)
#       - random_state: 결과 재현성을 위한 시드값 고정S
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# 클러스터 레이블 및 중심점 추출
labels = kmeans.labels_                 # 각 샘플이 속한 클러스터 번호(0 또는 1)
centroids = kmeans.cluster_centers_     # 각 클러스터의 중심 좌표

# 4. Cost Function (SSE: Sum of Squared Errors) 출력
#       - inertia_: 각 점과 해당 클러스터 중심점 간 거리 제곱의 총합 
print(f"SSE : {kmeans.inertia_:.2f}")

# 5. 결과 시각화
plt.figure(figsize=(8, 6))

# 데이터 포인트 산점도 (색상은 클러스터 레이블에 따라 지정)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=80, cmap='Accent', label='Points')

# 클러스터 중심점 표시 (빨간색 X 마커)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')

# 그래프 정보 설정
plt.xlabel("Eruption duration (min)")   # x축: 분출 시간
plt.ylabel("Waiting tim (min)")         # y축: 대기 시간
plt.title("K-means Clustering (NumPy only, no pandas)")
plt.legend()
plt.grid(True)
plt.show()