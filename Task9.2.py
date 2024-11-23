def difference(*numbers):
    if len(numbers) == 0:
        return 0
    else:
        return round(max(numbers) - min(numbers),2)