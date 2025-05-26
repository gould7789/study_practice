def test(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g)
    
arg_1 = [1, 2, 3, 4, 5, 6, 7]
arg_2 = [10, 20, 30, 40, 50, 60, 70]

# packing and unpacking for a list
test(*arg_1)
test(*arg_2)


# of parameters of the test function
def test2(*args):
    print(args)
    print(type(args))


test2(1)
test2(1, 2)
test2(1, 2, 3)
test2(1, 2, 3, 4)


def test3(*args):
    pass    # set -> packing

bar = [2, 3, 4]

test3(*bar) # get -> unpacking