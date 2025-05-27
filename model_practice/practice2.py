bar = [(2, 3), (10, 30), (100, 300)]

foo = [val for val in bar]

# [(2, 3), (10, 30), (100, 300)]
print(foo)

# (2, 3)
print(foo[0])

# 2, 3
print(foo[0][0])
print(foo[0][1])

# 100, 300
print(foo[2][0])
print(foo[2][1])