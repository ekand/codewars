def high(x):
    # Code here
    def letter_score(letter):
        return ord(letter) - 96

    def word_score(word):
        score = 0
        for character in word:
            score += letter_score(character)
        return score

    words = x.split()
    max_score = 0
    i = 0
    index = 0
    for word in words:
        score = word_score(word)
        if score > max_score:
            max_score = score
            index = i
        i += 1
    return words[index]
