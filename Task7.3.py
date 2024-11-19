def second_index(text, some_str):
  if text.count(some_str) > 1:
    index_1 = text.find(some_str)
    index_2 = text.find(some_str, index_1 + 1)
    return index_2
  else:
    return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
