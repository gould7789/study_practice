# list
bar = []
foo = list()

# tuple
pos = ()
kin = tuple()

# dictionary
sol = {}
pin = dict()

print(type(sol), type(pin))


# 리스트와 달리 딕셔너리는 아무 객체가 없어도 삽입 가능
lun = {}
lun[0] = 10
lun["0"] = 20
lun[0.0] = 30
lun[True] = 40
lun[(1, 2)] = 50
print(lun)