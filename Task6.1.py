import string

letters = input('Enter your letters, please: ')
all_lett = string.ascii_letters
list = list(letters)
res = all_lett[all_lett.find(list[0]):all_lett.find(list[2])+1]
print(res)