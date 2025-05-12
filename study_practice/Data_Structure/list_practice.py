# append

# bar = []
# foo = list()

# bar.append(100)
# bar.append(200)
# print(bar)
# print(bar[0], "\t", bar[1])


# print(type(bar), type(foo))

# insert

# bar = [10, 200, 1, 9]

# bar.insert(0, 300)
# bar.insert(2, -10)
# bar.append(-200)

# print(bar)

# for i, b in enumerate(bar):
#     print(f"{i}번째 값: {b}")


bar = list((40, 50, 30, 20))

print(bar[0], "\t", bar[3])

for val in bar:
    print(bar)

# bar = [10, 12, 14, 16, 18, 20]
bar = [val for val in range(10, 21, 2)]

print(bar.pop(0))
print(bar)
print(bar.pop(2))
print(bar)