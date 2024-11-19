def common_elements():
    first_list = list(range(0, 100, 5))
    new_set = set(first_list)
    second_list = list(range(0, 100, 3))
    new_set_2 = set(second_list)
    intersection_set = new_set.intersection(new_set_2)
    return intersection_set


print(common_elements())