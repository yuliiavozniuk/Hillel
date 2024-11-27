def first_word(text):
    text = text.replace('.', ' ').replace(',', ' ')
    my_word = text.split()
    return my_word[0] if my_word else None