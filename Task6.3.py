number = int(input('Enter your number: '))

while number > 9:
    original_number = 1
    for item in str(number):
        original_number = original_number * int(item)
    number = original_number
print(number)