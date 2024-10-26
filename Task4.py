user_input = int(input("Please enter the 5-digit number: "))

digit1 = user_input // 10000
digit2 = (user_input // 1000) % 10
digit3 = (user_input // 100) % 10
digit4 = (user_input // 10) % 10
digit5 = user_input % 10

number5 = digit5 * 10000
number4 = digit4 * 1000
number3 = digit3 * 100
number2 = digit2 * 10
number1 = digit1 * 1

print(number5 + number4 + number3 + number2 + number1)