list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

new_list = []
for item in list_4:
    if item != 0:
        new_list.append(item)
number_of_zeros = len(list_4) - len(new_list)
res = new_list + [0] * number_of_zeros
print(res)