def find_unique_value(some_list):
   if some_list == []:
      return None
   unique_number = [item for item in some_list if some_list.count(item) == 1]
   if unique_number:
      return unique_number[0]
   else:
      return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([]) == None, 'Test4'
assert find_unique_value([4, 4, 4]) == None, 'Test5'
print("ОК")