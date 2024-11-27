def first_word(text):
    """ Пошук першого слова """
    text = text.replace('.', ' ').replace(',', ' ')
    my_word = text.split()
    return my_word[0] if my_word else None
