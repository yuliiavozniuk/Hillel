users_input = int(input('Enter your number: '))

seconds = users_input
days = seconds // (24 * 60 * 60)
rest_of_seconds = seconds % (24 * 60 * 60)
hours = rest_of_seconds // (60 * 60)
rest_of_seconds %= (60 * 60)
minutes = rest_of_seconds // 60
seconds = rest_of_seconds % 60
result = f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
if users_input > 8640000:
    print('The number is too long')
elif users_input < 0:
    print('The number is too small')
else:
    print(result)