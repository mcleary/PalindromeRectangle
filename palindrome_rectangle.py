def is_palindrome(word):
    """

    Return if a word is a palindrome.
    Complexity O(len(word))

    :param word:
    :return:
    """
    b_is_palindrome = True

    for i in range(int(len(word)/2)):
        print(word[i], word[-i])
        b_is_palindrome &= word[i] == word[len(word) - i - 1]

    return b_is_palindrome

input_word = 'aWWSWWa'

input_rectangle = 'QWSDOP\n'\
                  'QWSSWP\n'\
                  'QDSDOP\n'\
                  'QDSDOP\n'\
                  'QWRRWP\n'\
                  'QWSDOP'

print(is_palindrome(input_word))


a = input_rectangle.split('\n')
print(a)