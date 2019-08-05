def high(x):
    """ Given a string of words, return the position of the
    word with the highest score (a worth 1, b worth 2
    c worth 3, etc...)

    x: string of (lowercase) words separated by spaces
    """
    #calcaulate the score for a word
    def word_score(word):
        '''Calcualates the score of a word
        word: a lowercase string
        '''
        score = 0
        for character in word:
            score += ord(character) - 96
        return score

    # put words into a list
    words = x.split()
    #initialize variables
    max_score = 0
    i = 0
    index = 0
    #compare score of words
    for word in words:
        score = word_score(word)
        if score > max_score:
            max_score = score
            index = i
        i += 1
    #return index of word with highest score     
    return words[index]
