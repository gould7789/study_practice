# bar = [1, 3, 5, 7, 9]
bar = [val for val in range(1, 11, 2)]


# 2, 4, 6, 8, 10
for val in range(2, 11, 2):
    print(val, end="\t")

print(bar[2:11:2])  # [5, 9]
print(bar[0:5:1])   # [1, 3, 5, 7, 9]
print(bar[0:])      # [1, 3, 5, 7, 9]
print(bar[2:])      # [5, 7, 9]
print(bar[2:4])     # [5, 7]
print(bar[2:3])     # [5]
print(bar[2:-1])    # [5, 7]

# 역순 출력
print(bar[::-1])

# 연속 출력
print(bar[::-1][:3])