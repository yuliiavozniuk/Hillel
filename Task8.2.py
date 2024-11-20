def is_palindrome(text):
    text = text.replace(' ', '').lower()
    text = ''.join(item for item in text if item.isalnum())
    reversed_text = text[::-1]
    if reversed_text == text:
        return True
    else:
        return False