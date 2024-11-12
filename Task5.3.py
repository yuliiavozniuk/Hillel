variable_1 = input('Print your variable: ')
variable_2 = variable_1.title().replace(' ', '')
variable_3 = ''.join(item for item in variable_2 if item.isalpha())
print("#" + variable_3[:139])