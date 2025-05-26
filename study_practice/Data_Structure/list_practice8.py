bar = [1, 2, 3]
foo = [40, 50, 60]

# [[1, 2, 3], [40, 50, 60]]
pos = [bar, foo]
print(pos)

# [1, 2, 3, 40, 50, 60]
sol = [*bar, *foo]
print(sol)
