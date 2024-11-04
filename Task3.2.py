any_list = [12, 3, 4, 10]

if len(any_list) > 1:
    new_list = [any_list[-1]] + any_list[:-1]
    print(new_list)
else:
    print(any_list)




