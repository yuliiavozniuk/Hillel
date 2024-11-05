import random

lst = [random.randint(1,10) for i in range(random.randint(3, 10))]
print(lst)
new_list = (lst[0], lst[2], lst[-2])
print(list(new_list))