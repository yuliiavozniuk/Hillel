def is_even(number):
    number = str(number)
    if number[-1] == '0' or number[-1] == '2' or number[-1] == '4' or number[-1] == '6' or number[-1] == '8':
        return True
    else:
        return False
