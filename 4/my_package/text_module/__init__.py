def reverse(text):
    return text[::-1]


def isPalindrome(text):
    new_text = ''.join(char.lower() for char in text if char.isalnum())
    return new_text == new_text[::-1]

