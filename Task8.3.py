def find_unique_value(some_list):
   unique_number = [item for item in some_list if some_list.count(item) == 1]
   return unique_number[0]