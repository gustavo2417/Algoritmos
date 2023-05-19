def is_palindrome_iterative(word):
    if len(word) == 1:
        return True
    if len(word) == 0:
        return False

    inverted_word = word[::-1]

    for i in range(len(word)):
        if word[i] != inverted_word[i]:
            return False

    return True
