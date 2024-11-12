import string
import keyword

variable_1 = input('Print your variable: ')
if variable_1[0].isdigit():
    print(False)
elif any(chr.isupper() for chr in variable_1):
    print(False)
elif any(chr in string.punctuation and chr != '_' for chr in variable_1):
    print(False)
elif variable_1 == '_':
    print(True)
elif variable_1.startswith ('_') and variable_1.count ('_') == len(variable_1):
    print(False)
elif variable_1 in keyword.kwlist:
    print(False)
elif ' ' in variable_1:
    print(False)
else:
    print(True)