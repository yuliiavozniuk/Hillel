first_digit = float(input("Enter first digit: "))
operator = input("Enter +, -, / or *: ")
second_digit = float(input("Enter second digit: "))

if operator == "+":
    print(first_digit + second_digit)
elif operator == "-":
    print(first_digit - second_digit)
elif operator == "*":
    print(first_digit * second_digit)
elif operator == "/":
    if second_digit == 0:
        print("The divisor cannot be equal to 0")
    else:
        print(first_digit / second_digit)
else:
    print("Something went wrong!")

