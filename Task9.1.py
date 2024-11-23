def popular_words(text, words):
    my_dictionary = {}
    for item in text.split():
        item = item.lower()
        if item in words:
            my_dictionary[item] = my_dictionary.get(item, 0) + 1
    else:
        for item_2 in words:
            if item_2 not in my_dictionary:
                my_dictionary[item_2] = 0
    return my_dictionary
