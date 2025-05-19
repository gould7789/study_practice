# bar = [1, 3, 5, 7, 9]
bar = [val for val in range(1, 11, 2)]
print(bar)


# pos = bar
# foo = bar
# pos = foo = bar

# pos[0] = 10     # 리스트의 맨앞쪽 인덱스부터 [0]로 시작
# foo[-1] = 100   # 리스트의 맨뒷쪽 인덱스부터 [-1]로 시작
# print(foo)


# [], list

foo = list(bar)
pos = bar.copy()
kin = bar[:]

bar[0] = 100
print(foo)
print(pos)
print(kin)