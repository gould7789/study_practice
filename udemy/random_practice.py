import random

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

random_head_or_tails = random.randint(0, 1)
if random_head_or_tails == 0:
    print("앞면")
else:
    print("뒷면")
