foo = []                    # 리스트를 생성, 요소는 0개 -> 빈 리스트 생성
pos = list()                # 리스트를 생성, 요소는 0개 -> 빈 리스트 생성
print(type(foo), type(pos))

foo = [10, 20]
pos = list((10, 20))

foo.append(10)              # 리스트에 10을 추가
pos.append(20)              # 리스트에 20을 추가
print(foo[0], "\t", pos[0])


bar = [50, 10, 30, 40, 20]

for index in range(5):
    print(bar[index], end=",\t")
    
bar[0] = 200
bar[4] = 100

print(bar)


char = [10, 20, 30, 50]

char.append(300)    # Create [10, 20, 30, 50] -> [10, 20, 30, 50, 300]
print(char[0])      # Read 
char[2] == 200      # Update
del char[1]         # Delete [10, 20, 30, 50, 300] -> [10, 30, 50, 300]