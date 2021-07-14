def duplicate_encode(word):
    word = word.lower()
    all_letters = set()
    duplicates = set()
    result = ''
    for letter in word:
        if letter in all_letters:
            duplicates.add(letter)
        else:
            all_letters.add(letter)
    for letter in word:
        if letter in duplicates:
             result += ')'
        else:
            result += '('
    return result
