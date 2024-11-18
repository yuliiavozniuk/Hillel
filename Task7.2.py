def correct_sentence(text):
    if text[-1] == '.':
        return f'{text.capitalize()}'
    elif '.' in text[0:]:
        return f'{text.title()}.'
    else:
        return f'{text.capitalize()}.'


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')