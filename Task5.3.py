import string

variable_1 = input('Print your variable: ')
variable_2 = variable_1.title().replace(' ', '')
variable_3 = ''.join(filter(str.isalnum, variable_2))
print("#" + variable_3[:139])