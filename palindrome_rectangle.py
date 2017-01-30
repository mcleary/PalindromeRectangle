
class CharMatrix:

    def __init__(self, input_matrix):

        if len(input_matrix) == 0:
            raise ValueError("input_matrix is empty")

        lines = input_matrix.split('\n')

        self.width = len(lines[0])
        self.height = len(lines)

        for line in lines:
            if len(line) != self.width:
                raise ValueError("The char matrix must have lines with equal sizes")

        self.input_matrix = input_matrix.replace('\n', '')

    def at(self, i, j):

        if i >= self.width or j >= self.height:
            raise IndexError("index out of bounds")

        # print("CharMatrix {i},{j} = {c}".format(i=i, j=j, c=self.input_matrix[i+j*self.width]))
        return self.input_matrix[i + j * self.width]

    def __str__(self):
        return "CharMatrix({width}, {height})".format(width=self.width, height=self.height)


class RectanglePalindromeAnalyser:

    def __init__(self, char_matrix):

        if not isinstance(char_matrix, CharMatrix):
            raise ValueError("char_matrix must be of type CharMatrix")

        if char_matrix.width < 2 or char_matrix.height < 2:
            raise ValueError("char_matrix must be at least 2x2")

        self.char_matrix = char_matrix
        self.num_op = 0

    def find_brute_force(self):

        idx_i = -1
        idx_j = -1
        rect_width = -1
        rect_height = -1

        for rw in range(2, self.char_matrix.width):
            for rh in range(2, self.char_matrix.height):

                for i in range(self.char_matrix.width - rw):
                    for j in range(self.char_matrix.height - rh):

                        if self.__is_rect_palindrome(i, j, rw, rh):
                            idx_i = i
                            idx_j = j
                            rect_width = rw
                            rect_height = rh

        return idx_i, idx_j, rect_width, rect_height, self.num_op

    def __is_rect_palindrome(self, start_i, start_j, width, height):
        is_pal_hor1 = self.__is_palindrome(start_i, start_j, width, 'hor')
        is_pal_hor2 = self.__is_palindrome(start_i, start_j + height - 1, width, 'hor')
        is_pal_ver1 = self.__is_palindrome(start_i, start_j, height, 'ver')
        is_pal_ver2 = self.__is_palindrome(start_i + width - 1, start_j, height, 'ver')

        # print(is_pal_hor1, is_pal_hor2, is_pal_ver1, is_pal_ver2)

        return is_pal_hor1 and is_pal_hor2 and is_pal_ver1 and is_pal_ver2

    def __is_palindrome(self, start_i, start_j, size, direction):
        b_is_palindrome = True

        if direction == 'ver':
            for i in range(int(size / 2)):
                idx = start_j + i
                ridx = size - i + start_j - 1

                char1 = self.char_matrix.at(start_i, idx)
                char2 = self.char_matrix.at(start_i, ridx)

                self.num_op += 1

                # print(char1, char2)

                b_is_palindrome &= char1 == char2

        if direction == 'hor':
            for j in range(int(size / 2)):
                idx = start_i + j
                ridx = size - j + start_i - 1

                char1 = self.char_matrix.at(idx, start_j)
                char2 = self.char_matrix.at(ridx, start_j)

                self.num_op += 1

                # print(char1, char2)

                b_is_palindrome &= char1 == char2

        return b_is_palindrome


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


def main():
    input_rectangle = 'QWSDOP\n' \
                      'QWSSWP\n' \
                      'QDSDOP\n' \
                      'QDSDOP\n' \
                      'QWRRWP\n' \
                      'QWSDOP'

    char_matrix = CharMatrix(input_rectangle)
    palindrome_analyser = RectanglePalindromeAnalyser(char_matrix)
    print(palindrome_analyser.find_brute_force())

if __name__ == '__main__':
    main()
