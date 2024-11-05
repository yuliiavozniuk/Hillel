lst = []
new_list = (lst[::2])
if len(lst) == 0:
    print(0)
else:
    last_number = lst[-1]
    sum = (sum(new_list)) * last_number
    print(sum)