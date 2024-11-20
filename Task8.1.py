def add_one(some_list):
    numbers = ''.join(str(item) for item in some_list)
    new_number = int(numbers) + 1
    my_string = str(new_number)
    result = [int(chr) for chr in my_string]
    return result
